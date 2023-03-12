import requests
username = 'kuba115x'

r = requests.get(f'https://api.chess.com/pub/player/{username}/games/archives')
result = r.json()
archivesList = []
for x in  range(len(result['archives'])):
    archivesList.append(result['archives'][x])
print(archivesList)


gameList = []
r = requests.get('https://api.chess.com/pub/player/kuba115x/games/2023/03')
result = r.json()


print(result)

