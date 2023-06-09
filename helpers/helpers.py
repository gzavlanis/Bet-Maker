import requests, random
import numpy as np

def fetchMarkets(message):
    return message.get('body', {}).get('markets', [])

def fetchOdds(markets_list):
    odds_list = []
    for market in markets_list:
        odds_list.append(market.get('odds', []))
    return odds_list

def fetchUuids(list):
    uuids = []
    for sublist in list:
        for dict in sublist:
            uuids.append(dict.get('properties', {}).get('uuid'))
    return uuids

def pickNumOfOdds(max_number):
    return random.randint(0, max_number)

def pickUuids(uuids, num): # from the list of all pick a num of odds
    picked_uuids = []
    if len(uuids) == 0: pass
    indexes = np.random.choice(range(1, len(uuids)), num, replace = False)
    for index in indexes:
        picked_uuids.append(uuids[index])
    return picked_uuids

def makeRequest(url, data, headers):
    response = requests.post(url, json = data, headers = headers)
    if response.status_code == 200:
        print("Request successful!")
        print("Response:", response.json())
    else: print("Request failed. Status code: ", response.status_code)