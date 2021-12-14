
# ---------------------------- CONSTANTS ------------------------------- #
import time
from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps = 0
timer = None
check_text = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(text_canvas, text="00:00")
    check_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(60*LONG_BREAK_MIN)
        timer_label.config(text="20min break", fg=PINK)
    elif reps % 2 == 0:
        count_down(60*SHORT_BREAK_MIN)
        timer_label.config(text="5min break", fg=RED)
    else:
        count_down(60*WORK_MIN)
        timer_label.config(text="Work!", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(timer_in):
    # print(f"timer_in : {timer_in}")
    timer_min = math.floor(timer_in / 60)
    # print(f"timer_min : {timer_min}")
    if timer_min < 10:
        timer_min = "0" + str(timer_min)
    timer_sec = int(timer_in % 60)
    if timer_sec < 10:
        timer_sec = "0" + str(timer_sec)
    canvas.itemconfig(text_canvas, text=f"{timer_min}:{timer_sec}")

    if timer_in > 0:
        global timer
        timer = window.after(1000, count_down, timer_in - 1)
    else:
        start_timer()
        global reps
        checks = ""
        sessions = math.floor(reps/2)
        for i in range(sessions):
            checks += "✔"
        check_label.config(text=checks)



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato)
text_canvas = canvas.create_text(100,140, text="00:00", font=(FONT_NAME, 24, "bold"), fill="white")
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 12, "normal"), command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)


reset_button = Button(text="Reset", font=(FONT_NAME, 12, "normal"),command=reset, highlightthickness=0)
reset_button.grid(row=2, column=2)

check_label = Label(font=(FONT_NAME, 12, "normal"), fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

window.mainloop()


