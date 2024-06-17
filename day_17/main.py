from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for d in question_data:
    question_bank.append(Question(d['text'], d['answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f'You\'ve completed the Quiz!\nYour final score is: {quiz.score}/{quiz.question_number}')
