import time
from datetime import datetime as dt
import json
import io

try:
    to_unicode = unicode
except NameError:
    to_unicode = str


def update_host(host_path):
    global stock_value
    global stock_time
    global stock_point
    stock_value=[]
    stock_point=[]
    stock_time=[]

    with open(host_path, 'r+') as file:
        global stock_symbol
        stock_symbol=file.readline().split(",")[0]
        for line in file:
            try:
                # hour=int(line.split(",")[1].split("-")[0])
                # minute=int(line.split(",")[1].split("-")[1])
                # second=int(line.split(",")[1].split("-")[2])

                stock_value.append(float(line.split(",")[2]))
                stock_point.append(line.split(",")[0])
                stock_time.append(line.split(",")[1])
                # print(int(line.split(",")[1].split("-")[0]))
                # print(type(int(line.split(",")[1].split("-")[0])))
            except ValueError:
                pass

def model_Run(buy_perc_delta,buy_val_delta,buy_max_shares,buy_max_value,buy_trade_comm,sell_perc_delta,sell_val_delta,sell_max_shares,sell_max_value,sell_trade_comm,cash):
    global cash_model
    cash_model=cash
    shares=0

    for i in range(1,len(stock_value)-1):
        perc_delta=(stock_value[i]-stock_value[i-1])/stock_value[i-1]
        value_delta=stock_value[i]-stock_value[i-1]
        if int(buy_perc_delta*1000000000)!=0 and perc_delta<buy_perc_delta and cash_model>stock_value[i]: # perc_delta<buy_perc_delta or
            shares=int(cash_model/stock_value[i])
            cash_model-=shares*stock_value[i]+buy_trade_comm
        elif int(buy_val_delta*100000000)!=0 and value_delta<buy_val_delta and cash_model>stock_value[i]: # perc_delta<buy_perc_delta or
            shares=int(cash_model/stock_value[i])
            cash_model-=shares*stock_value[i]+buy_trade_comm
        elif int(sell_perc_delta*1000000000)!=0 and perc_delta>sell_perc_delta and shares>0: #perc_delta>sell_perc_delta or
            cash_model+=shares*stock_value[i]-sell_trade_comm
            shares=0
        elif int(sell_val_delta*100000000)!=0 and value_delta>sell_val_delta and shares>0: #perc_delta>sell_perc_delta or
            cash_model+=shares*stock_value[i]-sell_trade_comm
            shares=0
        else:
            pass
        i+=1
    if shares>0:
        cash_model+=shares*stock_value[len(stock_value)-1]-sell_trade_comm
        shares=0

def load_Model_Para(model_File):
    with open(model_File) as data_file:
        data_loaded = json.load(data_file)

        global para_cash
        global para_buy_perc_delta
        global para_buy_val_delta
        global para_buy_max_shares
        global para_buy_max_value
        global para_buy_trade_comm
        global para_sell_perc_delta
        global para_sell_val_delta
        global para_sell_max_shares
        global para_sell_max_value
        global para_sell_trade_comm

        para_buy_perc_delta=data_loaded['Buy Parameters']['buy_perc_delta']
        para_buy_val_delta=data_loaded['Buy Parameters']['buy_val_delta']
        para_buy_max_shares=data_loaded['Buy Parameters']['buy_max_shares']
        para_buy_max_value=data_loaded['Buy Parameters']['buy_max_value']
        para_buy_trade_comm=data_loaded['Buy Parameters']['buy_trade_comm']
        para_sell_perc_delta=data_loaded['Sell Parameters']['sell_perc_delta']
        para_sell_val_delta=data_loaded['Sell Parameters']['sell_val_delta']
        para_sell_max_shares=data_loaded['Sell Parameters']['sell_max_shares']
        para_sell_max_value=data_loaded['Sell Parameters']['sell_max_value']
        para_sell_trade_comm=data_loaded['Sell Parameters']['sell_trade_comm']
        para_cash=data_loaded['Cash']

def save_Model_Para(model_file_save_name,buy_perc_delta,buy_val_delta,buy_max_shares,buy_max_value, buy_trade_comm,
                    sell_perc_delta,sell_val_delta,sell_max_shares,sell_max_value,sell_trade_comm,
                    cash):
    data = {'Cash':cash,
            'Buy Parameters': {'buy_perc_delta':buy_perc_delta,
                                'buy_val_delta':buy_val_delta,
                                'buy_max_shares':buy_max_shares,
                                'buy_max_value':buy_max_value,
                                'buy_trade_comm':buy_trade_comm},
            'Sell Parameters': {'sell_perc_delta':sell_perc_delta,
                                'sell_val_delta':sell_val_delta,
                                'sell_max_shares':sell_max_shares,
                                'sell_max_value':sell_max_value,
                                'sell_trade_comm':sell_trade_comm}}
    with io.open(model_file_save_name, 'w') as outfile: #, encoding='utf8'
        json_Data = json.dumps(data,indent=4, sort_keys=True,separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(json_Data))
