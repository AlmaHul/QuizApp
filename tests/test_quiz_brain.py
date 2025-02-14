from app.quiz_brain import QuizBrain, Question

# Testa frågeklassen
def test_question():
    q = Question("Vad är Sveriges huvudstad?", "Stockholm")
    assert q.text == "Vad är Sveriges huvudstad?"
    assert q.answer == "Stockholm"

# Testa funktionen för om det fortfarande finns frågor
def test_still_has_questions():
    q1 = Question("Vad är 1+2?", "3")
    q2 = Question("Vad säger kon?", "Mu")
    quiz = QuizBrain([q1, q2])

    assert quiz.still_has_questions() is True

    quiz.next_question()  # Svarat på en fråga
    assert quiz.still_has_questions() is True

    quiz.next_question()  # Svarat på två frågor
    assert quiz.still_has_questions() is False

# Testa metoden för nästa fråga
def test_next_question():
    q1 = Question("Vad är 2 + 2?", "4")
    q2 = Question("Vad är Sveriges huvudstad?", "Stockholm")
    quiz = QuizBrain([q1, q2])

    assert quiz.next_question() == "1: Vad är 2 + 2?"
    assert quiz.next_question() == "2: Vad är Sveriges huvudstad?"

# Testa metoden för rätt svar
def test_check_answer():
    q1 = Question("Vad är 5 + 5?", "4")
    q2 = Question("Vad är Sveriges huvudstad?", "Stockholm")
    quiz = QuizBrain([q1, q2])

    quiz.next_question()
    assert quiz.check_answer("4") is True
    assert quiz.score == 1

    quiz.next_question()
    assert quiz.check_answer("London") is False
    assert quiz.score == 1