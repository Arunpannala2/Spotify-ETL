import pandas as pd
import json
import datetime

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

