import tkinter
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 5
reps = 0
work_rep_list = [1,3,5,7]
short_break_list = [2,4,6]

def start_timer():
    global reps
    reps += 1
    print(reps)

    if reps in work_rep_list:
        title_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN)
    elif reps in short_break_list:
        title_label.config(text="short Work", fg=PINK)
        count_down(SHORT_BREAK_MIN)
    elif reps == 8:
        title_label.config(text="long Work", fg=RED)
        count_down(LONG_BREAK_MIN)

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=400, height=400, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(200, 200, image=tomato_img)
timer_text = canvas.create_text(200, 230, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

start_button = tkinter.Button(text="Start", font=(FONT_NAME, 15, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", font=(FONT_NAME, 15, "bold"))
reset_button.grid(column=2, row=2)

check_label = tkinter.Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
check_label.grid(column=1, row=2)


window.mainloop()