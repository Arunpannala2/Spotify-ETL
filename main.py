import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import requests
import json
import datetime
import sqlite3


DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
USER_ID = "apannala02"
TOKEN = "BQB9mj32ghCpGbLHCVhpJ9ITJoP9UHaQp3Op80ppT49_VC8Ej3V_NVPzXDBC2YHJpBIKxCEJGf21WmLgPnZ-2zcUqsFB3Dusgbv81_pjjjxB0XsVeddjoGoK1CjfoDsYlaP63FiTTjy0JvtUjSOORd4Lms7n51pQSUaeFkUNj9y3WaKc"

#Data Transformation/Validation
def data_validation(df: pd.DataFrame) -> bool: 
    if df.empty:
        print("No songs were downloaded. Complete execution")
        return False
    #Primary Key
    if pd.Series(df['played at']).is_unique:
        pass
    else:
        raise Exception("Primary Key Check Is Violated.Terminate Extraction")

    #Null Check
    if df.isnull().values.any():
        raise Exception("Null Values Found. Terminate Exception")

    #Check Timestamps are of Yesterday's date
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)

    timestamps = df["timestamp"].tolist()
    for timestamp in timestamps:
        if datetime.datetime.strptime(timestamp, "%Y-%m-%d") != yesterday:
            raise Exception("One of the songs does not come from last 24 hours")
    
    return True



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


    #Validate
    if data_validation(song_df):
        print("Data valid, Load Data")

    #Load Data
    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    conn = sqlite3.connect('my_played_tracks.sqlite')
    cursor = conn.cursor()

    sql_query = """
    CREATE TABLE IF NOT EXISTS my_played_tracks(
        song_name VARCHAR(250),
        artist_name VARCHAR(200),
        played_at VARCHAR(200),
        time_stamp VARCHAR(200),
        CONSTRAINT primary_key_constraint PRIMARY KEY(played_at)
        )
        
        """
    cursor.execute(sql_query)
    print("Database Loaded")

    try:
         song_df.to_sql("spotify_played_tracks", engine, index=False, if_exists='append')
    except:
        print("Data already exists in the database")
    
    conn.close()
    print("Close database")

    
        




