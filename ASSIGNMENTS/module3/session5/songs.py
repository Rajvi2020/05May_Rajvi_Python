class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

song1 = Song("Shape of You", "Ed Sheeran", 233)
song2 = Song("Blinding Lights", "The Weeknd", 200)

print("Song 1:")
print("Title:", song1.title)
print("Artist:", song1.artist)
print("Duration:", song1.duration, "seconds")

print("\nSong 2:")
print("Title:", song2.title)
print("Artist:", song2.artist)
print("Duration:", song2.duration, "seconds")