class QuizBrain:

    def __init__(self,question_list):
        self.question_id = 0
        self.score=0
        self.question_list = question_list


    def next_question(self):
        self.question_id += 1
        user_question= self.question_list[self.question_id-1]
        user_choice = input(f"Q.{self.question_id}: {user_question.question} (True/False)?: ").title()
        return self.check_answer(user_choice, user_question)


    def still_has_question(self):
        return self.question_id < len(self.question_list)

    def check_answer(self,user_answer, user_question):
        if user_answer  == user_question.answer:
            print("You got it right!")
            print("The correct answer was: " + user_question.answer)
            self.score+=1
            print(f"Your current score is: {self.score}/{self.question_id}\n")
        else:
            print("You got it wrong!")
            print("The correct answer was: " + user_question.answer)
            print(f"Your current score is: {self.score}/{self.question_id}\n")
