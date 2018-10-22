import json

# Make it work for Python 2+3 and with Unicode
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str


json_file_name="Google1"
# Define data
data = {'Cash':1000000.00,
        'Buy Parameters': {'buy_perc_delta':5,
                            'buy_val_delta':0.05,
                            'buy_max_shares':100,
                            'buy_max_value':100,
                            'buy_trade_comm':0},
        'Sell Parameters': {'sell_perc_delta':5,
                            'sell_val_delta':0.05,
                            'sell_max_shares':1000,
                            'sell_max_value':1000,
                            'sell_trade_comm':0}}

# Write JSON file
with io.open('{}.json'.format(json_file_name), 'w') as outfile: #, encoding='utf8'
    json_Data = json.dumps(data,indent=4, sort_keys=True,separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(json_Data))

# Read JSON file
# with open('{}.json'.format(json_file_name)) as data_file:
#     data_loaded = json.load(data_file)
#
# print(data==data_loaded)
# print(data_loaded)
