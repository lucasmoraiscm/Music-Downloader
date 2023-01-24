import os
from pytube import YouTube

class Downloader():
    @classmethod
    def download(cls, url):
        yt = YouTube(url)
        music = yt.streams.filter(only_audio = True).first()
        download_file = music.download()
        base, ext = os.path.splitext(download_file)
        new_file = base + '.mp3'
        os.rename(download_file, new_file)
        return("Música baixada com sucesso!")
