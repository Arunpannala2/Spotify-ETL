import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import sqlite3

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
 

    




