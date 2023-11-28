from question_model import Question
#from data import question_data
from quiz_brain import QuizBrain
from new_data import new_question_data
# import requests
question_bank = []

# for question in question_data:
#     new_question = Question(question["text"], question["answer"])
#     question_bank.append(new_question)

for question in new_question_data["results"]:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)
    print(new_question.text)
    print(new_question.answer)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_have_question():
    quiz_brain.next_question()
    quiz_brain.check_answer()



