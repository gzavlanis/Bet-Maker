from connectors.rmq import Connector

def main():
    connection = Connector()
    connection.consumer()

if __name__ == '__main__':
    main()