f = open("my_fav_songs.txt", "r")
i = 1
for song in f:
    print(i, "-", song)
    i = i + 1
f.close()