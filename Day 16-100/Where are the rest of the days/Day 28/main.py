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
window.config(padx=50, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=400, height=400, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(200, 200, image=tomato_img)
canvas.create_text(200, 230, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

start_button = tkinter.Button(text="Start", font=(FONT_NAME, 15, "bold"))
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", font=(FONT_NAME, 15, "bold"))
reset_button.grid(column=2, row=2)

check_label = tkinter.Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
check_label.grid(column=1, row=2)


window.mainloop()