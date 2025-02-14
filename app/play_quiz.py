from app.quiz_data import question_data, create_question_bank
from app.quiz_brain import QuizBrain
from app.quiz_interface import QuizInterface

def start_quiz():
    """Startar, kör och avslutar quizet."""
    question_bank = create_question_bank(question_data) #Skapa frågebank
    quiz = QuizBrain(question_bank) #Skapar en instans
    quiz_ui = QuizInterface(quiz) #Skapa ett användargränssnitt för quizet

    quiz_ui.start()

    if quiz.question_number < 10:
        print("Du har avslutat frågesporten")
        print(f"Ditt slutresultat var: {quiz.score}/{quiz.question_number}")
    else:
        print("Du har slutfört frågesporten")
        print(f"Ditt slutresultat var: {quiz.score}/{quiz.question_number}")
