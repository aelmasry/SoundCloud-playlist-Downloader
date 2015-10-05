import soundcloud, wget
# client id from registerd app YOU HAVE TO GET YOUR OWN FROM SOUNDCLOUD
CLIENT_ID ="b137996e08ffa19401924bd787ba8470"
# add playlist url
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


def downloadTrack(tracks):
	counter = 0
	print "Playlist has %d tracks" % len(tracks)
	for track in tracks:
		if track['downloadable']:
			track_title = str(track['title']) + '.mp3' 
			dl_url = str(track['uri'])  + '/download?client_id=' + CLIENT_ID
			print "Currently Downloading " + track_title
			wget.download(dl_url)
			print "\nsuccess"
			counter += 1
		else:
			print "No files to Download (probably not allowed)"
		# remove break to download the whole playlist
		break
	print "\n\n Successfully downloaded %d tracks" % counter
		

def printTracksInfo(tracks):
	print "Playlist has %d tracks and they are: \n\n" % len(tracks)
	for track in tracks:
		print "Id: %s" % track['id'] 
		print "title: %s " % track['title']
		print "duration: %s " % track['duration']
		print "URI: %s " % track['uri']
		print "---------------------------------------------------"

# print info about tracks in the list
printTracksInfo(getTracks(getPlaylist(createClient(CLIENT_ID), PLAYLIST_URL)))

# download tracks
downloadTrack(getTracks(getPlaylist(createClient(CLIENT_ID), PLAYLIST_URL)))
