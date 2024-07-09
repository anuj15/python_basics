from tkinter import *

import requests


def display_quote():
    response = requests.get(url='https://api.kanye.rest')
    response.raise_for_status()
    quote = response.json()['quote']
    canvas.itemconfig(canvas_quote, text=quote, fill='white')


window = Tk()
window.title('Kanye Quotes')
window.config(padx=20, pady=20)

background_image = PhotoImage(file='background.png')
button_image = PhotoImage(file='kanye.png')

canvas = Canvas(width=300, height=414)
canvas.create_image(150, 207, image=background_image)
canvas_quote = canvas.create_text(150, 207, text='Kanye Quotes...', font=('Arial', 20, 'bold'), width='250')
canvas.pack()

button = Button(highlightthickness=0, border=0)
button.config(image=button_image, command=display_quote)
button.pack()

window.mainloop()
