import requests
import json

#Function for finding the player count
def PlayerCount(steamID):
    API = "https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/"
    data = {
            "appid" : steamID
    }
#Gets the Information from the API
    response = requests.get(API, data)
#Checks to see if the API is down, or if the token entered is not a valid steam game
    if response.status_code != 200:
        print("Token is invalid or the Steam DB API is down, please retry")
    else:
        #Loads the information to a JSON and then prints the player count
        my_json = json.loads(response.text)
        print(f"Current player count for ID {steamID} = {my_json['response']['player_count']}")

#Main function for calling the player count function
while 1:
    ID = input("Please enter a valid Steam game ID to find the current active player count, or enter q to quit \n")
# Checks to see if the ID is equal to q which will quit the program
    if ID == 'q':
        print("Quitting")
        break
# Insures that ID is a digit, if not it will rerun the input
    if ID.isdigit():
        PlayerCount(ID)
    else:
        print("Invalid ID, please enter a valid ID"
