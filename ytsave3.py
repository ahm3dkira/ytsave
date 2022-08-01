from pytube import YouTube
import sys

SAVE_PATH = "/home/kira/Downloads/"

link = sys.argv[1]
print("downloading: ", link)


try:
	yt = YouTube(link)
except:
	print("Connection Error")



# download video as mp3 with highest quality
audio = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
audio.download(SAVE_PATH)

print('download completed!')
