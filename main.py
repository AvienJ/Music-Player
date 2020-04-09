# NAME: Music Player
# FILE: main.py(DIR: .\)

# DESCRIPTION: "A music player that using playsound and eyed3
# CREDITS: Avien Jones(GITHUB: AvienJ)
# MISC\NOTES:
# ____________________
from playsound import playsound
from eyed3 import id3
import os

input_filename = input("Enter to file and path to your music file: ")

mus_info = id3.Tag()
mus_info.parse(input_filename)

os.system("cls")

music_title = ""
if mus_info.title == None:
    music_title = "Unknown Title"
else:
    music_title = mus_info.title

print("Now Playing: " + ('"' + input_filename.upper() + '":'))
print("\n")
print("\t TITLE: " + str(music_title))
print("\t ARTIST: " + str(mus_info.artist))
print("\t ALBUM: " + str(mus_info.album))


playsound(input_filename)

