import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import requests
import json
import datetime
import sqlite3


DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
USER_ID = "apannala02"
TOKEN = "BQBluVnhA8DXERkPtt6UqcoO-gRYQW8DzwqNO94ZmWcqpz5iIeU0H7TBfUD-qhXpm0qedNFo07dKz3t5iLpsb3z3vi3ZGT6hqiAZmlcPi2-CxXnXD9culM7974cu-JnShZNhwg3fkqDzPmX0Jp4A3LChIKX7dUEQNwgT0i1kD8Ngjp8O"

#Data Transformation/Validation
def data_validation(df: pd.DataFrame) -> bool: 
    if df.empty:
        print("No songs were downloaded. Complete execution")
        return False


if __name__ == "__main__":

#Extract
#API creds for data request
    headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {token}".format(token=TOKEN)
    }
    
    #Convert time to Unix timestamp in miliseconds
    today = datetime.datetime.now()  
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    #Request data from Spotify API
    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers = headers)

    data = r.json()

    #Specify fields
    song_names = []
    artist_name = []
    played_at = []
    time_stamp = []
    
    #Extract the most important elements
    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_name.append(song["track"]["album"]["artists"][0]["name"])
        played_at.append(song["played_at"])
        time_stamp.append(song["played_at"][0:10])
    
    #Put data in tabular form
    #Prepare dictionary for pandas dataframe
    spotify_songs_dict = {
    "song_name" : song_names,
    "artist_name" : artist_name,
    "played_at" : played_at,
    "time_stamp" : time_stamp
    }

    song_df = pd.DataFrame(spotify_songs_dict, columns = ["song_names", "artist_name", "played_at", "time_stamp"])

    print(song_df)




