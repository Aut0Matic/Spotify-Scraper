import requests
import urllib

from requests.api import request

access_token ='BQDmPBjfCIfmz1TrRJvYpULzRz6pq857BxbFosMfyIpAUJl4LHzCtDG3FOID1lZGkIxtq-LfdLGHg7hKxpprazoSh_bEEmpoZdQQkp4B6UaGKNSNsSYoqyJ2nx2Gc33y_96gx0jQZfNWK5I'
#access_token = input("access token:")

#Setting the header and the request url
headers = {
    "Authorization": f"Bearer {access_token}"
}
endpoint = "https://api.spotify.com/v1/me/player/currently-playing"
request_url = f"{endpoint}"


# Making a request
r = requests.get(request_url, headers=headers)

json_response = r.json()
print(json_response)

album_name = json_response['item']['album']['name']
album_id = json_response['item']['album']['id']
track_name = json_response['item']['name']
print(track_name)
print(album_name)
print(album_id)

album_art_url = json_response['item']['album']['images'][0]['url']
print(album_art_url)
urllib.request.urlretrieve(album_art_url, "image.jpg")