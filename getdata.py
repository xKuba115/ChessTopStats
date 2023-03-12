import requests

#FUNCTIONS

def GetArchivesByUsername(username):
    r = requests.get(f'https://api.chess.com/pub/player/{username}/games/archives')
    result = r.json()
    archivesList = []
    for x in  range(len(result['archives'])):
        archivesList.append(result['archives'][x])
    return archivesList
def GetGamesByArchivesList(archivesList):
    gameList = []
    for archive in archivesList:
        r = requests.get(archive)
        result = r.json()
        for game in result['games']:
            gameList.append(game['url'])
    print(len(gameList))
GetGamesByArchivesList(GetArchivesByUsername('kuba115x'))