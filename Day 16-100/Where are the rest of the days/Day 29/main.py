import json
import os
import tkinter

FONT_NAME = "Courier"
FILE_NAME = "passwords.txt"

data = []
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        data = json.load(file)
else:
    data = []


def store_data():
    data.append({
        "website": website_entry.get(),
        "email": email_entry.get(),
        "password": password_entry.get(),
    })
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    website_entry.delete(0, tkinter.END)
    email_entry.delete(0, tkinter.END)
    email_entry.insert(0, "email@gmail.com")
    password_entry.delete(0, tkinter.END)


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

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

website_entry = tkinter.Entry(width=50, font=("Arial", 20, "bold"))
website_entry.grid(column=1, row=2, columnspan=2, sticky=tkinter.W, pady=10)
website_entry.focus()

email_entry = tkinter.Entry(width=50, font=("Arial", 20, "bold"))
email_entry.grid(column=1, row=3, columnspan=2, sticky=tkinter.W, pady=10)
email_entry.insert(0, "email@gmail.com")

password_entry = tkinter.Entry(width=33, font=("Arial", 20, "bold"))
password_entry.grid(column=1, row=4, sticky=tkinter.W, pady=10)

gen_pass_button = tkinter.Button(text="Generate Password", width=20, font=("Arial", 14, "bold"))
gen_pass_button.grid(column=2, row=4, sticky=tkinter.W, pady=10)

add_pass_button = tkinter.Button(text="add", width=62, font=("Arial", 14, "bold"), command=store_data)
add_pass_button.grid(column=1, row=5, columnspan=2, sticky=tkinter.W, pady=10)


window.mainloop()