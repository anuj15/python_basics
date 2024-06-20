from data import question_data
from quiz_brain import QuizBrain
from quiz_model import Question
from ui import QuizInterface

question_bank = []

for question in question_data:
    q_text = question['question']
    q_answer = question['correct_answer']
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

q_brain = QuizBrain(question_bank)
quiz_ui = QuizInterface(q_brain)

for _ in question_bank:
    q_brain.next_question()
print(f'Your final score is: {q_brain.score}/{q_brain.question_number}')
