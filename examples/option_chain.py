import configparser
from fast_arrow import (
    Client,
    Stock,
    OptionChain,
    Option,
)

print("----- running {}".format(__file__))

#
# get auth_data (see https://github.com/westonplatter/fast_arrow_auth)
#
with open("fast_arrow_auth.json") as f:
    auth_data = json.loads(f.read())


#
# initialize client with auth_data
#
client = Client(auth_data)


#
# fetch the stock info for TLT
#
symbol = "TLT"
stock = Stock.fetch(client, symbol)


#
# get the TLT option chain info
#
stock_id = stock["id"]
option_chain = OptionChain.fetch(client, stock_id, symbol)
option_chain_id = option_chain["id"]
expiration_dates = option_chain['expiration_dates']


#
# reduce the number of expiration dates we're interested in
#
next_3_expiration_dates = expiration_dates[0:3]


#
# get all options on the TLT option chain
#
ops = Option.in_chain(client, option_chain_id, expiration_dates=next_3_expiration_dates)


#
# merge in market data fro TLT option instruments
#
ops = Option.mergein_marketdata_list(client, ops)
