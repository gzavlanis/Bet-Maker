from connectors.rmq import Connector
import json

connection = Connector()
data = connection.receiver()

print(data)