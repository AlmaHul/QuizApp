import requests
from quiz_brain import Question


#Definiera parametrar för API-förfrågan
parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]


def create_question_bank(question_data):
    """Skapa en frågebank från API-datan"""
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    return question_bank