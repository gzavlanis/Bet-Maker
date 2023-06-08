import pika, os, sys, json
from dotenv import load_dotenv
load_dotenv()

# environmentals
host = os.environ.get('RMQ_URI')
exchange = os.environ.get('EXCHANGE')
routing_key = os.environ.get('ROUTING_KEY')
queue = os.environ.get('QUEUE_NAME')

class Connector(object):
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
        except Exception as error:
            print("[x] Error:", error)
            self.connection = pika.BlockingConnection(pika.URLParameters(host))
            print("[v] Connection restored.")

    def close_connection(self):
        self.connection.close()
        print("Connection closed.")

    # consume and collect messages
    def receiver(self):
        messages = []
        channel = self.connection.channel()
        result = channel.queue_declare(queue = queue, exclusive = True, auto_delete = True)
        queue_name = result.method.queue

        def callback(ch, method, properties, body):
            body = json.loads(body)
            messages.append(body)
            
        channel.queue_bind(queue = queue_name, exchange = exchange, routing_key = routing_key)

        channel.basic_consume(queue = queue_name, on_message_callback = callback, auto_ack = True)
        print('[*] Waiting for messsages. To exit press CTRL+C.')
        try:
            try:
                channel.start_consuming()
            except Exception as error:
                print("Error:", error)
        except KeyboardInterrupt:
            print('Interrupted from user')
            channel.stop_consuming()
            self.close_connection()

        return messages

