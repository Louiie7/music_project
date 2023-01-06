import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
import numpy as np




scope = "user-library-read"
"%"
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="3f176acfe7fd45e29625b17cedd3bfc9",client_secret="767c7c6b05a847848e8e2482af957d77"))

def getUniqueGenreList(genre_list):
    unique_genres = list(set(genre_list))
    return unique_genres

def getTrackInfo(artist, track):

    query = "artist:{artist} track:{track}".format(artist = artist, track = track)
    s = sp.search(q = query, type = "track")
    items = s['tracks']['items']

    if len(items) > 0:
        track = s['tracks']['items'][0]
        #release_date = track["release_date"]
        artist = sp.artist(track["artists"][0]["external_urls"]["spotify"])
        #album = sp.album(track["album"]["external_urls"]["spotify"])
        genres = artist["genres"]
        return genres
    else:
        return ["Result not found"]
    
def getGenre(df):
    res = []
    df_new = df
    artist_idx = df.columns.get_loc("Main_Artist")
    track_idx = df.columns.get_loc("Track_Title")
    genre_list = pd.DataFrame()
    i = 0
    for row in df.to_numpy():
        try:
            while(True):
                try:
                    print(row[0])
                    genres = getTrackInfo(row[artist_idx], row[track_idx])
                except:
                    print("Timed out")
                    time.sleep(5)
                    continue
                break
        except KeyboardInterrupt:
            df_new['genres'] = genre_list
            df_new.to_csv("data/data_with_genres.csv")


        if genres == "":
            print("Spotify registers no genres")
        #for genre in genres:
            #genre_list.append(genre)
        genre_list[i] = genres
        i = i+1
    df_new['genres'] = genre_list
    #df.to_excel("TesteretilLouieResultater.xlsx")
    #unique_genres = pd.DataFrame(getUniqueGenreList(genre_list))
    #unique_genres.to_csv("unique_genres.csv")
    return df_new




