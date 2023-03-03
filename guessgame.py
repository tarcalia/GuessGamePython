import random
from tkinter import *


number = int(0)
expectedNumber = random.randint(1, 100)


def determine_number(guess):
    global expectedNumber
    if guess == expectedNumber:
        guess_label['text'] = f'You win!'
        reply_label['text'] = f'New number generated'
        expectedNumber = random.randint(1, 100)
    elif guess > expectedNumber:
        reply_label['text'] = 'Number should be smaller'
    else:
        reply_label['text'] = f'Number should be bigger'


def button_click():
    global number
    guess = int(name_entry.get())
    if guess != '':
        guess_label['text'] = f"Your guess was {guess}"
        number = guess
        determine_number(guess)


root = Tk()
name_frame = Frame(master=root)
name_label = Label(master=name_frame, text='Guess:')
name_label.grid(column=0, row=0)
name_entry = Entry(master=name_frame)
name_entry.grid(column=1, row=0)
name_frame.pack()
button = Button(master=root, text='Guess a number!', command=button_click)
button.pack()
guess_label = Label(master=root, text='Guess a number game!')
guess_label.pack()
reply_label = Label(master=root, text='Number between 1 and 100')
reply_label.pack()
root.mainloop()
