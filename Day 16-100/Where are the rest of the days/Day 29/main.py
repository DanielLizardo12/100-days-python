import tkinter

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(window, width=600, height=600)
lock_img = tkinter.PhotoImage(file="lock.png")
canvas.create_image(300, 300, image=lock_img)
canvas.grid(column=1, row=1)


window.mainloop()