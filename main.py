from tkinter import *
from tkinter import messagebox
from random import choice, randint, random, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    new_letters = [choice(letters) for _ in range(randint(8, 10))]
    new_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    new_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = new_letters + new_symbols + new_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    Password_textbox.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    site = website_name.get()
    username = Email_textbox.get()
    password = Password_textbox.get()
    new_data = {
        site: {
            'Email': username,
            'Password': password,
        }
    }

    if len(site) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title='Error', message='Please fill out all of the details.')
        return

    ok = messagebox.askokcancel(title=site, message='Do you want to save the current details?')

    if ok:
        try:
            with open(file='data.json', mode='r') as data_file:
                # json.load returns the content of the doc as a python dictionary
                data = json.load(data_file)
                # json.update adds new data into an existing python dictionary
                data.update(new_data)
            with open(file='data.json', mode='w') as data_file:
                json.dump(data, data_file, indent=4)

        except:
            with open('data.json', mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)

        finally:
            website_name.delete(0, END)
            Password_textbox.delete(0, END)


# ---------------------------- Search ------------------------------- #
def search():
    try:
        web = website_name.get()
        with open('data.json', mode='r') as data_file:
            data = json.load(data_file)

        user_name = data[web]['Email']
        pass_word = data[web]['Password']
        messagebox.showinfo(title=web, message=f'Email: {user_name} \n Password: {pass_word}')

    except:
        messagebox.showerror(title='Error', message='No Data File Found.')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=60, pady=60)  # This adds space between the window outline and contents such as canvas

canvas = Canvas(width=200, height=200)
mypic = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=mypic)
canvas.grid(row=0, column=1)

# LABELS
website = Label(text='Website:', anchor='center', highlightthickness=0)
website.grid(row=1, column=0)

Email_User = Label(text='Email/Username:', anchor='center', highlightthickness=0)
Email_User.grid(row=2, column=0)

Password = Label(text='Password:', anchor='center', highlightthickness=0)
Password.grid(row=3, column=0)

# ENTRIES
website_name = Entry(width=24)
website_name.grid(row=1, column=1)
website_name.focus()  # This puts the cursor in this textbox when the program is lunched

Email_textbox = Entry(width=42)
Email_textbox.grid(row=2, column=1, columnspan=2)

Password_textbox = Entry(width=24)
Password_textbox.grid(row=3, column=1)

# BUTTONS
Generate_password = Button(text='Generate Password', highlightthickness=0, bg='white', anchor='w',
                           command=generate_password)
Generate_password.grid(row=3, column=2)

Add_password = Button(text='Add', highlightthickness=0, width=36, bg='white', command=save)
Add_password.grid(row=4, column=1, columnspan=2)

Search = Button(text='Search', highlightthickness=0, bg='white', width=14, command=search)
Search.grid(row=1, column=2)
# Search.place(x=274, y=202)

window.mainloop()
