import soundcloud

# client id from registerd app YOU HAVE TO GET YOUR OWN FROM SOUNDCLOUD
CLIENT_ID ="b137996e08ffa19401924bd787ba8470"
PLAYLIST_URL = 'https://soundcloud.com/admiralmoha/sets/arabic'

def createClient(client_id):
	# create client instance
	client = soundcloud.Client(client_id="b137996e08ffa19401924bd787ba8470")
	return client

def getPlaylist(client, playlist_url):
	# get playlist
	playlist = client.get('/resolve', url=playlist_url)
	return playlist

def getTracks(playlist):
	# get tracks which is a list of dictionaries each one containing track info
	tracks = playlist.tracks
	return tracks

def printTracksInfo(tracks):
	print "Playlist has %d tracks and they are: " % len(tracks)
	for track in tracks:
		print "Id: %s" % track['id'] 
		print "title: %s " % track['title']
		print "duration: %s " % track['duration']
		print "URI: %s " % track['uri']
		print "---------------------------------------------------"

printTracksInfo(getTracks(getPlaylist(createClient(CLIENT_ID), PLAYLIST_URL)))
