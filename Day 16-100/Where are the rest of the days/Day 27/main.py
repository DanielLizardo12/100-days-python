import tkinter

window = tkinter.Tk()
window.title("First GUI program")
window.minsize(500, 300)

#Label
my_label = tkinter.Label(text="hello", font=("Arial", 25, "bold"))
my_label.pack(side="left")

window.mainloop()