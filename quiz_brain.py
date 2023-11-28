class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.answer = ""
    def still_have_question(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        print("\n")
        self.answer = input(f'''Q{self.question_number+1}: {self.question_list[self.question_number].text} true or false''')
        self.question_number += 1

    def check_answer(self):
        if self.question_list[self.question_number-1].answer.lower() == self.answer.lower():
            print("you got it right!!")
            self.score += 1
            print(f"Your current score is {self.score}/{self.question_number}")
        else:
            print("That's wrong! :(")
            print(f"Your current score is {self.score}/{self.question_number}")
