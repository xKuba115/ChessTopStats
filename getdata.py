import requests
import json
import pymongo
gameList = []
#FUNCTIONS
nickname = 'Polish_fighter3000'
client = pymongo.MongoClient("x")
db = client["Chess"]
collection = db[f"{nickname}Games"]

def GetArchivesByUsername(username):
    r = requests.get(f'https://api.chess.com/pub/player/{username}/games/archives')
    result = r.json()
    archivesList = []
    for x in  range(len(result['archives'])):
        archivesList.append(result['archives'][x])
    print(f'found {len(archivesList)} archives ')
    return archivesList
def GetGameDataByArchivesList(archivesList):
    username = 'Polish_fighter3000'
    iterator = 1
    for archive in archivesList:
        r = requests.get(archive)
        result = r.json()
        for x in range (len(result['games'])):
            if(result['games'][x]['white']['username'])==username:
                enemy = result['games'][x]['black']['username']
                myColor = 'white'
            else:
                enemy = result['games'][x]['white']['username']
                myColor='black'
            if(result['games'][x]['white']['result'])=='win':
                winningColor = 'white'
            else:
                winningColor = 'black'

            gameData = {
                'enemy': enemy,
                'myColor':myColor,
                'winningColor': winningColor
            }
            gameList.append(gameData)
        print(f'Archive {iterator} done')
        iterator = iterator +1
    collection.insert_many(gameList)

    return gameList
GetGameDataByArchivesList(GetArchivesByUsername(nickname))
client.close()
