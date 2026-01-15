import tkinter

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window = tkinter.Tk()
window.title("Pomodoro")
#window.config(padx=50, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=400, height=400, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(200, 200, image=tomato_img)
canvas.create_text(200, 230, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

window.mainloop()