from pytube import YouTube
import sys

SAVE_PATH = "/home/kira/Downloads/"

link = sys.argv[1]
print("downloading: ", link)


try:
	yt = YouTube(link)
except:
	print("Connection Error")



# download video as mp4 with highest quality
video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
video.download(SAVE_PATH)

print('download completed!')
