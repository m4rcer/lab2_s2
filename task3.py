import os

def readSongList(filename):
    songs = {}
    with open(filename) as f:
        for line in f:
            if line.strip():
                title = line.strip().split()[1]
                songs[title] = line.strip()
    return songs

def renameFiles(directory, songs):
    for filename in os.listdir(directory):
        for title in songs:
            if title in filename:
                newFilename = songs[title].replace(':', " ") + ".mp3"
                print(os.path.join(directory, newFilename))
                os.rename(os.path.join(directory, filename),
                          os.path.join(directory, newFilename))

songs = readSongList('task3.txt')
print(songs)
renameFiles('task3', songs)
