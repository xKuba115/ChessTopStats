#ChessTopStats

This project is a website that utilizes Python as its backend. It fetches information from the Chess.com API regarding the top 10 chess players, processes and stores the data in a NoSQL MongoDB database, and then provides a Flask-based API in Python. This API, when given the names of two players, returns their game records against each other on Chess.com. The results are displayed on an HTML/CSS/JS webpage.

##Project Overview
The Chess.com Player Stats Website is designed to provide users with easy access to the game records of the top 10 chess players on Chess.com. The project consists of the following components:

Backend in Python: The project's backend is built using Python. It is responsible for fetching data from the Chess.com API and processing it for storage and retrieval.

Chess.com API Integration: The project connects to the Chess.com API to obtain information about the top 10 chess players. This includes their usernames, ratings, and game statistics.

MongoDB Database: The processed data is stored in a NoSQL MongoDB database. The database stores player profiles, ratings, and game records for future use.

Flask API: A Flask-based API has been implemented in Python to provide a user-friendly interface for accessing player game records. It accepts the names of two players and retrieves their historical game data against each other from the MongoDB database.

HTML/CSS/JS Webpage: The website's frontend is developed using HTML, CSS, and JavaScript. It allows users to pick the names of two players, triggers the API call to retrieve their game records, and displays the results on the webpage.

##Dependencies
Python
Flask
pymongo (Python driver for MongoDB)
HTML/CSS/JS for frontend
Chess.com API