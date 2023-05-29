import time
import tkinter as tk
import math

BG_COLOR = '#EDE9D5'
FONT_COLOR = '#617143'
BUTTON_COLOR = '#E7AB9A'
reps = 0
timer = None

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    global reps
    reps = 0

def start_timer():
    global reps
    reps += 1

    work_sec = 25 * 60
    short_break_sec = 5 * 60
    long_break_sec = 20 * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=FONT_COLOR)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=FONT_COLOR)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=FONT_COLOR)


def count_down(count):
    minutes = math.floor(count/60)
    seconds = count%60
    if seconds<10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text = f'{minutes}:{seconds}')

    if count>0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_sessions = math.floor(reps/2)


window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BG_COLOR)


title_label = tk.Label(text="Timer", fg=FONT_COLOR, bg=BG_COLOR, font=('Impact', 50))
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg=BG_COLOR, highlightthickness=0)
tomato_img = tk.PhotoImage(file='/Users/haniazwolinska/Desktop/100days_of_python/intermediate_level/pomodoro_app/tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=('Impact', 35, "bold"))
canvas.grid(column=1, row=1)

button1 = tk.Button(window, text='Start',  font=(
    'Impact', 15, 'bold'), bg=BUTTON_COLOR, fg=FONT_COLOR , borderwidth=0,highlightthickness=0, command= start_timer)  # command=''
button1.grid(row=3, column=0)

button2 = tk.Button(window, text='Reset', font=(
    'Impact', 15, 'bold'), bg=BUTTON_COLOR, fg=FONT_COLOR, relief='flat', borderwidth=0,highlightthickness=0, command=reset_timer)  # command=''
button2.grid(row=3, column=2)

window.mainloop()
