from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from youtube_search import YoutubeSearch

PLAYLISTS = [['Latest Love Songs','https://open.spotify.com/playlist/37i9dQZF1DWWWpLwNv0bd2?si=a828f9349d4449ad','37i9dQZF1DWWWpLwNv0bd2'],
['SidSriram','https://open.spotify.com/playlist/4EqzeF547YYJDOZshQFNzC?si=b9cc62d1c91a4650','4EqzeF547YYJDOZshQFNzC'],
['Programming & Coding Music','https://open.spotify.com/playlist/6vWEpKDjVitlEDrOmLjIAj', 'PL59eqqQABruNew5O0cRvomfbU6FI0RGyl'],
['Latest Songs','https://open.spotify.com/playlist/37i9dQZF1DWVo4cdnikh7Z?si=738810c70a394654', '37i9dQZF1DWVo4cdnikh7Z']
]
client_credentials_manager = SpotifyClientCredentials(client_id='e5d66c188ef64dd89afa4d13f9555411',
                client_secret='d070988d7bd5479a9e0818fa23839544')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


CONTAINER = []
for playlist in PLAYLISTS:
    Name,Link,playlistid = playlist
    playlistcard = []
    count = 0
    PlaylistLink = "http://www.youtube.com/watch_videos?video_ids="
    try:
        for i in (sp.playlist_tracks(Link)['items']):
            if count == 50:
                break
            try:
                song = i['track']['name'] + i['track']['artists'][0]['name']
                songdic = (YoutubeSearch(song, max_results=1).to_dict())[0]
                playlistcard.append([songdic['thumbnails'][0],songdic['title'],songdic['channel'],songdic['id']])
                PlaylistLink += songdic['id'] + ','
            except:
                continue
            count += 1

        from urllib.request import urlopen
        req = urlopen(PlaylistLink)
        PlaylistLink = req.geturl()
        PlaylistId = PlaylistLink[PlaylistLink.find('list')+5:]

        CONTAINER.append([Name,playlistcard,playlistid])
    except:
        pass

import json

json.dump(CONTAINER,open('card1.json', 'w'),indent = 6) 
