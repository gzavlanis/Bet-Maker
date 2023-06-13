import pika, os, json, time
from dotenv import load_dotenv
from helpers.helpers import *
from helpers.request_params import *
load_dotenv()

# environmentals
host = os.environ.get('RMQ_URI')
exchange = os.environ.get('EXCHANGE')
routing_key = os.environ.get('ROUTING_KEY')
queue = os.environ.get('QUEUE_NAME')
bet_time = os.environ.get('BET_TIME')
max_odds = os.environ.get('MAX_ODDS')

class Connector:
    message = None
    last_place_bet_time = 0
    place_bet_timeout_min = int(bet_time) # frequency of bets creation

    # Singleton pattern
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
    # create connection
    def __init__(self):
        try:
            self.connection = pika.BlockingConnection(pika.URLParameters(host))
            print(f"[v] Connection with {host} was successfull.")
            print('Receiving messages. To exit press CTRL+C.')
        except Exception as error:
            print("[x] Error:", error)
            self.connection = pika.BlockingConnection(pika.URLParameters(host))
            print("[v] Connection restored.")

    # message receiver
    def consumer(self):
        channel = self.connection.channel()
        result = channel.queue_declare(queue = queue, exclusive = True, auto_delete = True)
        queue_name = result.method.queue
        channel.queue_bind(queue = queue_name, exchange = exchange, routing_key = routing_key)
        channel.basic_consume(queue = queue_name, on_message_callback = self.callback, auto_ack = True)
        try:
            channel.start_consuming()
        except Exception as error:
            print("Error: ", error)
            channel.stop_consuming()
    
    def close_connection(self):
        self.connection.close()
        print("Connection closed.")

    def callback(self, ch, method, properties, body):
        current_time = time.time()
        if current_time > self.last_place_bet_time + 60 * self.place_bet_timeout_min:
            self.message = json.loads(body)
            print("Placing bet")
            self.bet_maker()
            self.last_place_bet_time = current_time

    def bet_maker(self):
        all_uuids = fetchUuids(fetchOdds(fetchMarkets(self.message)))
        picked_uuids = pickUuids(all_uuids, int(pickNumOfOdds(int(max_odds))))
        if len(picked_uuids) == 0:
            print("No odds picked this time.")
        else:
            print("The bets were picked are: ", picked_uuids)
        makeRequest(url, object(picked_uuids), headers())