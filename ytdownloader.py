#imports
from pytube import *
yturl = input("Enter Yt Link: \n")
video=YouTube(yturl)
vidfile = video.streams.get_highest_resolution()
vidfile.download()
