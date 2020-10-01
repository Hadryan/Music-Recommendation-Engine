# web_app/routes/suggestion_routes.py

from flask import Blueprint, render_template
from web_app.services.spotify_service import spot as sp
import requests
from dotenv import load_dotenv
import os
import joblib
import pandas as pd
import sklearn
# from web_app.visualizations.radar_charts import visualization

suggestion_routes = Blueprint("suggestion_routes", __name__)

load_dotenv()

SPOTIFY_AUTHORIZATION = os.getenv("SPOTIFY_SECRET")

@suggestion_routes.route("/suggest/<artist_name>/<track_name>",
                         methods=["GET", "POST"])
def suggest_songs(artist_name, track_name):

    """
    Gets access token utilizing client credentials
    """

    headers = {
        'Authorization': f"Basic {SPOTIFY_AUTHORIZATION}"
    }

    data = {
        'grant_type': 'client_credentials'
    }

    response = requests.post('https://accounts.spotify.com/api/token',
                             headers=headers,
                             data=data)

    access_token = response.json()['access_token']

    """
    Queries Spotify API to pull song ID
    """

    artist_name = artist_name
    track_name = track_name
    # artist_name = request.form["artist"]
    # track_name = request.form["title"]

    user_query = artist_name + ' ' + track_name

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {access_token}",
    }

    params = (
        ('q', user_query),
        ('type', 'track,artist'),
    )

    song_info = requests.get('https://api.spotify.com/v1/search',
                             headers=headers,
                             params=params)

    track_id = song_info.json()['tracks']['items'][0]['id']

    """
    Loads pickled model
    """

    filename = 'models/KNN_pickle.sav'
    knn_model = joblib.load(filename)



    tracks = pd.read_csv("https://raw.githubusercontent.com/Build-Week-Spotify-Song-Suggester-2/datascience/master/SpotifyTrackFeatures.csv", error_bad_lines=False)
    tracks = tracks.drop_duplicates(['track_id'])

    # gets track audio features via track id and puts them into a df
    track_features = sp.audio_features(track_id)
    track_features = pd.DataFrame(track_features[0], index=[0])
    track_features = track_features.drop(columns=["id",
                                                  "uri",
                                                  "analysis_url",
                                                  "type",
                                                  "track_href",
                                                  "duration_ms",
                                                  "time_signature"])
    pred = knn_model.kneighbors(track_features)

    return_rec = {}
    arr = pred[1][0]
    for i in arr:
        return_rec[i] = {"track_name": tracks['track_name'].iloc[i],
                         "artist": tracks['artist_name'].iloc[i]}

    return_rec = list(return_rec.values())
    for i in range(10):
        print(f"Artist: {return_rec[i]['artist']}, Song: {return_rec[i]['track_name']}")

    return render_template("suggestion_results.html",
                           title=track_name,
                           artist=artist_name,
                           recommendations=return_rec
                           )
