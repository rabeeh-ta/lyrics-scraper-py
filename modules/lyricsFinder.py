import bs4
import requests
import re


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

    song_link = f"https://www.azlyrics.com/lyrics/{artistName}/{songName}.html"

    getLyrics(song_link)
