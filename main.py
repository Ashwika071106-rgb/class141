from flask import Flask,jsonify,request
import csv

all_movies = []

with open("venv\movies.csv", encoding='utf8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
disliked_movies = []
not_watched_movies = []

app = Flask(__name__)

@app.route('/get-movie')
def get_movie():
    return jsonify({
        "data" : all_movies[0],
        "status" : "Success"
    })

@app.route('/liked-movie',methods=["POST"])
def liked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status" : "Success"
    }),201

@app.route('/disliked-movies',methods=["POST"])
def disliked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    disliked_movies.append(movie)
    return jsonify({
        "Status" : "Success"
    }),201

@app.route('/not-watched-movies',methods=["POST"])
def not_watched_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_watched_movies.append(movie)
    return jsonify({
        "Status" : "Success"
    }),201

if(__name__ == "__main__"):
    app.run()