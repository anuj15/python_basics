import html


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return len(self.question_list) != self.question_number

    def next_question(self):
        q_text = html.unescape(self.question_list[self.question_number].text)
        self.question_number += 1
        return f'Q.{self.question_number} {q_text}'

    def check_answer(self, user_answer):
        correct_answer = self.question_list[self.question_number].answer
        if correct_answer == user_answer:
            self.score += 1
            return True
        else:
            return False
