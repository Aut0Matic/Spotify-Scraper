import spotipy
from spotipy.oauth2 import SpotifyOAuth
client_id='785059c78823447fb32cb094072cd452'
client_secret=''
redirect_uri='http://127.0.0.1:9090'
scope='user-read-playback-state'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))
    
track_query = sp.current_user_playing_track()
album = track_query['item']['album']['name']
track = track_query['item']['name']
artist = track_query['item']['artists'][0]['name']
print("Track: ",track,"\nAlbum: ",album,"\nArtist :",artist)

