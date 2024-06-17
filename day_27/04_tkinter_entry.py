from tkinter import Tk, Button, Label, Entry


def on_click():
    label.config(text=entry.get())


window = Tk()
window.title('learning Tkinter')
window.minsize(width=500, height=300)

label = Label()
label.config(text='I am a label', font=('Courier', 16, 'bold'))
label.pack()

button = Button(text='Click Me', command=on_click)
button.pack()

entry = Entry(width=10)
entry.pack()

window.mainloop()
