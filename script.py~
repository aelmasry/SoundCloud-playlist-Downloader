import soundcloud, urllib
# client id from registerd app YOU HAVE TO GET YOUR OWN FROM SOUNDCLOUD
CLIENT_ID ="b137996e08ffa19401924bd787ba8470"
PLAYLIST_URL = 'https://soundcloud.com/classicalclassroom/sets/classical-classroom-1'

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

def downloadTrack(tracks):
	for track in tracks:
		if track['downloadable'] == True:
			track_title = str(track['title']) + '.mp3' 
			dl_url = str(track['uri'])  + '/download?client_id=' + CLIENT_ID
			urllib.urlretrieve(dl_url, track_title)
		# remove break to download the whole playlist
		else:
			print "No files to Download (probably not allowed)"
		break

def printTracksInfo(tracks):
	print "Playlist has %d tracks and they are: " % len(tracks)
	for track in tracks:
		print "Id: %s" % track['id'] 
		print "title: %s " % track['title']
		print "duration: %s " % track['duration']
		print "URI: %s " % track['uri']
		print "---------------------------------------------------"

# printTracksInfo(getTracks(getPlaylist(createClient(CLIENT_ID), PLAYLIST_URL)))

downloadTrack(getTracks(getPlaylist(createClient(CLIENT_ID), PLAYLIST_URL)))
