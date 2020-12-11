import eyed3
import os


for folders, sub_folders, files in os.walk("C:\\Users\\user\\Desktop\\music-automate\\Katy Perry - Greatest Songs"):
    for indx, file in enumerate(files):
        if os.path.splitext(file)[1] == ".mp3":
            audiofile = eyed3.load(folders + "\\"+file)
            audiofile.tag.album = "Katty Perry Hits"
            print(f'\n done {indx+1}')
            audiofile.tag.save()
