from connectors.rmq import Connector

def main():
    try:
        while True:
            connection = Connector()
            try:
                connection.consumer()
            except Exception as error:
                print("Error: ", error)
                pass
    except KeyboardInterrupt:
        print("Interrupted from user (CTRL+C)")
        connection.close_connection()

if __name__ == '__main__':
    main()