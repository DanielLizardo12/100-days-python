import tkinter

def calculate():
    result_label["text"] = float(entry.get()) * 1.60934

window = tkinter.Tk()
window.title("Mile to Km converter")
window.minsize(300, 120)
window.config(padx=40, pady=20)

initial_value = tkinter.IntVar(value=0)
entry = tkinter.Entry(width=10, textvariable=initial_value)
entry.grid(column=1, row=0)

equal_label = tkinter.Label(text="Is equal to", font=("Arial", 10))
equal_label.grid(column=0, row=1)

miles_label = tkinter.Label(text="Miles", font=("Arial", 10))
miles_label.grid(column=2, row=0)

result_label = tkinter.Label(text=0, font=("Arial", 10))
result_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km", font=("Arial", 10))
km_label.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()