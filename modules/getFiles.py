import os

#cwd = os.getcwd()


def getFiles(cwd):
    songs_list = []
    for folder, _, files in os.walk(cwd+"\\src"):
        for file in files:
            if os.path.splitext(file)[-1] == ".mp3":
                songs_list.append(folder + "\\" + file)
    return songs_list


if __name__ == "__main__":
    print("pass location of the folder to search in getFiles func")
