def get_song_duration(song):
    songs = {
        "Believer": "3:24",
        "Faded": "3:32",
        "Perfect": "4:23"
    }

    try:
        print(songs[song])
    except:
        print("Song not found on Spotify!")

get_song_duration("Believer")
get_song_duration("ABC")