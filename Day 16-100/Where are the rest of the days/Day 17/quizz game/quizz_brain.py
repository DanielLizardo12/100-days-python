class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.check_answer(input(f"Q.{self.question_number + 1} "
                       f"{self.question_list[self.question_number].text} "
                       f"(True/False): "),
                          self.question_list[self.question_number].answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got it")
            self.score += 1
        else:
            print("wrong")
        print(f"your current score is {self.score}/{len(self.question_list)}")
        print("\n")

    def final_score(self):
        print(f"You've completed the quizz, your final score was "
              f"{self.score}/{len(self.question_list)}")