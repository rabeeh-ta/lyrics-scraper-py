import bs4


class Song:
    def __init__(self, title, artist, location, lyricsFound=False):
        self.title = title
        self.artist = artist
        self.location = location
        self.lyricsFound = lyricsFound
