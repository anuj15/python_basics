from random import *
from tkinter import *
from tkinter import messagebox

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    separator = ' | '

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='Please don\'t leave any empty fields')
    else:
        user_input = messagebox.askokcancel(title=website, message=f'Email: {username}\nPassword: {password}')
        print(user_input)
        if user_input:
            new_data = website + separator + username + separator + password + '\n'
            with open(file='data.txt', mode='a') as f:
                f.write(new_data)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

username_label = Label(text='Email/Username:')
username_label.grid(row=2, column=0)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky='EW')
website_entry.focus()

username_entry = Entry()
username_entry.grid(row=2, column=1, columnspan=2, sticky='EW')
username_entry.insert(0, 'anuj.nits@gmail.com')

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky='EW')

generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')

window.mainloop()
