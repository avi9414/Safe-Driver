from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import requests
import geocoder
import json
import time
import threading
from cefpython3 import cefpython as cef
import Predictor as pothole_module
import distracteddriver as dd_module
import cv2
import Keys


def disdra():
    # dd_module.start()
    ii=0


def pothole():
    pothole_module.start()


def EVP():
    headers = {
    'Authorization': Keys.radarapi,
    }

    data = {
  'deviceId': 'test',
  'userId': '1',
  'latitude': '28.943498',
  'longitude': '77.369886',
  'accuracy': '10'
    }

    response = requests.post('https://api.radar.io/v1/track', headers=headers, data=data)
    response=response.json()
    rt=Tk()
    rt.withdraw()
    messagebox.showwarning("Warning","??? Emergency Vehicle on its way,make room ???")


class Mainscreen(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.ms()

    def ms(self):
        self.canvas= Canvas(root,height=800,width=1600)
        self.bgpic = ImageTk.PhotoImage(file='Images/mainbg.jpg')
        self.canvas.create_image(0,0, image=self.bgpic, anchor=NW)
        self.canvas.pack() 
        self.canvas.pack_propagate(False)
        self.musicpic=PhotoImage(file="Images/musicpic.png")
        self.musicpic=self.musicpic.subsample(4,4)
        self.redbutton = Button(self.canvas,command=self.music,height=200,width=400,activebackground='#8f246b',image=self.musicpic,bg="#b82e8a",compound=LEFT,relief=GROOVE,cursor="hand2") 
        self.redbutton.place(x=250,y=150)
        self.navpic=PhotoImage(file="navpic.png")
        self.navpic=self.navpic.subsample(3,3)
        self.weatherpic=PhotoImage(file="Images/weatherpic.png")
        self.weatherpic=self.weatherpic.subsample(3,3) 
        self.greenbutton = Button(self.canvas,command=self.navigate, height=200,width=400,activebackground='#40ff00',image=self.navpic,bg="#66ff33",compound=LEFT,relief=GROOVE,cursor="hand2") 
        self.greenbutton.place(x=700,y=150) 
        self.carpic=PhotoImage(file="Images/carpic.png")
        self.carpic=self.carpic.subsample(2,2) 
        self.blebutton = Button(self.canvas,command=lambda : self.weather(), height=200,width=400,activebackground='#00ace6',image=self.weatherpic,bg="#33ccff",compound=LEFT,relief=GROOVE,cursor="hand2")
        self.blebutton.place(x=250,y=400) 
        self.bluebutton = Button(self.canvas,command=lambda : self.car(), height=200,width=400,activebackground='#660022',image=self.carpic,bg="#990033",compound=LEFT,relief=GROOVE,cursor="hand2")
        self.bluebutton.place(x=700,y=400)

    def music(self):
        self.music_canvas=Canvas(self.canvas,height=800,width=1600,bg="grey")
        self.bbbpic = ImageTk.PhotoImage(file='Images/22.png')
        self.music_canvas.create_image(0,0, image=self.bbbpic, anchor=NW)
        self.music_canvas.pack() 
        self.music_canvas.pack_propagate(False)
        self.exit_button=Button(self.music_canvas,bg="grey",text="BACK",cursor="hand2",fg="white",command=lambda : self.back(self.music_canvas)).place(x=20,y=20)

    def car(self):
        self.car_canvas= Canvas(self.canvas,height=800,width=1600)
        self.bpic = ImageTk.PhotoImage(file='Images/incar.jpg')
        self.car_canvas.create_image(0,0, image=self.bpic, anchor=NW)
        self.car_canvas.pack() 
        self.car_canvas.pack_propagate(False)
        self.exiit_button=Button(self.car_canvas,command=lambda : self.back(self.car_canvas),height=800,width=560,bg="grey",text="BACK",cursor="hand2",fg="white").place(x=1040,y=0)


    def navigate(self):
        self.url="https://www.google.com/maps/dir///@2.2798485,70.4050408,3z/data=!4m2!4m1!3e0"
        cef.Initialize()
        cef.CreateBrowserSync(url=self.url,window_title="Navigate")
        cef.MessageLoop()


    def weather(self):

        self.wth_canvas= Canvas(self.canvas,height=800,width=1600)
        self.bpicc = ImageTk.PhotoImage(file='pngbarn.png')
        self.wth_canvas.create_image(0,0, image=self.bpicc, anchor=NW)
        self.wth_canvas.pack() 
        self.wth_canvas.pack_propagate(False)
        g = geocoder.ip('me')
        answer=g.latlng
        lat=str(answer[0])
        lon=str(answer[1])
        url="http://api.openweathermap.org/data/2.5/forecast?lat="+lat+"&lon="+lon+"&appid="+Keys.open_weatherapi
        rep=requests.get(url)
        rep=rep.json()
        temprature=str(int(rep['list'][0]['main']['temp'])-273)
        weath=str(rep['list'][0]['weather'][0]['main'])
        city=str(rep['city']['name'])
        tmplab=Label(self.wth_canvas,text=temprature,font=("Courier", 100)).place(x=900,y=150)
        wtlab=Label(self.wth_canvas,text=weath,font=("Courier", 75)).place(x=900,y=300)
        ctlab=Label(self.wth_canvas,text=city,font=("Courier", 50)).place(x=900,y=400)
        self.exiitt_button=Button(self.wth_canvas,command=lambda : self.back(self.wth_canvas),bg="grey",text="BACK",cursor="hand2",fg="white").place(x=20,y=20)
        
    def back(self,dcan=Canvas):
        dcan.destroy()



thread1 = threading.Thread(target=disdra)
thread1.start()
thread2 = threading.Thread(target=pothole)
thread2.start()
thread3= threading.Thread(target=EVP)
thread3.start()
root=Tk()
root.geometry("1600x800+0+0")
root.title("Safe Driver")
app=Mainscreen(master=root)
app.mainloop()


