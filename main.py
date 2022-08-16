import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import sqlite3

DATABASE_LOCATION = "sqlite:///player_tracks.sqlite"
USER_ID = "payday_11"
TOKEN = "BQB83P_oAUkb4FvG00EgrknsKidbmb141sD8VrVFkLkUHIpPskHE64hGOsYIzxt45Aqzj_B"

