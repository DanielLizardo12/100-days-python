import tkinter

def button_clicked():
    my_label["text"] = input_tk.get()

window = tkinter.Tk()
window.title("First GUI program")
window.minsize(500, 300)

#Label
my_label = tkinter.Label(text="hello", font=("Arial", 25, "bold"))
my_label.pack()

##button
button = tkinter.Button(text="Click here", command=button_clicked)
button.pack()

#entry
input_tk = tkinter.Entry(width=10)
input_tk.pack()

window.mainloop()