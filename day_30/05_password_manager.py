import json
from random import choice, shuffle, randint
from tkinter import *
from tkinter import messagebox

import pandas


def search():
    website = website_entry.get()
    try:
        data = pandas.read_json('data.json').to_dict()
    except FileNotFoundError:
        messagebox.showinfo(title=website, message='File does not exist')
    else:
        if website in data:
            message = f'Email: {data[website]["username"]}\nPassword: {data[website]["password"]}'
            messagebox.showinfo(title=website, message=message)
        else:
            messagebox.showinfo(title=website, message='No Results Found')


def set_default():
    username_entry.insert(0, 'anuj.nits@gmail.com')


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    letter = [choice(letters) for _ in range(randint(8, 10))]
    number = [choice(numbers) for _ in range(randint(2, 4))]
    symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password = letter + number + symbol
    shuffle(password)
    password_entry.insert(END, ''.join(password))


def clear_password():
    password_entry.delete(0, END)


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'username': username,
            'password': password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='Please make sure you haven\'t left any fields empty')
    else:
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            with open('data.json', 'w') as f:
                json.dump(new_data, f, indent=4)
        else:
            with open('data.json', 'w') as f:
                data.update(new_data)
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def clear_all():
    website_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# canvas
lock_image = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

username_label = Label(text='Email/Username:')
username_label.grid(row=2, column=0)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry()
website_entry.grid(row=1, column=1, sticky='EW')
website_entry.focus()

username_entry = Entry()
username_entry.grid(row=2, column=1, sticky='EW')

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky='EW')

# Buttons
search_button = Button(text='Search', command=search)
search_button.grid(row=1, column=2, columnspan=2, sticky='EW')

username_button = Button(text='Set Default', command=set_default)
username_button.grid(row=2, column=2, columnspan=2, sticky='EW')

password_button = Button(text='Generate Password', command=generate_password)
password_button.grid(row=3, column=2, sticky='EW')

clear_button = Button(text='Clear', command=clear_password)
clear_button.grid(row=3, column=3, sticky='EW')

save_button = Button(text='Save', command=save)
save_button.grid(row=4, column=1, columnspan=2, sticky='EW')

clear_all = Button(text='Clear All', command=clear_all)
clear_all.grid(row=4, column=2, columnspan=2, sticky='EW')

window.mainloop()
