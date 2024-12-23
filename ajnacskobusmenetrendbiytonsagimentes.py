from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from time import *
import locale
import turtle
from threading import Thread
from subprocess import call

window = Tk()
canvas = Canvas(window, height=1000, width=1500)
canvas.pack()
t = turtle.RawTurtle(canvas)
t.penup()
t.speed(0)
t.hideturtle()

def open_image(image_path):
    img = Image.open(image_path)
    img.thumbnail((canvas.winfo_width(), canvas.winfo_height()))
    img_tk = ImageTk.PhotoImage(img)
    canvas.create_image(-750, -500, anchor=tk.NW, image=img_tk)
    canvas.img = img_tk


    
current_image_index = 0

def update():
    locale.setlocale(locale.LC_TIME, 'sk_SK')
    time_string = strftime("%I:%M:%S %p", localtime())
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    day_string = strftime("%A")
    day_label.config(text=day_string)
    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)
    window.after(1000, update)

time_label = Label(window, font=("Italic", 50, "bold"))
time_label.place(x=0, y=900)
day_label = Label(window, font=("Italic", 30, "bold"))
day_label.place(x=0, y=850)
date_label = Label(window, font=("Italic", 30, "bold"))
date_label.place(x=0, y=800)
def centrumc(): 

    global brod, brdo
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
    brdo = Button(window,text='do Kolónia',font="Ariel 20 bold",command=centrum,bg="lightgreen",width=50,height=20)
    brdo.bind("<Enter>", lambda event: on_enter(event, brdo))
    brdo.bind("<Leave>", lambda event: on_leave(event, brdo))
    brdo.place(x=0,y=100)
    brod=Button(window,text="do Centrum",font="Ariel 20 bold",command=centrumr,bg="lightgreen",width=50,height=20)
    brod.bind("<Enter>", lambda event: on_enter(event, brod))
    brod.bind("<Leave>", lambda event: on_leave(event, brod))
    brod.place(x=750,y=100)
ysav=200
#black
def centrum():
    global ysav
    brod.destroy()
    brdo.destroy()
    canvas.create_rectangle(-250, 220, 1490, 255, fill="red", outline="black", tag="sav")
    canvas.create_text(150, 330, text="Hajnáčka Centrum -  Hajnáčka do Centrum  - 4 minúty\nHajnáčka do Centrum - Hajnáčka Doh.  - 8 minút\nHajnáčka Doh - Hajnáčka do Ostrá skala   - 15 minút\nHajnáčka do Ostrá skala - Hajnáčka do Doh.  - 16 minút\nHajnáčka do Doh. - Hajnáčka do Kolónia  - 20 minúty\nHajnáčka do Kolónia - Hajnáčka Kolónia  - 23 minút\nHajnáčka Kolónia - Hajnáčka Kolónia do Pose  - 27 minút", font="Italic 20 bold")
    s=1
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==1:
            image=open_image("HMD_Center.png")
    t1=Thread(target=img)
    t1.start()
    t.goto(20, -20)
    t.width(70)
    t.pendown()
    t.seth(180)
    for i in range(300):
        t.fd(1)
    for i in range(140):
        t.rt(0.5)
        t.fd(2)
    canvas.move("sav",0,32)
        #image = open_image(image_path)
    for i in range(120):
        t.rt(0.5)
        t.fd(2)
    s=2
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==2:
            image=open_image("HMD_Doh..png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(500,-180)
    t.pendown()
    t.seth(100)
    for i in range(150):
        t.fd(1)
    t.lt(65)
    for i in range(220):
        t.fd(1)
    canvas.move("sav",0,32)
    for i in range(60):
        t.fd(1)
    t.seth(180)
    for i in range(350):
        t.fd(1)
    t.seth(100)
    for i in range(200):
        t.fd(1)
    t.color("grey")
    canvas.move("sav",0,32)
    t.seth(280)
    t.color("black")
    for i in range(200):
        t.fd(1)
    t.seth(180)
    for i in range(200):
        t.fd(1)
    t.rt(30)
    
    for i in range(150):
        t.fd(1)
    canvas.move("sav",0,32)
    s=3
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==3:
            image=open_image("HMD_Kolonia.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(750,210)
    t.pendown()
    t.seth(180)
    t.fd(230)
    for i in range(370):
        t.fd(1)
    canvas.move("sav",0,32)
    for i in range(100):
        t.fd(1)
    t.lt(45)
    for i in range(200):
        t.fd(1)
    canvas.move("sav",0,32)
    t.seth(0)
    for i in range(440):
        t.fd(1)
    canvas.delete("sav")
    

def centrumr():
    global ysav
    brod.destroy()
    brdo.destroy()
    canvas.create_rectangle(-250, 220, 1490, 255, fill="red", outline="black", tag="sav")
    canvas.create_text(150, 330, text="Hajnáčka Kolónia do Pose -Hajnáčka Kolónia - 27 minút\nHajnáčka Kolónia - do Kolónia - 23 minút\nHajnáčka do Kolónia - Hajnáčka do Doh. - 20 minúty\nHajnáčka do Doh.  - do Ostrá skala - 16 minút\nHajnáčka do Ostrá skala - Hajnáčka Doh. - 15 minút\nHajnáčka Doh. - Hajnáčka do Centrum - 8 minúty\nHajnáčka do Centrum - Hajnáčka Centrum - 4 minúty", font="Italic 20 bold")
    s=1
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==1:
            image=open_image("HMD_Kolonia.png")
    t1=Thread(target=img)
    t1.start()
    t.goto(350, 70)
    t.width(70)
    t.pendown()
    t.seth(180)
    for i in range(400):
        t.fd(1)
    canvas.move("sav",0,32)
    t.seth(45)
    for i in range(200):
        t.fd(1)
    t.seth(0)
    for i in range(40):
        t.fd(1)
    canvas.move("sav",0,32)
    for i in range(180):
        t.fd(1)
    t.lt(25)
    for i in range(100):
        t.fd(1)
    canvas.move("sav",0,32)
    s=2
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==2:
            image=open_image("HMD_Doh..png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(-750,70)
    t.pendown()
    t.seth(15)
    t.fd(250)
    canvas.move("sav",0,32)
    t.seth(330)
    for i in range(200):
        t.fd(1)
    t.seth(15)
    for i in range(200):
        t.fd(1)
    t.seth(110)
    for i in range(170):
        t.fd(1)
    t.rt(180)
    t.color("grey")
    for i in range(170):
        t.fd(1)
    t.color("black")
    t.seth(350)
    for i in range(400):
        t.fd(1)
    canvas.move("sav",0,32)
    for i in range(170):
        t.fd(1)
    t.rt(50)
    for i in range(195):
        t.fd(1)
    s=3
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==3:
            image=open_image("HMD_Center.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(-600,400)
    t.pendown()
    t.seth(340)
    for i in range(150):
        t.fd(1)
    t.rt(110)
    for i in range(100):
        t.lt(0.5)
        t.fd(2)
    canvas.move("sav",0,32)
    t.lt(10)
    for i in range(160):
        t.lt(0.5)
        t.fd(2)
    t.seth(350)
    for i in range(300):
        t.fd(1)
    canvas.delete("sav")
    s=4
    
    
    
#blue
def gortvac():    
    global brod, brdo
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
    brdo = Button(window,text='do Gortva',font="Ariel 20 bold",command=gortva,bg="lightgreen",width=50,height=20)
    brdo.bind("<Enter>", lambda event: on_enter(event, brdo))
    brdo.bind("<Leave>", lambda event: on_leave(event, brdo))
    brdo.place(x=0,y=100)
    brod=Button(window,text="do Centrum",font="Ariel 20 bold",command=gortvar,bg="lightgreen",width=50,height=20)
    brod.bind("<Enter>", lambda event: on_enter(event, brod))
    brod.bind("<Leave>", lambda event: on_leave(event, brod))
    brod.place(x=750,y=100)
    
def gortva():
    global ysav
    brod.destroy()
    brdo.destroy()
    canvas.create_rectangle(-250, 225, 1490, 260, fill="red", outline="black", tag="sav")
    canvas.create_text(150, 280, text="Hajnáčka Centrum - Hajnáčka Sasbik  - 35 minút\nHajnáčka Sasbik - Hajnáčka Gortva – 10 minút\nHajnáčka Gortva - Hajnáčka Gortva do Zabodou - 5 minút",font="Italic 20 bold")
    t.goto(20, -20)
    t.width(70)
    t.pendown()
    t.seth(180)
    t.color("blue")
    s=1
    def img():
        while s==1:
            image=open_image("HMD_Center.png")
    t1=Thread(target=img)
    t1.start()
    for i in range(300):
        t.fd(1)
    for i in range(160):
        t.rt(0.5)
        t.fd(2)
    for i in range(100):
        t.rt(0.5)
        t.fd(2)
    s=2
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==2:
            image=open_image("HMD_Doh..png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(500,-180)
    t.pendown()
    t.seth(100)
    for i in range(150):
        t.fd(1)
    t.lt(65)
    for i in range(220):
        t.fd(1)
    for i in range(60):
        t.fd(1)
    t.seth(180)
    for i in range(550):
        t.fd(1)
    t.rt(30)
    
    for i in range(150):
        t.fd(1)
    s=3
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==3:
            image=open_image("HMD_Kolonia.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(750,210)
    t.pendown()
    t.seth(180)
    t.fd(230)
    for i in range(370):
        t.fd(1)
    for i in range(100):
        t.fd(1)
    t.lt(45)
    for i in range(200):
        t.fd(1)
    t.rt(20)
    for i in range(40):
        t.fd(1)
    t.seth(165)
    for i in range(520):
        t.fd(1)
    t.seth(90)
    for i in range(200):
        t.fd(1)
    canvas.move("sav",0,32)
    s=4
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==4:
            image=open_image("HMD_Gortva.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(-120,-180)
    t.pendown()
    t.seth(115)
    for i in range(230):
        t.fd(1)
    canvas.move("sav",0,32)
    for i in range(50):
        t.fd(1)
    t.rt(90)
    for i in range(360):
        t.fd(1)
    canvas.delete("sav")
    s=5
    
    
def gortvar():
    global ysav
    brod.destroy()
    brdo.destroy()
    canvas.create_rectangle(-250, 225, 1490, 260, fill="red", outline="black", tag="sav")
    canvas.create_text(150, 280, text="Hajnáčka Gortva do Zabodou - Hajnáčka Gortva - 5 minút\nHajnáčka Gortva - Hajnáčka Sasbik – 10 minút\nHajnáčka Sasbik - Hajnáčka Centrum  - 35 minút",font="Italic 20 bold")
    t.color("blue")
    s=1
    def img():
        while s==1:
            image=open_image("HMD_Gortva.png")
    t1=Thread(target=img)
    t1.start()
    t.goto(100, 230)
    t.width(70)
    t.color("blue")
    t.pendown()
    t.seth(208)
    for i in range(400):
        t.fd(1)
    t.seth(310)
    for i in range(20):
        t.fd(1)
    canvas.move("sav",0,32)
    for i in range(275):
        t.fd(1)
    canvas.move("sav",0,32)
    s=2
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==2:
            image=open_image("HMD_Kolonia.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(-700, 400)
    t.pendown()
    t.seth(315)
    for i in range(100):
        t.fd(1)
    t.seth(270)
    for i in range(120):
        t.fd(1)
    t.seth(340)
    for i in range(550):
        t.fd(1)
    t.seth(45)
    for i in range(250):
        t.fd(1)
    t.seth(0)
    for i in range(300):
        t.fd(1)
    t.seth(35)
    for i in range(100):
        t.fd(1)
    t.seth(350)
    for i in range(350):
        t.fd(1)
    s=3
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==3:
            image=open_image("HMD_Doh..png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(-750,70)
    t.pendown()
    t.seth(15)
    t.fd(250)
    t.seth(330)
    for i in range(200):
        t.fd(1)
    t.seth(15)
    for i in range(200):
        t.fd(1)
    t.seth(350)
    for i in range(400):
        t.fd(1)
    for i in range(170):
        t.fd(1)
    t.rt(50)
    for i in range(195):
        t.fd(1)
    s=4
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==4:
            image=open_image("HMD_Center.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(-600,400)
    t.pendown()
    t.seth(340)
    for i in range(150):
        t.fd(1)
    t.rt(110)
    for i in range(100):
        t.lt(0.5)
        t.fd(2)
    t.lt(10)
    for i in range(160):
        t.lt(0.5)
        t.fd(2)
    t.seth(350)
    for i in range(300):
        t.fd(1)
    canvas.delete("sav")
    
#green
def depoc():
    global brdo,brod
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
    brdo = Button(window,text='do Depo',font="Ariel 20 bold",command=depo,bg="lightgreen",width=50,height=20)
    brdo.bind("<Enter>", lambda event: on_enter(event, brdo))
    brdo.bind("<Leave>", lambda event: on_leave(event, brdo))
    brdo.place(x=0,y=100)
    brod=Button(window,text="do Centrum",font="Ariel 20 bold",command=depor,bg="lightgreen",width=50,height=20)
    brod.bind("<Enter>", lambda event: on_enter(event, brod))
    brod.bind("<Leave>", lambda event: on_leave(event, brod))
    brod.place(x=750,y=100)
def depo():
    global ysav
    brod.destroy()
    brdo.destroy()
    canvas.create_rectangle(-290, 220, 1490, 255, fill="red", outline="black", tag="sav")
    canvas.create_text(200, 300, text="Hajnáčka Centrum - Hajnáčka Sasbik\nHajnáčka Sasbik - Hajnáčka časť Železničná Stanica\nHajnáčka  Železničná časť Stanica - Hajnáčka Ipeľské Teheľňa - 35 minút\nHajnáčka Ipeľná Teheľňa - Hajnáčka Železničná Stanica - 35 minút\nHajnáčka  Železničná Stanica - Hajnáčka Depo - 43 minút",font="Italic 20 bold")
    s=1
    canvas.create_rectangle(-1000,-1000,1000,220,fill="white")
    def img():
        while s==1:
            image=open_image("HMD_Center.png")
    t1=Thread(target=img)
    t1.start()
    t.goto(20, -20)
    t.color("green")
    t.width(70)
    t.pendown()
    t.seth(180)
    for i in range(300):
        t.fd(1)
    for i in range(160):
        t.rt(0.5)
        t.fd(2)
    for i in range(100):
        t.rt(0.5)
        t.fd(2)
    s=2
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==2:
            image=open_image("HMD_Doh..png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(500,-180)
    t.pendown()
    t.seth(100)
    for i in range(150):
        t.fd(1)
    t.lt(65)
    for i in range(220):
        t.fd(1)
    for i in range(60):
        t.fd(1)
    t.seth(180)
    for i in range(550):
        t.fd(1)
    t.rt(30)
    
    for i in range(150):
        t.fd(1)
    s=3
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==3:
            image=open_image("HMD_Kolonia.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(750,210)
    t.pendown()
    t.seth(180)
    t.fd(230)
    for i in range(370):
        t.fd(1)
    for i in range(100):
        t.fd(1)
    t.lt(45)
    for i in range(200):
        t.fd(1)
    t.rt(20)
    for i in range(40):
        t.fd(1)
    t.seth(165)
    for i in range(520):
        t.fd(1)
    t.seth(90)
    for i in range(200):
        t.fd(1)
    canvas.move("sav",0,32)
    s=4
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==4:
            image=open_image("HMD_Zel.Stanica.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(400,450)
    t.pendown()
    t.seth(180)
    for i in range(50):
        t.fd(1)
    t.seth(235)
    for i in range(350):
        t.fd(1)
    canvas.move("sav",0,32)
    t.rt(180)
    t.color("grey")
    for i in range(320):
        t.fd(1)
    t.rt(90)
    t.color("green")
    for i in range(50):
        t.fd(1)
    t.rt(90)
    for i in range(270):
        t.fd(1)
    canvas.move("sav",0,32)
    for i in range(230):
        t.fd(1)
    t.rt(15)
    for i in range(50):
        t.fd(1)
    t.seth(110)
    for i in range(50):
        t.fd(1)
    canvas.move("sav",0,32)
    t.rt(180)
    for i in range(50):
        t.fd(1)
    t.seth(200)
    for i in range(300):
        t.fd(1)
    canvas.delete("sav")
    s=5
def depor():
    global ysav
    brod.destroy()
    brdo.destroy()
    canvas.create_rectangle(-290, 220, 1490, 255, fill="red", outline="black", tag="sav")
    canvas.create_text(200, 300, text="Hajnáčka Depo - Hajnáčka Železničná Stanica - 43 minút\nHajnáčka Železničná Stanica - Hajnáčka Ipeľná Teheľňa - 35 minút\nHajnáčka Ipeľná Teheľňa - Hajnáčka Časť Železničná Stanica - 35 minút\nHajnáčka Časť Železničná Stanica - Hajnáčka Sasbik - 40 minút\nHajnáčka Sasbik - Hajnáčka Centrum",font="Italic 20 bold")
    s=1
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==1:
            image=open_image("HMD_Zel.Stanica.png")
    t1=Thread(target=img)
    t1.start()
    t.goto(-200, -110)
    t.color("green")
    t.width(70)
    t.seth(17)
    t.pendown()
    for i in range(240):
        t.fd(1)
    t.seth(110)
    for i in range(50):
        t.fd(1)
    canvas.move("sav",0,32)
    t.rt(180)
    for i in range(50):
        t.fd(1)
    t.seth(20)
    for i in range(100):
        t.fd(1)
    t.seth(60)
    for i in range(470):
        t.fd(1)
    t.lt(90)
    for i in range(40):
        t.fd(1)
    t.lt(85)
    for i in range(250):
        t.fd(1)
    canvas.move("sav",0,32)
    for i in range(50):
        t.fd(1)
    canvas.move("sav",0,32)
    t.rt(180)
    t.color("grey")
    for i in range(300):
        t.fd(1)
    t.color("green")
    t.rt(35)
    for i in range(40):
        t.fd(1)
    canvas.move("sav",0,32)
    s=2
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==2:
            image=open_image("HMD_Kolonia.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(-700, 400)
    t.pendown()
    t.seth(315)
    for i in range(100):
        t.fd(1)
    t.seth(270)
    for i in range(120):
        t.fd(1)
    t.seth(340)
    for i in range(550):
        t.fd(1)
    t.seth(45)
    for i in range(250):
        t.fd(1)
    t.seth(0)
    for i in range(300):
        t.fd(1)
    t.seth(35)
    for i in range(100):
        t.fd(1)
    t.seth(350)
    for i in range(350):
        t.fd(1)
    s=3
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==3:
            image=open_image("HMD_Doh..png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(-750,70)
    t.pendown()
    t.seth(15)
    for i in range(250):
        t.fd(1)
    t.seth(330)
    for i in range(200):
        t.fd(1)
    t.seth(15)
    for i in range(200):
        t.fd(1)
    t.seth(350)
    for i in range(400):
        t.fd(1)
    for i in range(170):
        t.fd(1)
    t.rt(50)
    for i in range(195):
        t.fd(1)
    s=4
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==4:
            image=open_image("HMD_Center.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(-600,400)
    t.pendown()
    t.seth(340)
    for i in range(150):
        t.fd(1)
    t.rt(110)
    for i in range(100):
        t.lt(0.5)
        t.fd(2)
    t.lt(10)
    for i in range(160):
        t.lt(0.5)
        t.fd(2)
    t.seth(350)
    for i in range(300):
        t.fd(1)
    canvas.delete("sav")
    s=5
#red
def tenkesc():
    global brdo,brod
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
    brdo = Button(window,text='do Zabovy',font="Ariel 20 bold",command=tenkes,bg="lightgreen",width=50,height=20)
    brdo.bind("<Enter>", lambda event: on_enter(event, brdo))
    brdo.bind("<Leave>", lambda event: on_leave(event, brdo))
    brdo.place(x=0,y=100)
    brod=Button(window,text="do Centrum",font="Ariel 20 bold",command=tenkesr,bg="lightgreen",width=50,height=20)
    brod.bind("<Enter>", lambda event: on_enter(event, brod))
    brod.bind("<Leave>", lambda event: on_leave(event, brod))
    brod.place(x=750,y=100)
def tenkes():
    global ysav
    brod.destroy()
    brdo.destroy()
    canvas.create_rectangle(-290, 220, 1490, 255, fill="red", outline="black", tag="sav")
    canvas.create_text(200, 335, text="Hajnáčka Centrum - Hajnáčka Durenda - 10 minút\nHajnáčka Durenda - Hajnáčka Hrad - 15 minút\nHajnáčka Hrad - Hajnáčka Nové Cintorín - 20 minút\nHajnáčka Nové Cintorín - Hajnáčka Ragačou - 27 minút\nHajnáčka Ragačou  - Hajnáčka ulica Nového - 40 minút\nHajnáčka ulica Nového  - Hajnáčka ulica Selecov - 45 minút\nHajnáčka ulica Selecov - Hajnáčka ulica Zabovy - 50 minút",font="Italic 20 bold")
    s=1
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==1:
            image=open_image("HMD_Center.png")
    t1=Thread(target=img)
    t1.start()
    t.goto(20, -20)
    t.color("red")
    t.width(70)
    t.pendown()
    t.seth(180)
    for i in range(300):
        t.fd(1)
    for i in range(160):
        t.rt(0.5)
        t.fd(2)
    for i in range(100):
        t.rt(0.5)
        t.fd(2)
    s=2
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==2:
            image=open_image("HMD_Doh..png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(500,-180)
    t.pendown()
    t.seth(100)
    for i in range(150):
        t.fd(1)
    t.lt(65)
    for i in range(220):
        t.fd(1)
    for i in range(150):
        t.fd(1)
    t.seth(25)
    for i in range(350):
        t.fd(1)
    canvas.move("sav",0,32)
    t.fd(350)
    s=3
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==3:
            image=open_image("HMD_Upertown.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(-500,0)
    t.pendown()
    t.seth(15)
    for i in range(400):
        t.fd(1)
    t.seth(270)
    for i in range(50):
        t.fd(1)
    canvas.move("sav",0,32)
    for i in range(50):
        t.bk(1)
    t.seth(35)
    for i in range(60):
        t.fd(1)
    t.lt(20)
    for i in range(150):
        t.fd(1)
    canvas.move("sav",0,32)
    s=4
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==4:
            image=open_image("HMD_Ragacou.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(150,-180)
    t.pendown()
    t.seth(100)
    for i in range(200):
        t.fd(1)
    canvas.move("sav",0,32)
    t.color("grey")
    for i in range(200):
        t.bk(1)
    t.color("red")
    s=5
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==5:
            image=open_image("HMD_Upertown.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(-30,230)
    t.pendown()
    t.seth(270)
    for i in range(80):
        t.fd(1)
    t.seth(337)
    for i in range(150):
        t.fd(1)
    canvas.move("sav",0,32)
    for i in range(580):
        t.fd(1)
    t.lt(20)
    for i in range(100):
        t.fd(1)
    s=6
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==6:
            image=open_image("HMD_Selec_Vilage.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(-180,-170)
    t.pendown()
    t.seth(70)
    canvas.move("sav",0,32)
    for i in range(550):
        t.fd(1)
    canvas.delete("sav")
    s=7

    
    
        #image = open_image(image_path)
def tenkesr():
    global ysav
    brod.destroy()
    brdo.destroy()
    canvas.create_rectangle(-290, 220, 1490, 255, fill="red", outline="black", tag="sav")
    canvas.create_text(200, 335, text="Hajnáčka ulica Zabovy - Hajnáčka ulica Selecov - 50 minút\nHajnáčka ulica Selecov - Hajnáčka ulica Nového - 45 minút\nHajnáčka ulica Nového - Hajnáčka Nové Cintorín - 27 minút\nHajnáčka Nové Cintorín - Hajnáčka Ragačou - 40 minút\nHajnáčka Ragačou - Hajnáčka Hrad - 20 minút  \nHajnáčka Hrad - Hajnáčka Durenda - 15 minút\nHajnáčka Durenda - Hajnáčka Centrum - 10 minút",font="Italic 20 bold")
    t.goto(30, 300)
    t.width(70)
    t.color("red")
    t.pendown()
    s=1
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==1:
            image=open_image("HMD_Selec_Vilage.png")
    t1=Thread(target=img)
    t1.start()
    t.seth(245)
    for i in range(500):
        t.fd(1)
    canvas.move("sav",0,32)
    s=2
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==2:
            image=open_image("HMD_Upertown.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(750,-100)
    t.pendown()
    t.seth(170)
    for i in range(600):
        t.fd(1)
    canvas.move("sav",0,32)
    t.rt(25)
    for i in range(250):
        t.fd(1)
    t.rt(80)
    for i in range(200):
        t.fd(1)
    canvas.move("sav",0,32)
    s=3
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==3:
            image=open_image("HMD_Ragacou.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(150,-180)
    t.pendown()
    t.seth(100)
    for i in range(200):
        t.fd(1)
    canvas.move("sav",0,32)
    t.color("grey")
    for i in range(200):
        t.bk(1)
    t.color("red")
    s=4
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==4:
            image=open_image("HMD_Upertown.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(-30,230)
    t.pendown()
    t.seth(250)
    for i in range(250):
        t.fd(1)
    canvas.move("sav",0,32)
    for i in range(100):
        t.bk(1)
    t.seth(195)
    for i in range(430):
        t.fd(1)
    canvas.move("sav",0,32)
    s=5
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==5:
            image=open_image("HMD_Doh..png")
    t1=Thread(target=img)
    t1.start()
    t.goto(750, 300)
    t.width(70)
    t.pendown()
    t.width(70)
    t.seth(200)
    t.fd(315)
    for i in range(315):
        t.fd(1)
    t.seth(330)
    for i in range(300):
        t.fd(1)
    t.seth(300)
    for i in range(130):
        t.fd(1)
    s=6
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==6:
            image=open_image("HMD_Center.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(-600,400)
    t.pendown()
    t.seth(340)
    for i in range(150):
        t.fd(1)
    t.rt(110)
    for i in range(100):
        t.lt(0.5)
        t.fd(2)
    t.lt(10)
    for i in range(160):
        t.lt(0.5)
        t.fd(2)
    t.seth(350)
    for i in range(300):
        t.fd(1)
    canvas.delete("sav")
    s=7
    
#yellow
def selecovc():
    global brdo,brod
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
    brdo = Button(window,text='do Ragacou',font="Ariel 20 bold",command=selecov,bg="lightgreen",width=50,height=20)
    brdo.bind("<Enter>", lambda event: on_enter(event, brdo))
    brdo.bind("<Leave>", lambda event: on_leave(event, brdo))
    brdo.place(x=0,y=100)
    brod=Button(window,text="do Centrum",font="Ariel 20 bold",command=selecovr,bg="lightgreen",width=50,height=20)
    brod.bind("<Enter>", lambda event: on_enter(event, brod))
    brod.bind("<Leave>", lambda event: on_leave(event, brod))
    brod.place(x=750,y=100)
def selecov():
    global ysav
    brod.destroy()
    brdo.destroy()
    canvas.create_rectangle(-290, 220, 1490, 255, fill="red", outline="black", tag="sav")
    canvas.create_text(210, 300, text="Hajnáčka Centrum - Hajnáčka Lekáreň - 2  minúty\nHajnáčka Lekáreň - Hajnáčka Pekáreň  - 5 minút\nHajnáčka Pekáreň - Hajnáčka ulica Na Hradu - 10 minút\nHajnáčka ulica do Hradu - Hajnáčka Nové Cintorín - 15 minút\nHajnáčka Nové Cintorín - Hajnáčka Ragácou - 22 minút",font="Italic 20 bold")
    s=1
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==1:
            image=open_image("HMD_Center.png")
    t1=Thread(target=img)
    t1.start()
    t.goto(40, -20)
    t.color("yellow")
    t.width(70)
    t.pendown()
    t.seth(30)
    for i in range(180):
        t.fd(1)
        canvas.after(90)
    t.seth(65)
    for i in range(20):
        t.fd(1)
        canvas.after(90)
    canvas.move("sav",0,32)
    for i in range(180):
        t.fd(1)
        canvas.after(90)
    canvas.move("sav",0,32)
    for i in range(40):
        t.fd(1)
        canvas.after(90)
    t.seth(90)
    for i in range(120):
        t.fd(1)
        canvas.after(90)
    t.seth(110)
    for i in range(100):
        t.fd(1)
        canvas.after(90)
    s=2
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==2:
            image=open_image("HMD_Upertown.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(-50, -180)
    t.pendown()
    t.width(70)
    t.pendown()
    t.seth(90)
    canvas.move("sav",0,32)
    for i in range(150):
        t.fd(1)
        canvas.after(90)
    t.seth(0)
    for i in range(50):
        t.fd(1)
        canvas.after(90)
    t.seth(90)
    for i in range(150):
        t.fd(1)
        canvas.after(90)
    t.seth(160)
    for i in range(50):
        t.fd(1)  
        canvas.after(90)  
    t.seth(75)
    for i in range(150):
        t.fd(1)
        canvas.after(90)
    canvas.move("sav",0,32)
    s=3
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==3:
            image=open_image("HMD_NC.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(-500,-180)
    t.pendown()
    t.seth(37)
    t.fd(150)
    for i in range(350):
        t.fd(1)
        canvas.after(90)
    t.seth(120)
    for i in range(100):
        t.fd(1)
        canvas.after(90)
    t.seth(70)
    for i in range(170):
        t.fd(1)
        canvas.after(90)
    canvas.move("sav",0,32)
    s=4

def selecovr():
    global ysav
    brod.destroy()
    brdo.destroy()
    canvas.create_rectangle(-290, 220, 1490, 255, fill="red", outline="black", tag="sav")
    canvas.create_text(210, 300, text="Hajnáčka Ragácou- Hajnáčka Nové Cintorín\nHajnáčka Nové Cintorín - Hajnáčka ulica Na Hradu - 15 minút\nHajnáčka ulica do Hradu - Hajnáčka Hajnáčka Pekáreň - 10 minút\nHajnáčka Hajnáčka Pekáreň - Hajnáčka Lekáreň - \nHajnáčka Lekáreň - Hajnáčka Centrum",font="Italic 20 bold")
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    s=1
    def img():
        while s==1:
            image=open_image("HMD_NC.png")
    t1=Thread(target=img)
    t1.start()
    t.goto(-50,400)
    t.color("yellow")
    t.width(70)
    t.pendown()
    t.seth(240)
    for i in range(200):
        t.fd(1)
        canvas.after(90)
    t.seth(315)
    for i in range(80):
        t.fd(1)
        canvas.after(90)
    t.seth(225)
    for i in range(350):
        t.fd(1)
        canvas.after(90)
    canvas.move("sav",0,32)
    for i in range(150):
        t.fd(1)
        canvas.after(90)
        
    s=2
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==2:
            image=open_image("HMD_Upertown.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(0, 250)
    t.pendown()
    t.width(70)
    t.pendown()
    t.seth(255)
    canvas.move("sav",0,32)
    for i in range(100):
        t.fd(1)
        canvas.after(90)
    t.seth(330)
    for i in range(10):
        t.fd(1)
        canvas.after(90)
    t.seth(270)
    for i in range(180):
        t.fd(1)
        canvas.after(90)
    canvas.move("sav",0,32)
    s=3
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==3:
            image=open_image("HMD_Center.png")
    t1=Thread(target=img)
    t1.start()
    t.goto(250, 500)
    t.width(70)
    t.pendown()
    t.seth(270)
    for i in range(100):
        t.fd(1)
        canvas.after(90)
    t.lt(30)
    for i in range(150):
        t.fd(1)
        canvas.after(90)
    canvas.move("sav",0,32)
    t.rt(70)
    for i in range(160):
        t.fd(1)
        canvas.after(90)
    canvas.move("sav",0,32)
    for i in range(180):
        t.fd(1)
        canvas.after(90)
    canvas.delete("sav")
    s=4
        


#orange
def koloniac():
    global brdo,brod
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
    brdo = Button(window,text='do Selecov',font="Ariel 20 bold",command=kolonia,bg="lightgreen",width=50,height=20)
    brdo.bind("<Enter>", lambda event: on_enter(event, brdo))
    brdo.bind("<Leave>", lambda event: on_leave(event, brdo))
    brdo.place(x=0,y=100)
    brod=Button(window,text="do Centrum",font="Ariel 20 bold",command=koloniar,bg="lightgreen",width=50,height=20)
    brod.bind("<Enter>", lambda event: on_enter(event, brod))
    brod.bind("<Leave>", lambda event: on_leave(event, brod))
    brod.place(x=750,y=100)
def kolonia():
    global ysav
    brod.destroy()
    brdo.destroy()
    canvas.create_rectangle(-290, 220, 1490, 255, fill="red", outline="black", tag="sav")
    canvas.create_text(200, 280, text="Hajnáčka Centrum - Hajnáčka ulica Na Hradu - 10 minút\nHajnáčka ulica do Hradu - Hajnáčka ulica Nového - 14 minút\nHajnáčka ulica Nového - Hajnáčka ulica Selecov - 18 minút\nHajnáčka ulica Selecov - Hajnáčka ulica Zabovy - 22 minút",font="Italic 20 bold")
    s=1
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==1:
            image=open_image("HMD_Center.png")
    t1=Thread(target=img)
    t1.start()
    t.goto(20, -20)
    t.color("orange")
    t.width(70)
    t.pendown()
    t.seth(30)
    for i in range(200):
        t.fd(1)
        canvas.after(90)
    t.seth(55)
    for i in range(20):
        t.fd(1)
        canvas.after(90)
    for i in range(180):
        t.fd(1)
        canvas.after(90)
    t.seth(90)
    for i in range(150):
        t.fd(1)
        canvas.after(90)
    t.seth(110)
    for i in range(100):
        t.fd(1)
        canvas.after(90)
    s=2
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==2:
            image=open_image("HMD_Upertown.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(0, -180)
    t.pendown()
    t.width(70)
    t.pendown()
    t.seth(90)
    
    for i in range(100):
        t.fd(1)
        canvas.after(90)
    canvas.move("sav",0,32)
    for i in range(200):
        t.fd(1)
        canvas.after(90)
    t.seth(340)
    for i in range(250):
        t.fd(1)
        canvas.after(90)
    canvas.move("sav",0,32)
    for i in range(530):
        t.fd(1)
        canvas.after(90)
    s=3
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==3:
            image=open_image("HMD_Selec_Vilage.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(-180,-170)
    t.pendown()
    t.seth(70)
    canvas.move("sav",0,32)
    for i in range(550):
        t.fd(1)
    canvas.delete("sav")
    s=4
        
        
        
def koloniar():
    global ysav
    brod.destroy()
    brdo.destroy()
    canvas.create_rectangle(-290, 220, 1490, 255, fill="red", outline="black", tag="sav")
    canvas.create_text(200, 280, text="Hajnáčka ulica Zabovy - Hajnáčka ulica Selecov - 22 minút\nHajnáčka ulica Selecov - Hajnáčka ulica Nového - 18 minút\nHajnáčka ulica Nového - Hajnáčka ulica Na Hradu - 14 minút\nHajnáčka ulica Na Hradu - Hajnáčka Centrum - 10 minút",font="Italic 20 bold")
    s=1
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==1:
            image=open_image("HMD_Selec_Vilage.png")
    t1=Thread(target=img)
    t1.start()
    t.goto(30, 300)
    t.width(70)
    t.color("orange")
    t.pendown()
    t.width(70)
    t.seth(245)
    for i in range(500):
        t.fd(1)
    canvas.move("sav",0,32)
    s=2
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==2:
            image=open_image("HMD_Upertown.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(750,-100)
    t.pendown()
    t.seth(170)
    for i in range(600):
        t.fd(1)
        canvas.after(90)
    canvas.move("sav",0,32)
    t.rt(25)
    for i in range(220):
        t.fd(1)
        canvas.after(90)
    t.seth(270)
    for i in range(200):
        t.fd(1)
        canvas.after(90)
    canvas.move("sav",0,32)
    s=3
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==3:
            image=open_image("HMD_Center.png")
    t1=Thread(target=img)
    t1.start()
    t.goto(250, 500)
    t.width(70)
    t.pendown()
    t.seth(270)
    for i in range(100):
        canvas.after(90)
        t.fd(1)
    t.lt(30)
    for i in range(150):
        canvas.after(90)
        t.fd(1)
    t.rt(70)
    for i in range(160):
        canvas.after(90)
        t.fd(1)
    for i in range(180):
        canvas.after(90)
        t.fd(1)
    canvas.delete("sav")
    s=4
    
#cyan
def dohc():
    global brdo,brod
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
    brdo = Button(window,text='do Posa',font="Ariel 20 bold",command=doh,bg="lightgreen",width=50,height=20)
    brdo.bind("<Enter>", lambda event: on_enter(event, brdo))
    brdo.bind("<Leave>", lambda event: on_leave(event, brdo))
    brdo.place(x=0,y=100)
    brod=Button(window,text="do Centrum",font="Ariel 20 bold",command=dohr,bg="lightgreen",width=50,height=20)
    brod.bind("<Enter>", lambda event: on_enter(event, brod))
    brod.bind("<Leave>", lambda event: on_leave(event, brod))
    brod.place(x=750,y=100)
def doh():
    global ysav
    brod.destroy()
    brdo.destroy()
    canvas.create_rectangle(-290, 220, 1490, 255, fill="red", outline="black", tag="sav")
    canvas.create_text(200, 255, text="Hajnáčka Centrum - Hajnáčka Posa - 4 minúty\nHajnáčka Posa - Hajnáčka Posa do Tilíc - 6 minút",font="Italic 20 bold")
    s=1
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==1:
            image=open_image("HMD_Center.png")
    t1=Thread(target=img)
    t1.start()
    t.goto(80, -50)
    t.color("cyan")
    t.width(70)
    t.pendown()
    t.seth(240)
    for i in range(150):
        canvas.after(90)
        t.fd(1)
    t.seth(180)
    s=2
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==2:
            image=open_image("HMD_Posa.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(80, 400)
    t.pendown()
    t.width(70)
    t.pendown()
    for i in range(200):
        canvas.after(90)
        t.fd(1)
    canvas.move("sav",0,32)
    t.seth(225)
    for i in range(270):
        canvas.after(90)
        t.fd(1)
        t.lt(0.2)
    for i in range(300):
        canvas.after(90)
        t.fd(1)
    canvas.delete("sav")
    s=3
def dohr():
    global ysav
    brod.destroy()
    brdo.destroy()
    canvas.create_rectangle(-290, 220, 1490, 255, fill="red", outline="black", tag="sav")
    canvas.create_text(200, 270, text="Hajnáčka Posa do Tilíc - Hajnáčka Posa - 6 minút\nHajnáčka Posa - Hajnáčka Centrum - 4 minúty\n",font="Italic 20 bold")
    s=1
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==1:
            image=open_image("HMD_Posa.png")
    t1=Thread(target=img)
    t1.start()
    t.goto(-130, -180)
    t.width(70)
    t.color("cyan")
    t.pendown()
    t.seth(110)
    for i in range(300):
        canvas.after(90)
        t.fd(1)
    t.seth(70)
    for i in range(300):
        canvas.after(90)
        t.fd(1)
    canvas.move("sav",0,32)
    t.seth(0)
    for i in range(200):
        canvas.after(90)
        t.fd(1)
    s=2
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==2:
            image=open_image("HMD_Center.png")
    t1=Thread(target=img)
    t1.start()
    t.goto(0, -180)
    t.width(70)
    t.pendown()
    t.seth(60)
    for i in range(150):
        canvas.after(90)
        t.fd(1)
    canvas.delete("sav")
    s=3
    
    
#dark green
def posac():
    global brdo,brod
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
    brdo = Button(window,text='do ulica do Pesov',font="Ariel 20 bold",command=posa,bg="lightgreen",width=50,height=20)
    brdo.bind("<Enter>", lambda event: on_enter(event, brdo))
    brdo.bind("<Leave>", lambda event: on_leave(event, brdo))
    brdo.place(x=0,y=100)
    brod=Button(window,text="do Centrum",font="Ariel 20 bold",command=posar,bg="lightgreen",width=50,height=20)
    brod.bind("<Enter>", lambda event: on_enter(event, brod))
    brod.bind("<Leave>", lambda event: on_leave(event, brod))
    brod.place(x=750,y=100)
def posa():
    brod.destroy()
    brdo.destroy()
    canvas.create_rectangle(-290, 230, 1490, 265, fill="red", outline="black", tag="sav")
    canvas.create_text(200, 280, text="Hajnáčka Centrum - Hajnáčka Lekáreň - 2 minúty\nHajnáčka Lekáreň - Hajnáčka Futbal - 4 minúty\nHajnáčka Futbal - Hajnáčka ulica Pesov - 7 minút",font="Italic 20 bold")
    s=1
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==1:
            image=open_image("HMD_futbal.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(-650, 200)
    t.color("darkgreen")
    t.width(70)
    t.pendown()
    t.seth(40)
    for i in range(300):
        canvas.after(90)
        t.fd(1)
    canvas.move("sav",0,32)
    t.color("grey")
    for i in range(50):
        canvas.after(90)
        t.bk(1)
    t.seth(320)
    t.color("darkgreen")
    for i in range(150):
        canvas.after(90)
        t.fd(1)
    canvas.move("sav",0,32)
    for i in range(50):
        canvas.after(90)
        t.fd(1)
    t.seth(340)
    for i in range(750):
        canvas.after(90)
        t.fd(1)
    canvas.delete("sav")
    s=2
def posar():
    brod.destroy()
    brdo.destroy()
    canvas.create_rectangle(-290, 230, 1490, 265, fill="red", outline="black", tag="sav")
    canvas.create_text(200, 280, text="Hajnáčka ulica Pesov - Hajnáčka Futbal - 7 minút\nHajnáčka Futbal - Hajnáčka Lekáreň - 4 minúty\nHajnáčka Lekáreň - Hajnáčka Centrum - 2 minúty",font="Italic 20 bold")
    s=1
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==1:
            image=open_image("HMD_futbal.png")
    t1=Thread(target=img)
    t1.start()
    t.goto(450, -30)
    t.color("darkgreen")
    t.width(70)
    t.pendown()
    t.seth(160)
    for i in range(800):
        canvas.after(90)
        t.fd(1)
    canvas.move("sav",0,32)
    t.rt(25)
    for i in range(130):
        canvas.after(90)
        t.fd(1)
    t.rt(15)
    for i in range(50):
        canvas.after(90)
        t.fd(1)
    canvas.move("sav",0,32)
    t.lt(100)
    t.color("grey")
    for i in range(50):
        canvas.after(90)
        t.fd(1)
    t.color("darkgreen")
    for i in range(250):
        canvas.after(90)
        t.fd(1)
    canvas.delete("sav")
    s=2
#pink
def sjrdc():
    global brdo,brod
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
    brdo = Button(window,text='do Štavica',font="Ariel 20 bold",command=sjrd,bg="lightgreen",width=50,height=20)
    brdo.bind("<Enter>", lambda event: on_enter(event, brdo))
    brdo.bind("<Leave>", lambda event: on_leave(event, brdo))
    brdo.place(x=0,y=100)
    brod=Button(window,text="do Centrum",font="Ariel 20 bold",command=sjrdr,bg="lightgreen",width=50,height=20)
    brod.bind("<Enter>", lambda event: on_enter(event, brod))
    brod.bind("<Leave>", lambda event: on_leave(event, brod))
    brod.place(x=750,y=100)
def sjrd():
    brod.destroy()
    brdo.destroy()
    canvas.create_rectangle(-290, 230, 1490, 265, fill="red", outline="black", tag="sav")
    canvas.create_text(200, 310, text="Hajnáčka Centrum - Hajnáčka do Tenkeš - 4 minúty\nHajnáčka do Tenkeš - Hajnáčka Tenkeš - 7 minút\nHajnáčka Tenkeš - Hajnáčka Sťavica - 15 minút\nHajnáčka Sťavica - Hajnáčka S.J.R.D. - 12 minút\n",font="Italic 20 bold")
    s=1
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==1:
            image=open_image("HMD_Center.png")
    t1=Thread(target=img)
    t1.start()
    t.goto(80, -50)
    t.color("pink")
    t.width(70)
    t.pendown()
    t.seth(240)
    for i in range(150):
        canvas.after(90)
        t.fd(1)
    t.seth(180)
    s=2
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==2:
            image=open_image("HMD_Tenkes1.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(-750, 400)
    t.pendown()
    t.seth(325)
    for i in range(500):
        canvas.after(90)
        t.fd(1)
    t.seth(350)
    for i in range(230):
        canvas.after(90)
        t.fd(1)
    canvas.move("sav",0,32)
    s=3
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==3:
            image=open_image("HMD_DOtenkes.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(-350,350)
    t.pendown()
    t.seth(0)
    for i in range(700):
        canvas.after(90)
        t.fd(1)
        t.rt(0.08)
    canvas.move("sav",0,32)
    s=4
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==4:
            image=open_image("HMD_Stavica.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(-750,450)
    t.pendown()
    t.seth(345)
    for i in range(800):
        canvas.after(90)
        t.fd(1)
    t.seth(0)
    for i in range(600):
        canvas.after(90)
        t.fd(1)
    canvas.move("sav",0,32)
    t.seth(180)
    t.color("grey")
    for i in range(750):
        canvas.after(90)
        t.fd(1)
    t.color("pink")
    t.seth(195)
    for i in range(290):
        canvas.after(90)
        t.fd(1)
    canvas.delete("sav")
    s=5
def sjrdr():
    brod.destroy()
    brdo.destroy()
    canvas.create_rectangle(-290, 230, 1490, 265, fill="red", outline="black", tag="sav")
    canvas.create_text(200, 310, text="Hajnáčka S.J.R.D. - Hajnáčka Sťavica - 12 minút\nHajnáčka Sťavica - Hajnáčka Tenkeš - 15 minút\nHajnáčka Tenkeš - Hajnáčka do Tenkeš - 7 minút\nHajnáčka do Tenkeš - Hajnáčka Centrum - 4 minúty\n",font="Italic 20 bold")
    s=1
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==1:
            image=open_image("HMD_Stavica.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.color("pink")
    t.width(70)
    t.goto(-400,180)
    t.pendown()
    t.seth(15)
    for i in range(250):
        canvas.after(90)
        t.fd(1)
    t.seth(357)
    for i in range(750):
        canvas.after(90)
        t.fd(1)
    canvas.move("sav",0,32)
    t.color("grey")
    t.seth(175)
    for i in range(750):
        canvas.after(90)
        t.fd(1)
    t.color("pink")
    t.rt(12)
    for i in range(600):
        canvas.after(90)
        t.fd(1)
    s=2
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==2:
            image=open_image("HMD_DOtenkes.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(250,0)
    t.pendown()
    t.seth(120)
    canvas.move("sav",0,32)
    for i in range(700):
        canvas.after(90)
        t.fd(1)
        t.lt(0.08)
    s=3
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==3:
            image=open_image("HMD_Tenkes1.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(750,-150)
    t.pendown()
    t.seth(164)
    for i in range(800):
        canvas.after(90)
        t.fd(1)
    canvas.move("sav",0,32)
    for i in range(600):
        canvas.after(90)
        t.fd(1)
    t.rt(25)
    for i in range(200):
        canvas.after(90)
        t.fd(1)
    s=4
    canvas.create_rectangle(-1000,-1000,1000,220,fill="#c2c2d6")
    def img():
        while s==4:
            image=open_image("HMD_Center.png")
    t1=Thread(target=img)
    t1.start()
    t.penup()
    t.goto(0, -180)
    t.width(70)
    t.pendown()
    t.seth(60)
    for i in range(150):
        canvas.after(90)
        t.fd(1)
    canvas.delete("sav")
    s=5
def exit():
    window.destroy()

button = Button(window, text='Bus 1', command=centrumc, font=('Italic', 20, 'bold'),
                activebackground='#aab1ff', activeforeground='#393b55', width=200, height=250)
image = PhotoImage(file='centrum.png')
button.config(image=image, compound='top')

button2 = Button(window,text='Bus 2')
button2.config(command=gortvac) #performs call back of function
button2.config(font=('Italic',20,'bold'))
button2.config(activebackground='#aab1ff')
button2.config(activeforeground='#393b55')
image2 = PhotoImage(file='zelst.png')
button2.config(image=image2)
button2.config(compound='top')
button2.config(width=200,height=250)

button3 = Button(window,text='Bus 3')
button3.config(command=depoc) #performs call back of function
button3.config(font=('Italic',20,'bold'))
button3.config(activebackground='#aab1ff')
button3.config(activeforeground='#393b55')
image3 = PhotoImage(file='stav.png')
button3.config(image=image3)
button3.config(compound='top')
button3.config(width=200,height=250)

button4 = Button(window,text='Bus 4')
button4.config(command=tenkesc) #performs call back of function
button4.config(font=('Italic',20,'bold'))
button4.config(activebackground='#aab1ff')
button4.config(activeforeground='#393b55')
image4 = PhotoImage(file='tenkes.png')
button4.config(image=image4)
button4.config(compound='top')
button4.config(width=200,height=250)

button5 = Button(window,text='Bus 5')
button5.config(command=selecovc) #performs call back of function
button5.config(font=('Italic',20,'bold'))
button5.config(activebackground='#aab1ff')
button5.config(activeforeground='#393b55')
image5 = PhotoImage(file='ragacou.png')
button5.config(image=image5)
button5.config(compound='top')
button5.config(width=200,height=250)

button6 = Button(window,text='Bus 6')
button6.config(command=koloniac) #performs call back of function
button6.config(font=('Italic',20,'bold'))
button6.config(activebackground='#aab1ff')
button6.config(activeforeground='#393b55')
image6 = PhotoImage(file='kol.png')
button6.config(image=image6)
button6.config(compound='top')
button6.config(width=200,height=250)

button7 = Button(window,text='Bus 7')
button7.config(command=dohc) #performs call back of function
button7.config(font=('Italic',20,'bold'))
button7.config(activebackground='#aab1ff')
button7.config(activeforeground='#393b55')
image7 = PhotoImage(file='doh.png')
button7.config(image=image7)
button7.config(compound='top')
button7.config(width=200,height=250)

button8 = Button(window,text='Bus 8')
button8.config(command=posac) #performs call back of function
button8.config(font=('Italic',20,'bold'))
button8.config(activebackground='#aab1ff')
button8.config(activeforeground='#393b55')
image8 = PhotoImage(file='posa.png')
button8.config(image=image8)
button8.config(compound='top')
button8.config(width=200,height=250)

button9 = Button(window,text='Bus 9')
button9.config(command=sjrdc) #performs call back of function
button9.config(font=('Italic',20,'bold'))
button9.config(activebackground='#aab1ff')
button9.config(activeforeground='#393b55')
image9 = PhotoImage(file='sjrd.png')
button9.config(image=image9)
button9.config(compound='top')
button9.config(width=200,height=250)

button10 = Button(window, text='Exit', command=exit, font=('Italic', 20, 'bold'),activebackground='#aab1ff', activeforeground='#393b55', width=200, height=250)
image10 = PhotoImage(file='exit.png')
button10.config(image=image10, compound='top')
def busses():
    button.place(x=0,y=0)
    button2.place(x=250,y=0)
    button3.place(x=500,y=0)
    button4.place(x=750,y=0)
    button5.place(x=1000,y=0)
    button6.place(x=0,y=250)
    button7.place(x=250,y=250)
    button8.place(x=500,y=250)
    button9.place(x=750,y=250)
    button10.place(x=1000,y=250)
# Define custom colors
primary_color = "#3498db"  # Blue
secondary_color = "#e74c3c"  # Red
background_color = "#ecf0f1"  # Light Gray
text_color = "#333333"  # Dark Gray
button_color = "#2ecc71"  # Green
# Use the custom colors in your UI elements
window.configure(bg=background_color)
time_label.config(bg=background_color, fg=text_color)
day_label.config(bg=background_color, fg=text_color)
date_label.config(bg=background_color, fg=text_color)
buttons=[button,button2,button3,button4,button5,button6,button7,button8,button9,button10]
for b in buttons:
    b.config(bg=button_color)
error_message_label = Label(window, text="An error occurred.", bg=background_color, fg=secondary_color)
def on_enter(event,button):
    button.config(bg="green")
def on_leave(event,button):
    button.config(bg=button_color)
for b in buttons:
    b.bind("<Enter>", lambda event, button=b: on_enter(event, button))
    b.bind("<Leave>", lambda event, button=b: on_leave(event, button))
def reopenw():
    call(["python","ajnacskobusmenetrendbiytonsagimentes.py"])
    exit()
reopen=Button(window,text="Back to routes",command=reopenw)
reopen.pack()
update()
busses()
window.mainloop()
