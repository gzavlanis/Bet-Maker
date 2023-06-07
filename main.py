from connectors.rmq import Connector
from helpers.helpers import *
from dotenv import load_dotenv
import os

connection = Connector()
data = connection.receiver()
print("Received: ", data)
