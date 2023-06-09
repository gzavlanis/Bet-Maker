import os, schedule, time, sys
sys.path.append("./")
sys.path.append("connectors")
sys.path.append("helpers")
from connectors.rmq import Connector
# from helpers.helpers import *
# from helpers.request_params import url, object, headers
from dotenv import load_dotenv
load_dotenv()

# num_of_odds = os.environ.get('NUM_OF_ODDS')
connection = Connector()

# data = connection.receiver()

# all_uuids = fetchUuids(fetchOdds(fetchMarkets(data, 2)))
# print(all_uuids)

# picked_uuids = pickUuids(all_uuids, int(num_of_odds))
# print(picked_uuids)

# makeRequest(url, object(picked_uuids), headers())

connection.consumer()
