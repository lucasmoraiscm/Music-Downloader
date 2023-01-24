from tkinter import *
from controller import *

def btn_download():
    get_url = (ed.get())
    request_download = Music.request(get_url)
    lb_resp['text'] = request_download

janelaHome = Tk()
janelaHome.geometry('500x500+300+300')
janelaHome.title('Music Downloader')

lb = Label(janelaHome, text = 'Digite a URL da música:')
lb.place(x = 20,y = 20)

ed = Entry(janelaHome, bg = 'white')
ed.place(x = 150,y = 20)

lb_resp = Label(janelaHome, bg = 'white', width = 30, text = '')
lb_resp.place(x = 20, y = 50)

btn = Button(janelaHome, text = 'Baixar', width = 10, command = btn_download)
btn.place(x = 85, y = 80)

janelaHome.mainloop()
