from connectors.rmq import Connector
from helpers.helpers import *
from helpers.request_params import url, object, headers
from dotenv import load_dotenv
import os, schedule, time, threading
load_dotenv()

num_of_odds = os.environ.get('NUM_OF_ODDS')
running_time = os.environ.get('MINUTES')
num_of_messages = os.environ.get('NUM_OF_MESSAGES')

connection = Connector()
data = connection.receiver()

def process():
    messages = data[:int(num_of_messages)]
    all_uuids = fetchUuids(fetchOdds(fetchMarkets(messages, 2)))
    picked_uuids = pickUuids(all_uuids, int(num_of_odds))
    makeRequest(url, object(picked_uuids), headers())

def schedule_task():
    schedule.every(int(running_time)).minutes.do(process) # schedule the process function to run every running_time minutes
    while True:
        schedule.run_pending()
        time.sleep(1)

schedule_thread = threading.Thread(target = schedule_task)
schedule_thread.start()
