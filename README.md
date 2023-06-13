# Bet Maker Application
## Create fake bets in specific platform

#### This application creates a connection in an RMQ exchange, which corresponds with a platform.
#### After that, it collects random messages and pick some odds of them to create a fake bet request in client api.

#### To run this application, you must do the following steps:

## Create the Python virtual environment

#### Please, have in mind that you have to install all the required packages.

#### To do that, run in terminal, inside the project folder the following: 

Windows:

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Linux:

```
python3 -m venv .venv
source .venv/Scripts/activate.bat
pip install requirements.txt
```
## Environment

#### Create your .env file as follows:

| Variable | Usage |
| ------------ | -------------------------------------------------------------- |
| RMQ_URI | **string** the uri to make connection to Rabbit MQ |
| API_URL | **string** the url of the client API |
| API_KEY | **string** api key taken from client panel |
| EXCHANGE | **string** the Rabit MQ exchange to connect the queue in order to recieve messages |
| QUEUE_NAME | **string** the name of the queue that the project creates |
| ROUTING_KEY | **string** depending of the routing key, you can change the type of data you receive |
| BET_TIME | **string** the time in minutes between every fake bet creation |
| RUNNING_MINUTES | **string** the time that the scheduler will rerun the app in minutes |
| MAX_ODDS | **string** the max number of odds that the bet will have |

#### To run this program, write in your terminal:
```
python main.py
```

### That's it Enjoy!