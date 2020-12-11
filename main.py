import os
import eyed3
import re
from modules.getFiles import getFiles
from modules.songClass import Song

cwd = os.getcwd()  # get file location

songs_list = getFiles(cwd)  # retruns a list with all songs location
song_class_list = []  # for stoing all the Song class


for indx, item in enumerate(songs_list):

    af = eyed3.load(item)  # loading the .mp3 to eyed3 object as af

    class_name = indx + 1
    # create class for every song with infos
    # split is for when song has someone FEAT: in it
    class_name = Song(af.tag.title, af.tag.artist.split(",")[0], item)

    # check if the song has lyrics
    if len(af.tag.lyrics) == 0:
        class_name.lyricsFound = False
    else:
        class_name.lyricsFound = True

    song_class_list.append(class_name)  # store all song class in array
    af.tag.save()


def getLyrics(artistName, songName):

    # some regex BS no idea ;)
    artistName = re.sub('[^0-9a-zA-Z]+', '', artistName).lower()
    songName = re.sub('[^0-9a-zA-Z]+', '', songName).lower()

    linkTemp = f"https://www.azlyrics.com/lyrics/{artistName}/{songName}.html"

    print(linkTemp)


for song in song_class_list:
    getLyrics(song.artist, song.title)
