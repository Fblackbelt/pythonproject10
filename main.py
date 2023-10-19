import requests
import json

def PlayerCount(steamID):
    API = "https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1"
    data = {
            "appid" : steamID
            }
    response = requests.get(API, data)
    print(response.status_code)
    if response.status_code != 200:
        print("Steam DB API is down, please retry later")
        exit(0)
    else:
        my_json = json.loads(response.text)
        print(f"Current player count for ID {steamID} = {my_json['response']['player_count']}")


while 1:
    ID = input("Please enter a valid Steam game ID to find the current active player count, or enter q to quit \n")
    if ID == 'q':
        print("Quitting")
        break
    if ID.isdigit():
        PlayerCount(ID)