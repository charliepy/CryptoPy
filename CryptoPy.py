from lib.functions import get_quandl_data, getLogger
from datetime import datetime
import os
import numpy as np
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import plotly.figure_factory as ff

# Constants
LOGGER = getLogger()
STARTDATE = '2017-01-01'
ENDDATE = datetime.now().strftime('%Y-%m-%d')
LOGGER.info(STARTDATE)

# Start
# py.init_notebook_mode(connected=True)

# Pull pricing data for 3 more BTC exchanges
exchanges = ['KRAKEN', 'COINBASE', 'BITSTAMP', 'COINSBANK', 'ITBIT']
exchange_data = {}

for exchange in exchanges:
    exchange_code = 'BCHARTS/{}USD'.format(exchange)
    btc_exchange_df = get_quandl_data(exchange_code, STARTDATE, ENDDATE)
    exchange_data[exchange] = btc_exchange_df
    LOGGER.info(list(exchange_data[exchange]))
    LOGGER.info(exchange_data[exchange].last_valid_index())
    testdate = exchange_data[exchange].last_valid_index().strftime('%Y-%m-%d')

LOGGER.info(testdate < ENDDATE)

btc_trace = go.Scatter(
    x=exchange_data['COINBASE'].index,
    y=exchange_data['COINBASE']['Weighted Price'])
# py.iplot([btc_trace])
# py.plot([btc_trace])
