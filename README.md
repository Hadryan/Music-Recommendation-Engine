# Spotify Song Recommendation Engine 

## App :headphones: 
[https://bw-spotify.herokuapp.com/](https://bw-spotify.herokuapp.com/)

[https://bw-spotify-song-suggester-2-web-ui.netlify.app/](https://bw-spotify-song-suggester-2-web-ui.netlify.app/)

## Workflow
![Alt text](https://raw.githubusercontent.com/Build-Week-Spotify-Song-Suggester-2/datascience/master/DS%20Flowchart.jpg)

## Project Information 
We were assigned to deploy a personalized song recommendation app by creating an algorithm to recommend songs based on a user's inputted song. We created a new dataset of 120k unique song tracks to train our model with by combining a dataset of tracks from [Kaggle](https://www.kaggle.com/tomigelo/spotify-audio-features) and updating it with additional tracks from the [Spotify API]( https://api.spotify.com) directly. 

Our app takes the provided user input, and generates a GET request that matches the track to its unique ID in the Spotify API, and then applies our model to return a json list of top 10 most similar songs back to the user. Song similarity was determined by model analysis of each track's audio features, including danceability, acousticness, instrumentalness vs speechiness, loudness, energy, and valence. We created both a k-nearest neighbors model and a neural network. However, we chose to only deploy the KNN model to our app as it was more lightweight and accurate given the time constraint of one fewer workday. 

## API Endpoints

['Spotify API - Authorization Token'](https://accounts.spotify.com/api/token)

Sends POST request to Spotify API using client credentials to generate an authorization token.

['Spotify API - Search'](https://api.spotify.com/v1/search)

Generates GET request using the authorization token acquired via client credentials, the user-inputted song title, and user-inputted artist. This GET request returns a JSON object which is indexed to extract the song's unique song ID.

## Visual Representation of Track Audio Data :notes:

![Radar chart visualization for Aerodynamic by Daft Punk](https://raw.githubusercontent.com/Build-Week-Spotify-Song-Suggester-2/datascience/f7adc65e3366a0df1fe83e732baea3419d9d134b/daft_punk_audio_features_radar_chart.jpg)

## Libraries Used
In this project we used libraries including:

['Pandas'](https://pandas.pydata.org/docs/)

['Numpy'](https://docs.scipy.org/doc/)

['Flask'](https://flask.palletsprojects.com/en/1.1.x/)

['Sklearn'](https://scikit-learn.org/stable/)

['Spotipy'](https://spotipy.readthedocs.io/en/2.12.0/)

['Plotly'](https://github.com/plotly/plotly.py)

['Joblib'](https://joblib.readthedocs.io/en/latest/)

['Tensorflow'](https://www.tensorflow.org/overview/)

['Dotenv'](https://pypi.org/project/python-dotenv/)

['Os'](https://docs.python.org/3/library/os.html)


## Team Github Links :musical_note:
[Front-End](https://github.com/Build-Week-Spotify-Song-Suggester-2/front-end)

[Web-UI](https://github.com/Build-Week-Spotify-Song-Suggester-2/Web-UI-Marketing)

[Back-End](https://github.com/Build-Week-Spotify-Song-Suggester-2/back-end)
