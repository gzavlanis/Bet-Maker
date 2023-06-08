# create fake bets in specific platform

#### This application creates a connection in an RMQ exchange, which corresponds with a platform.
#### After that, it collects random messages and pick some odds of them to create a fake bet request in client api.

#### To run this application, you must do the following steps:

## Create the Python virtual environment

#### Please, have in mind that you have to install all the required packages.

#### To do that, run in terminal, inside the project folder the following: 

Windows:

```
python -m venv .venv
\.venv\Scripts\activate
pip install -r requirements.txt
```

Linux:

```
python3 -m venv .venv
source .venv/Scripts/activate.bat
pip install requirements.txt
```
## Environment

#### Create your file as follows:

| Variable | Usage |
| ------------ | -------------------------------------------------------------- |
| PG_HOST | **string** the url of the host |
| PG_PORT | **string** the port of connection |
| PG_USER | **string** the username |
| PG_PASSWORD | **string** the password to connect |
| PG_DATABASE | **string** the name of the database |
| API_KEY | **string** your secret key to connect to Openai API |
| RUNNING_HOURS | **string** the time that the scheduler will rerun the app in hours |
| RUNNING_MINUTES | **string** the time that the scheduler will rerun the app in minutes |
| LANG_ID | **string** for test reasons you can add a specifing lang_id to take translations only in one language |

#### Τhe scheduler runs the main function again and again in a period of time defined by you. This fuction check the table that you created and the original dataset and collects data that they don't have translation. Then, runs the translation process again for these data.
#### The main function takes pamateres, depends on what dataset you wan to translate. You can define the jobs of the scheduler and the parameters of the main function in the app.py file, which is the running file.

### That's it Enjoy!