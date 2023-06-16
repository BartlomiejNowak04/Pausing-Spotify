import spotipy
import variables


Client_ID = variables.Client_ID
Client_Secret = variables.Client_Secret
uri = variables.uri


scope = 'user-modify-playback-state'

oauth_object = spotipy.SpotifyOAuth(client_id=Client_ID,

                                    client_secret=Client_Secret, redirect_uri=uri, scope=scope)
token_dict = oauth_object.get_access_token()
print(token_dict)


def pause():
    try:
        sp = spotipy.Spotify(oauth_manager=oauth_object)
        pause_spotipy = sp.pause_playback()
    except spotipy.SpotifyException:
        pass


