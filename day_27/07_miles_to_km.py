from tkinter import Tk, Label, Button, Entry


def convert():
    miles = miles_value.get()
    km = float(miles) * 1.6
    label_miles_value.config(text=int(km))


window = Tk()
window.minsize(width=300, height=200)
window.title('Miles to Km Converter')
window.config(padx=20, pady=20)

miles_value = Entry(width=10)
miles_value.grid(row=0, column=1, padx=10, pady=10)

label_miles = Label(text='Miles')
label_miles.grid(row=0, column=2)

label_is_equal_to = Label(text='is equal to')
label_is_equal_to.grid(row=1, column=0)

label_miles_value = Label(text='')
label_miles_value.grid(row=1, column=1)

label_km = Label(text='Km')
label_km.grid(row=1, column=2)

calculate_button = Button(text='Calculate', command=convert)
calculate_button.grid(row=2, column=1)

window.mainloop()
