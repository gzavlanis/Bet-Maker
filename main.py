from connectors.rmq import Connector

def main():
    try:
        connection = Connector()
        connection.consumer()
    except KeyboardInterrupt:
        print("Interrupted from user (CTRL+C)")
        connection.close_connection()

if __name__ == '__main__':
        main()