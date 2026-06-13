f = open("my_fav_songs.txt", "r")
songs = f.readlines()
print("Total songs:", len(songs))
f.close()