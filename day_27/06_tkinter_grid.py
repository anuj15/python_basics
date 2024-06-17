from tkinter import Tk, Label, Button, Entry, END

window = Tk()
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

label = Label()
label.config(text='I am a label')
label.grid(row=0, column=0)

button_1 = Button(text='button 1')
button_1.grid(row=1, column=1)

button_2 = Button(text='button 2')
button_2.grid(row=0, column=2)

entry = Entry(width=25)
entry.insert(END, 'Some text to begin with.')
entry.grid(row=2, column=3)

window.mainloop()
