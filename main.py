import os
import eyed3
import re
import requests
import bs4
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
    class_name = Song(af.tag.title.split("feat")[
                      0], af.tag.artist.split(",")[0], item)

    # check if the song has lyrics
    if len(af.tag.lyrics) == 0:
        class_name.lyricsFound = False
    else:
        class_name.lyricsFound = True

    song_class_list.append(class_name)  # store all song class in array
    af.tag.save()


def getLyrics(link):
    lyrics = ''
    res = requests.get(link)
    soup = bs4.BeautifulSoup(res.text, "lxml")

    for lyrics_divs in soup.find_all("div", {"class": None}):
        if len(lyrics_divs.text) == 0:
            pass
        else:
            # print(goods.text)
            lyrics = lyrics + lyrics_divs.text
    print("---------------------------------------------------------------")
    print(lyrics)


def getLyricsLink(artistName, songName):

    # some regex BS no idea ;)
    artistName = re.sub('[^0-9a-zA-Z]+', '', artistName).lower()
    songName = re.sub('[^0-9a-zA-Z]+', '', songName).lower()

    linkTemp = f"https://www.azlyrics.com/lyrics/{artistName}/{songName}.html"

    getLyrics(linkTemp)


for song in song_class_list:
    if song.lyricsFound == False:
        getLyricsLink(song.artist, song.title)
