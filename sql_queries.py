# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES
# songplays TABLE
songplay_table_create = """
CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY, start_time int NOT NULL, user_id int NOT NULL, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar)
"""

# users TABLE
user_table_create = """CREATE TABLE IF NOT EXISTS users (user_id int PRIMARY KEY, first_name varchar, last_name varchar, gender varchar, level varchar)"""

# songs TABLE
song_table_create = """
CREATE TABLE IF NOT EXISTS songs (song_id varchar, title varchar, artist_id varchar, year INT CHECK (year >= 0), duration float, PRIMARY KEY(song_id))
"""

# artists TABLE
artist_table_create = """CREATE TABLE IF NOT EXISTS artists (artist_id varchar PRIMARY KEY, artist_name varchar, artist_location varchar, artist_latitude float, artist_longitude float)"""

# time TABLE
time_table_create = """CREATE TABLE IF NOT EXISTS time (start_time varchar PRIMARY KEY, hour int, day int, week int, month int, year int, weekday int)"""


# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (user_id)
DO UPDATE SET level=EXCLUDED.level
""")


#songs dimension table
song_table_insert = """
INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (song_id)
DO NOTHING
"""


artist_table_insert = """
INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude, artist_longitude)
VALUES(%s, %s, %s, %s, %s)
"""


time_table_insert = """
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES(%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time)
DO NOTHING
"""

# FIND SONGS
# Query to find the song ID and artist ID based on the title, artist name, and duration of a song.
song_select = """
SELECT s.song_id, a.artist_id
FROM songs AS s
JOIN artists AS a
ON s.artist_id = a.artist_id
WHERE s.title = %s
AND a.artist_name = %s
AND s.duration = %s
"""

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]