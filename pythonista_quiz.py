from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]

for question_items in question_data:
    question=Question(question_items["text"],question_items["answer"])
    question_bank.append(question)

quiz_brain=QuizBrain(question_bank)

while quiz_brain.still_has_question():
    user_response=quiz_brain.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz_brain.score}/{quiz_brain.question_id}\n")
