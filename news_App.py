import io
import webbrowser
from tkinter import *
import requests
from urllib.request import urlopen
from PIL import ImageTk,Image

class Newsapp:
    def __init__(self):
        self.data = requests.get(
            "https://newsapi.org/v2/top-headlines?country=in&apiKey=a3227eaaff01481bad5aaa4904e923bc").json()

        self.get_GUI()

        self.load_News(0)

    def get_GUI(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0, 0)
        self.root.configure(background='white')
        self.root.title("Welcome! Mini News Mart")

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def open_link(self, url):
        webbrowser.open(url)

    def load_News(self, index):
        self.clear()
        try:
            img_url =self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im)

        except:
            img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)

        label = Label(self.root,image  = photo)
        label.pack()





        heading = Label(self.root, text=self.data['articles'][index]['title'], bg='red', fg='white', wraplength=350,
                        justify='center')
        heading.pack(pady=(10, 20))
        heading.config(font=('verdana', 15))

        dets = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white', wraplength=350,
                     justify='center')
        dets.pack(pady=(5, 20))
        dets.config(font=('verdana', 12))

        frame = Frame(self.root,bg = 'black')
        frame.pack(expand=TRUE,fill=BOTH)

        if index!=0:
            prev = Button(frame,text="Prev.",width=16,height=3,command = lambda : self.load_News(index-1))
            prev.pack(side = LEFT)

        read = Button(frame, text='Read More', width=16, height=3,
                      command=lambda: self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)


        if index != len(self.data['articles']) - 1:
            next = Button(frame, text="Next", width=16, height=3,command = lambda : self.load_News(index+1))
            next.pack(side=LEFT)

        self.root.mainloop()




obj = Newsapp()
