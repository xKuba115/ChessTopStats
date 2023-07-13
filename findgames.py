import requests
import json
import pymongo
from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
client = pymongo.MongoClient("connectionstring")
db = client["Chess"]

@app.route("/stats", methods=["GET"])
def FindGamesByEnemy():
    data = request.args.to_dict()
    myNickname = data["firstPlayer"]
    enemyNickname = data["secondPlayer"]
    collection = db[f"{myNickname}Games"]
    wins = 0
    loses = 0
    gamesplayed = 0
    games = collection.find({'enemy': enemyNickname})


    for game in games:

        if(game['myColor']==game['winningColor']):
            wins = wins +1
        else:
            loses = loses+1
        gamesplayed = gamesplayed +1
    print(f"Games played between {myNickname} and {enemyNickname}: {gamesplayed}")
    print(f"{myNickname} won: {wins}")
    print(f"{myNickname} lost: {loses}")
    return (f"Games played between {myNickname} and {enemyNickname}: {gamesplayed}, {myNickname} won: {wins}, {myNickname} lost: {loses}")


if __name__ == "__main__":
    app.run(port=3000)