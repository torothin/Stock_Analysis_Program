import glob
import datetime
import pandas

date="05-26-17"
l=glob.glob('Google Data/{}/*.csv'.format(date))

date_String=datetime.datetime.now().strftime("%m-%d-%y")
new_list=[]
ticker_name="GOOG"
new_list_col=["Time", "Price"]

for i in range(0,len(l)):
    with open(l[i], 'r+') as file:
        for line in file:
            try:
                stock_value=float(line.split(",")[2])
                stock_time=line.split(",")[1]
                new_list.append([stock_time, stock_value])
            except ValueError:
                pass
print
df=pandas.DataFrame(new_list,columns=new_list_col)
df.index.name = ticker_name
df.to_csv("Yahoo_{}_{}.csv".format(ticker_name,date))
