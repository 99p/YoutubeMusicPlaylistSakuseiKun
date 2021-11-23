import sys
from ytmusicapi import YTMusic
ytmusic = YTMusic('headers_auth.json')

if not len(sys.argv) > 2:
    print("\n",'usage: sakuseiKun "Playlist-title" "Playlist-description"',"\n")
    exit()

#--------------------
#playlist_name = "Super dorian"
playlist_name = sys.argv[1]
#playlist_description = "dorian mode musics"
playlist_description = sys.argv[2]
music_list = "list.txt"
#--------------------

playlist_id = ytmusic.create_playlist(playlist_name, playlist_description)

with open(music_list) as f:
    for line in f:
        try:
            search_result = ytmusic.search(line)
            ytmusic.add_playlist_items(playlist_id, [search_result[0]['videoId']])
        except:
            continue
