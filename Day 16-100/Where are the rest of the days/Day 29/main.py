import json
import os
import random
import string
import tkinter
from tkinter import messagebox

FONT_NAME = "Courier"
FILE_NAME = "passwords.txt"

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


data = {}
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        data = json.load(file)

def search_password():
    website = website_entry.get()

    if website in data:
        messagebox.showinfo(title=website, message=f"Email: {data[website]["email"]} \nPassword: {data[website]["password"]}")
    else:
        messagebox.showinfo(title="Not Found", message="Website not registred")

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def fill_and_copy_password():
    password = generate_password()
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)

    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()


def store_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not email or not password:
        messagebox.showerror(title="Error", message="Please enter all required information")
        return


    new_entry = {
        "email": email,
        "password": password,
    }

    if website in data:
        overwrite = messagebox.askyesno(
            title="warning",
            message=f"'{website}' already exists.\nDo you want to overwrite it?"
        )
        if not overwrite:
            return

    data[website] = new_entry

    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    website_entry.delete(0, tkinter.END)
    email_entry.delete(0, tkinter.END)
    email_entry.insert(0, "email@gmail.com")
    password_entry.delete(0, tkinter.END)



canvas = tkinter.Canvas(width=500, height=500)
lock_img = tkinter.PhotoImage(file="lock.png")
canvas.create_image(250, 250, image=lock_img)
canvas.grid(column=1, row=1)

title_label = tkinter.Label(text="Password Manager", fg="lightBlue", font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

website_label = tkinter.Label(text="Website:", fg="darkBlue", font=(FONT_NAME, 25, "bold"))
website_label.grid(column=0, row=2, sticky=tkinter.E, pady=10)

email_label = tkinter.Label(text="email/username:", fg="darkBlue", font=(FONT_NAME, 25, "bold"))
email_label.grid(column=0, row=3, sticky=tkinter.E, pady=10)

password_label = tkinter.Label(text="password:", fg="darkBlue", font=(FONT_NAME, 25, "bold"))
password_label.grid(column=0, row=4, sticky=tkinter.E, pady=10)

website_entry = tkinter.Entry(width=33, font=("Arial", 20, "bold"))
website_entry.grid(column=1, row=2, sticky=tkinter.W, pady=10)
website_entry.focus()

search_website_button = tkinter.Button(text="Search", width=20, font=("Arial", 14, "bold"), command=search_password)
search_website_button.grid(column=2, row=2, sticky=tkinter.W, pady=10)

email_entry = tkinter.Entry(width=50, font=("Arial", 20, "bold"))
email_entry.grid(column=1, row=3, columnspan=2, sticky=tkinter.W, pady=10)
email_entry.insert(0, "email@gmail.com")

password_entry = tkinter.Entry(width=33, font=("Arial", 20, "bold"))
password_entry.grid(column=1, row=4, sticky=tkinter.W, pady=10)

gen_pass_button = tkinter.Button(text="Generate Password", width=20, font=("Arial", 14, "bold"), command=fill_and_copy_password)
gen_pass_button.grid(column=2, row=4, sticky=tkinter.W, pady=10)

add_pass_button = tkinter.Button(text="add", width=62, font=("Arial", 14, "bold"), command=store_data)
add_pass_button.grid(column=1, row=5, columnspan=2, sticky=tkinter.W, pady=10)


window.mainloop()