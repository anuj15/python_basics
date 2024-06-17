import random
from tkinter import *

import pandas

try:
    to_learn = pandas.read_csv('data/words_to_learn.csv').to_dict(orient='records')
except FileNotFoundError:
    to_learn = pandas.read_csv('data/french_words.csv').to_dict(orient='records')
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(title_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=current_card['French'], fill='black')
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn).to_csv('data/words_to_learn.csv', index=False)
    next_card()


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(title_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=current_card['English'], fill='white')


bg = '#B1DDC6'

window = Tk()
window.title('Flash Cards')
window.config(padx=20, pady=20, bg=bg)

flip_timer = window.after(3000, func=flip_card)

right_image = PhotoImage(file='./images/right.png')
wrong_image = PhotoImage(file='./images/wrong.png')

card_front_image = PhotoImage(file='./images/card_front.png')
card_back_image = PhotoImage(file='./images/card_back.png')

canvas = Canvas(width=800, height=526, highlightthickness=0, border=0, bg=bg)

canvas_image = canvas.create_image(400, 263, image=card_front_image)

title_text = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))

canvas.grid(row=0, column=0, columnspan=2)

unknown_button = Button(image=wrong_image, highlightthickness=0, border=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_button = Button(image=right_image, highlightthickness=0, border=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
