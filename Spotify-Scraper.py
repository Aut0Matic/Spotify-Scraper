import requests
import urllib
from requests.api import request

""" Spotify Request """

access_token ='BQCe22TjrxsNOd0f-Bf9S1TWwxn5GLck9etIaa6SyP2Yfaaq5OeFtjLHPeet7HfF_CI_ej0WlxxeV3Z7Czg8P6OYp0KwNKQ71FF-x_D-tUUgXA9LC0GRMS2m_NjfiP9JL2ecX4YM9aBsXP8'
# access_token = input("access token:")

# Setting the header and the request url
headers = {
    "Authorization": f"Bearer {access_token}"
}
endpoint = "https://api.spotify.com/v1/me/player/currently-playing"
request_url = f"{endpoint}"


# Making a request
spotify_request = requests.get(request_url, headers=headers)

# Converting to json
spotify_json_response = spotify_request.json()
print(spotify_json_response)

# Retrieving information
album_name = spotify_json_response['item']['album']['name']
album_id = spotify_json_response['item']['album']['id']
track_name = spotify_json_response['item']['name']
print(track_name)
print(album_name)
print(album_id)


album_art_url = spotify_json_response['item']['album']['images'][0]['url']
print(album_art_url)
urllib.request.urlretrieve(album_art_url, "image.jpg")

""" Musicbrainzngs Request """

import musicbrainzngs

mb_endpoint = "http://musicbrainz.org/ws/2/annotation"
request_url = f"{endpoint}?query=name:{album_name}"

musicbrainzngs_id_request = requests.get(request_url)

musicbrainzngs_json = musicbrainzngs_id_request.json()
print(musicbrainzngs_json)

musicbrainz_id = musicbrainzngs_json["annotations"]["entity"]



musicbrainzngs_request = musicbrainzngs.get_image_list(musicbrainz_id)
musicbrainzngs_json_request = musicbrainzngs_request.json()

print(musicbrainzngs_request['images']['image'])