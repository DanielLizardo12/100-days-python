import tkinter

def button_clicked():
    my_label["text"] = input_tk.get()

window = tkinter.Tk()
window.title("First GUI program")
window.minsize(500, 300)
window.config(padx=20, pady=20)

#Label
my_label = tkinter.Label(text="hello", font=("Arial", 25, "bold"))
my_label.grid(column=0, row=0)

##button
button = tkinter.Button(text="Click here", command=button_clicked)
button.grid(column=1, row=1)

#entry
input_tk = tkinter.Entry(width=10)
input_tk.grid(column=3, row=2)

button_1 = tkinter.Button(text="Click here again", command=button_clicked)
button_1.grid(column=2, row=0)

window.mainloop()