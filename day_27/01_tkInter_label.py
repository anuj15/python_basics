from tkinter import Tk, Label

window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
label = Label(text='I am a Label', font=('Courier', 24, 'bold'))
label.pack()
window.mainloop()
