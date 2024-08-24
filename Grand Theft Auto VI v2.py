from tkinter import *
import pygame

def click():
    print("Why did I move here?")
    print("Guess it was the weather")

def breaking():
    wn.destroy()

# Initialize Pygame mixer
pygame.mixer.init()

# Load the audio file
pygame.mixer.music.load("love_is_a_long_road.mp3")

# Play the audio on a loop
pygame.mixer.music.play(-1)

wn = Tk()
wn.geometry("1280x720")
wn.title("Grand Theft Auto VI")

icon = PhotoImage(file='icon.png')
wn.config(background="#ff61e5")
wn.iconphoto(True, icon)

photo = PhotoImage(file='icon.png')
menu = PhotoImage(file="menu.png")
label = Label(wn,
              text="Copyright® Rockstar 2025",
              font=("typewriter", 20, 'bold'),
              fg='#85daff',
              bg='#ff61e5',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=menu,
              compound='top')
label.place(x=200, y=0)

button = Button(wn,
                text='Story mode',
                command=click,
                font=("Arial", 20, 'bold'))
button.place(x=950, y=650)

button2 = Button(wn,
                 text='Setting',
                 command=click,
                 font=("Arial", 20, 'bold'))
button2.place(x=1150, y=650)

button3 = Button(wn,
                 text='Exit',
                 command=breaking,
                 font=("Arial", 20, 'bold'))
button3.place(x=850, y=650)

wn.mainloop()
