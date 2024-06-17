from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 3
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text='00:00')
    timer_label.config(text='Timer', fg=GREEN)
    tick_label.config(text='')


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
def count_down(count_):
    global timer
    minutes = count_ // 60
    seconds = count_ % 60
    if minutes < 10:
        minutes = f'0{minutes}'
    if seconds < 10:
        seconds = f'0{seconds}'
    display_time = f'{minutes}:{seconds}'
    if reps > 0:
        if count_ >= 0:
            canvas.itemconfig(canvas_text, text=display_time)
            timer = window.after(1000, count_down, count_ - 1)
        else:
            start_timer()
            marks = ''
            for _ in range(reps // 2):
                marks += '✔'
                tick_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(bg=YELLOW, padx=100, pady=50)

canvas = Canvas(width=220, height=230, bg=YELLOW, highlightthickness=0)
my_image = PhotoImage(file='tomato.png')
canvas.create_image(110, 100, image=my_image)
canvas_text = canvas.create_text(110, 125, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(row=1, column=1)

timer_label = Label(text='Timer', font=(FONT_NAME, 32, 'bold'), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

start_button = Button(text='Start', border=0, bg='white', command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', border=0, bg='white', command=reset_timer)
reset_button.grid(row=2, column=2)

tick_label = Label(text='', bg=YELLOW, fg=GREEN)
tick_label.grid(row=3, column=1)

window.mainloop()
