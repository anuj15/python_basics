from tkinter import Tk, Button, Label

window = Tk()
window.title('Label & Button')
window.minsize(width=500, height=300)

label = Label()
label.config(text='I am a label', font=('Courier', 12, 'italic'))
label.pack()


def to_do():
    label.config(text='Button got clicked')


button = Button(text='click Me', command=to_do)
button.pack()
window.mainloop()
