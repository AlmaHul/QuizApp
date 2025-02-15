import html

class QuizBrain:
    """Hanterar logiken - håller reda på frågorna, användarens poäng,
    och säkerställer att quizet kan fortsätta tills alla frågor har besvarats. """
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"{self.question_number}: {q_text}"


    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False



class Question:
    """Definerar en frågeställning som tar två parametrar"""
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer