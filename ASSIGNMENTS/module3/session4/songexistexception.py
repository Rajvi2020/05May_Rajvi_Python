class SongAlreadyExistsError(Exception):
    pass
def add_song_to_playlist(song_name, playlist):
    try:
        if song_name in playlist:
            raise SongAlreadyExistsError("Song already exists in playlist!")
        else:
            print("Song added successfully!")
            playlist.append(song_name)

    except SongAlreadyExistsError as e:
        print(e)
playlist = ["Believer", "Faded"]
add_song_to_playlist("Perfect", playlist)
add_song_to_playlist("Believer", playlist)

