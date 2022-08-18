# Spotify-ETL

In this pipeline, I have built an ETL(Extract, Transform, Load), pipeline which requests data from the Spotify API about what songs I have listened to in the last 24 hours as I am interested in extracting my listening history.
I then loaded the extracted data into a SQLite database. The pipeline has been schelued to run daily using Apache Airflow and I did this by creating DAG's to schedule the data pipeline.

Token from https://developer.spotify.com/console/get-recently-played/
