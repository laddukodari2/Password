from pytube import YouTube

try:
    url = input("Enter YouTube URL: ")
    folder = input("Enter Download Folder: ")

    yt = YouTube(url)
    stream = yt.streams.get_highest
