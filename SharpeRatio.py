import pandas as pd
import quandl

start = pd.to_datetime('2018-01-01')
end = pd.to_datetime('2019-03-01')

aapl = quandl.get('WIKI/AAPL.11', start_date=start, end_date=end, authtoken='g6Cs2-b1GNVFEiaaw5LF')
cisco = quandl.get('WIKI/CSCO.11', start_date=start, end_date=end, authtoken='g6Cs2-b1GNVFEiaaw5LF')
ibm = quandl.get('WIKI/IBM.11', start_date=start, end_date=end, authtoken='g6Cs2-b1GNVFEiaaw5LF')
amzn = quandl.get('WIKI/AMZN.11', start_date=start, end_date=end, authtoken='g6Cs2-b1GNVFEiaaw5LF')

aapl.to_csv('AAPL_CLOSE')
cisco.to_csv('CISCO_CLOSE')
ibm.to_csv('IBM_CLOSE')
amzn.to_csv('AMZN_CLOSE')
