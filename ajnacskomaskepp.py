from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from time import strftime

class BusDisplayApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Bus Display App")
        self.window.geometry("1200x1000")

        self.canvas = Canvas(self.window, height=700, width=1200)
        self.canvas.pack()

        self.setup_labels()
        self.setup_buttons()

        self.image_paths = {
            "Centrum": ["HMD_Center.jpg", "HMD_Zel._Stanica.jpg", "HMD_Stavica.jpg"],
            "Zelst": ["HMD_Center.jpg", "HMD_Zel._Stanica.jpg", "HMD_Doh.jpg", "HMD_Kolonia.jpg", "HMD_Gortva.jpg"],
            "Stavica": ["HMD_Center.jpg", "HMD_Doh.jpg", "HMD_Kolonia.jpg", "HMD_Zel._Stanica.jpg"],
            "Tenkes": ["HMD_Center.jpg", "HMD_Doh..jpg", "HMD_Upertown.jpg", "HMD_Ragacou.jpg"],
            "Selecov": ["HMD_Center.jpg", "HMD_Doh..jpg", "HMD_Upertown.jpg", "HMD_Ragacou.jpg"],
            "Kolonia": ["HMD_Center.jpg", "HMD_Doh..jpg", "HMD_Upertown.jpg", "HMD_Selec_Vilage.jpg"],
            "Doh": ["HMD_Center.jpg", "HMD_Posa.jpg"],
            "Posa": ["HMD_Center.jpg", "HMD_futbal.jpg"],
            "Sjrd": ["HMD_Center.jpg", "HMD_Tenkes1.jpg", "HMD_Stavica.jpg"]
        }

        self.current_image_index = 0
        self.current_route = None

    def setup_labels(self):
        self.time_label = Label(self.window, font=("Italic", 50, "bold"), fg="#00FF00", bg="black")
        self.time_label.place(x=0, y=900)

        self.day_label = Label(self.window, font=("Italic", 30, "bold"), fg="#00FF00", bg="black")
        self.day_label.place(x=0, y=850)

        self.date_label = Label(self.window, font=("Italic", 30, "bold"), fg="#00FF00", bg="black")
        self.date_label.place(x=0, y=800)

    def setup_buttons(self):
        button_positions = [
            (0, 0), (250, 0), (500, 0), (750, 0), (1000, 0),
            (0, 250), (250, 250), (500, 250), (750, 250),
            (1000, 250)
        ]

        routes = list(self.image_paths.keys())

        self.buttons = []

        for i, route in enumerate(routes):
            button = Button(self.window, text=f'Bus {i + 1}')
            button.config(command=lambda r=route: self.display_route(r))
            button.config(font=('Italic', 20, 'bold'))
            button.config(activebackground='#aab1ff')
            button.config(activeforeground='#393b55')
            button.config(width=200, height=250)
            image = PhotoImage(file=f'{route.lower()}.png')
            button.config(image=image)
            button.config(compound='top')
            button.image = image  # Store a reference to the image to prevent it from being garbage collected
            button.place(x=button_positions[i][0], y=button_positions[i][1])
            self.buttons.append(button)

        exit_button = Button(self.window, text='Exit', command=self.window.destroy)
        exit_button.config(font=('Italic', 20, 'bold'))
        exit_button.config(activebackground='#aab1ff')
        exit_button.config(activeforeground='#393b55')
        exit_button.config(width=200, height=250)
        image = PhotoImage(file='exit.png')
        exit_button.config(image=image)
        exit_button.config(compound='top')
        exit_button.image = image
        exit_button.place(x=1000, y=500)

    def open_image(self, image_path):
        img = Image.open(image_path)
        img.thumbnail((self.canvas.winfo_width(), self.canvas.winfo_height()))
        img_tk = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        self.canvas.img = img_tk

    def open_next_image(self, route, delay):
        if self.current_image_index < len(self.image_paths[route]):
            image_path = self.image_paths[route][self.current_image_index]
            self.open_image(image_path)
            self.current_image_index += 1
            self.window.after(delay, lambda: self.open_next_image(route, delay))
        else:
            self.current_image_index = 0

    def update(self):
        time_string = strftime("%I:%M:%S %p")
        self.time_label.config(text=time_string)
        day_string = strftime("%A")
        self.day_label.config(text=day_string)
        date_string = strftime("%B %d, %Y")
        self.date_label.config(text=date_string)
        self.window.after(1000, self.update)

    def display_route(self, route):
        self.current_route = route
        self.current_image_index = 0
        self.open_image(self.image_paths[route][0])
        self.window.after(1000, lambda: self.open_next_image(route, 1000))

    def run(self):
        self.update()
        self.window.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = BusDisplayApp(root)
    app.run()