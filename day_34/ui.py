from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.quiz_brain = quiz_brain
        true_image = PhotoImage(file='images/true.png')
        false_image = PhotoImage(file='images/false.png')
        self.score = Label(text='Score: 0', bg=THEME_COLOR, fg='white', font=('Arial', 12, 'normal'))
        self.score.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150, 125,
            text='sample text. ',
            width=280,
            font=('Arial', 18, 'italic'),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=50, pady=50)
        self.true_button = Button(image=true_image, border=0, highlightthickness=0, command=self.true_button)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_image, border=0, highlightthickness=0, command=self.false_button)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz_brain.still_has_questions():
            self.score.config(text=f'Score: {self.quiz_brain.score}')
            next_question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=next_question)
        else:
            self.canvas.itemconfig(self.question_text, text='You\'ve reached the end of the quiz')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_button(self):
        is_right = self.quiz_brain.check_answer('True')
        self.get_feedback(is_right)

    def false_button(self):
        is_right = self.quiz_brain.check_answer('False')
        self.get_feedback(is_right)

    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
