import pandas as pd
import json

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
    
