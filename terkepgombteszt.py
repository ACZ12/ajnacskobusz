from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from time import *
import datetime
window=Tk()
canvas=Canvas(window,height=1000,width=1200)
canvas.pack()

def open_image(image_path):
    img = Image.open(image_path)
    img.thumbnail((canvas.winfo_width(), canvas.winfo_height()))  # Resize the image to fit the canvas
    img_tk = ImageTk.PhotoImage(img)  # Create a PhotoImage object from the PIL image
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas.img = img_tk

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    day_string = strftime("%A")
    day_label.config(text=day_string)
    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)
    window.after(1000,update)
time_label = Label(window,font=("Italic",50,"bold"),fg="#00FF00",bg="black")
time_label.place(x=0,y=900)
day_label = Label(window,font=("Italic",30,"bold"),fg="#00FF00",bg="black")
day_label.place(x=0,y=850)
date_label = Label(window,font=("Italic",30,"bold"),fg="#00FF00",bg="black")
date_label.place(x=0,y=800)

def centrum():
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    open_image("HMD_Center.jpg")
    
if open_image("HMD_Center.jpg")==1:
    window.after(1000)
    open_image("HMD_Zel._Stanica.jpg")

def zelst():
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    open_image("HMD_Zel._Stanica.jpg")
def stavica():
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    open_image("HMD_Stavica.jpg")
def tenkes():
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    open_image("HMD_Tenkes1.jpg")
def selecov():
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    open_image("HMD_Selec_Vilage.jpg")
def kolonia():
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    open_image("HMD_Kolonia.jpg")
def doh():
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    open_image("HMD_Doh..jpg")
def posa():
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    open_image("HMD_Posa.jpg")
def exit():
    window.destroy()

button = Button(window,text='Bus 1')
button.config(command=centrum) #performs call back of function
button.config(font=('Italic',20,'bold'))
button.config(activebackground='#aab1ff')
button.config(activeforeground='#393b55')
image = PhotoImage(file='centrum.png')
button.config(image=image)
button.config(compound='top')
button.config(width=200,height=250)

button2 = Button(window,text='Bus 2')
button2.config(command=zelst) #performs call back of function
button2.config(font=('Italic',20,'bold'))
button2.config(activebackground='#aab1ff')
button2.config(activeforeground='#393b55')
image2 = PhotoImage(file='zelst.png')
button2.config(image=image2)
button2.config(compound='top')
button2.config(width=200,height=250)

button3 = Button(window,text='Bus 3')
button3.config(command=stavica) #performs call back of function
button3.config(font=('Italic',20,'bold'))
button3.config(activebackground='#aab1ff')
button3.config(activeforeground='#393b55')
image3 = PhotoImage(file='stav.png')
button3.config(image=image3)
button3.config(compound='top')
button3.config(width=200,height=250)

button4 = Button(window,text='Bus 4')
button4.config(command=tenkes) #performs call back of function
button4.config(font=('Italic',20,'bold'))
button4.config(activebackground='#aab1ff')
button4.config(activeforeground='#393b55')
image4 = PhotoImage(file='tenkes.png')
button4.config(image=image4)
button4.config(compound='top')
button4.config(width=200,height=250)

button5 = Button(window,text='Bus 5')
button5.config(command=selecov) #performs call back of function
button5.config(font=('Italic',20,'bold'))
button5.config(activebackground='#aab1ff')
button5.config(activeforeground='#393b55')
image5 = PhotoImage(file='sel.png')
button5.config(image=image5)
button5.config(compound='top')
button5.config(width=200,height=250)

button6 = Button(window,text='Bus 6')
button6.config(command=kolonia) #performs call back of function
button6.config(font=('Italic',20,'bold'))
button6.config(activebackground='#aab1ff')
button6.config(activeforeground='#393b55')
image6 = PhotoImage(file='kol.png')
button6.config(image=image6)
button6.config(compound='top')
button6.config(width=200,height=250)

button7 = Button(window,text='Bus 7')
button7.config(command=doh) #performs call back of function
button7.config(font=('Italic',20,'bold'))
button7.config(activebackground='#aab1ff')
button7.config(activeforeground='#393b55')
image7 = PhotoImage(file='doh.png')
button7.config(image=image7)
button7.config(compound='top')
button7.config(width=200,height=250)

button8 = Button(window,text='Bus 8')
button8.config(command=posa) #performs call back of function
button8.config(font=('Italic',20,'bold'))
button8.config(activebackground='#aab1ff')
button8.config(activeforeground='#393b55')
image8 = PhotoImage(file='posa.png')
button8.config(image=image8)
button8.config(compound='top')
button8.config(width=200,height=250)

button9 = Button(window,text='Exit')
button9.config(command=exit) #performs call back of function
button9.config(font=('Italic',20,'bold'))
button9.config(activebackground='#aab1ff')
button9.config(activeforeground='#393b55')
image9 = PhotoImage(file='exit.png')
button9.config(image=image9)
button9.config(compound='top')
button9.config(width=200,height=250)

def busses():
    button.place(x=0,y=0)
    button2.place(x=250,y=0)
    button3.place(x=500,y=0)
    button4.place(x=0,y=250)
    button5.place(x=250,y=250)
    button6.place(x=500,y=250)
    button7.place(x=0,y=500)
    button8.place(x=250,y=500)
    button9.place(x=500,y=500)
    
update()
busses()
window.mainloop()