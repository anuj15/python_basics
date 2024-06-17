from tkinter import *


def button_used():
    print(entry.get())


def spinbox_used():
    print(spinbox.get())


def scale_used(value):
    print(value)


def check_button_used():
    print(checked_state.get())


def radio_button_used():
    print(radio_state.get())


def list_box_used(event):
    print(list_box.get(list_box.curselection()))


window = Tk()
window.minsize(width=500, height=300)
window.title('Tkinter')

label = Label()
label.config(text='I am a label')
label.pack()

button = Button(text='Click Me', command=button_used)
button.pack()

entry = Entry(width=30)
entry.insert(END, 'Some text to begin with.')
entry.pack()

text = Text(width=30, height=5)
text.focus()
text.insert(END, 'Example of multi-line text entry.')
text.pack()

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

checked_state = IntVar()
checkbox = Checkbutton(text='is on?', variable=checked_state, command=check_button_used)
checkbox.pack()

radio_state = IntVar()
radio_button_1 = Radiobutton(text='Option 1', value=1, variable=radio_state, command=radio_button_used)
radio_button_2 = Radiobutton(text='Option 2', value=2, variable=radio_state, command=radio_button_used)
radio_button_1.pack()
radio_button_2.pack()

fruits = ['Apple', 'Pear', 'Orange', 'Banana']
list_box = Listbox(height=4)
for fruit in fruits:
    list_box.insert(fruits.index(fruit), fruit)
list_box.bind('<<ListboxSelect>>', list_box_used)
list_box.pack()

window.mainloop()
