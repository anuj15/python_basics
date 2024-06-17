from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 3
timer = None
reps = 0
marks = ''


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, marks
    window.after_cancel(timer)
    timer_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(canvas_text, text='00:00')
    tick_label.config(text='')
    reps = 0
    marks = ''


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count = LONG_BREAK_MIN
        timer_label.config(text='Long Break', fg=RED)
    elif reps % 2 == 0:
        count = SHORT_BREAK_MIN
        timer_label.config(text='Short Break', fg=PINK)
    else:
        count = WORK_MIN
        timer_label.config(text='Timer', fg=GREEN)
    count_down(count)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(counter):
    global timer, reps, marks
    if counter >= 0:
        minutes = counter // 60
        seconds = counter % 60
        if minutes < 10:
            minutes = f'0{minutes}'
        if seconds < 10:
            seconds = f'0{seconds}'
        timer = window.after(1000, count_down, counter - 1)
        canvas.itemconfig(canvas_text, text=f'{minutes}:{seconds}')
    else:
        start_timer()
        if reps % 2 == 0:
            marks += '✔'
        tick_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(bg=YELLOW, padx=50, pady=50)

timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW)
timer_label.config(font=(FONT_NAME, 24, 'bold'))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=220, height=230, bg=YELLOW, highlightthickness=0)
my_image = PhotoImage(file='tomato.png')
canvas.create_image(110, 100, image=my_image)
canvas_text = canvas.create_text(110, 125, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(row=1, column=1)

start_button = Button(text='Start', border=0, bg='white', command=start_timer)
start_button.grid(row=2, column=0)

tick_label = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, 'bold'))
tick_label.grid(row=2, column=1)

reset_button = Button(text='Reset', border=0, bg='white', command=reset_timer)
reset_button.grid(row=2, column=3)

window.mainloop()
