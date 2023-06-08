from connectors.rmq import Connector
from helpers.helpers import *
from helpers.request_params import url, object, headers
from dotenv import load_dotenv
import os, schedule, time
load_dotenv()

def main():
    num_of_odds = os.environ.get('NUM_OF_ODDS')
    connection = Connector()

    data = connection.receiver()

    all_uuids = fetchUuids(fetchOdds(fetchMarkets(data, 2)))
    picked_uuids = pickUuids(all_uuids, int(num_of_odds))
    makeRequest(url, object(picked_uuids), headers())

