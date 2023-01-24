from model import *

class Music():
    @classmethod
    def request(cls, url):
        url_music = Downloader()
        request_download = url_music.download(url)
        return request_download