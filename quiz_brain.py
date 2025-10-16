class QuizBrain:
    def __init__(self, q_list):
        self.q_num = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.q_num < len(self.q_list)  # Use < to avoid IndexError

    def next_question(self):
        current_q = self.q_list[self.q_num]
        self.q_num += 1
        user = input(f"{self.q_num}: {current_q.question} - (True/False) ")
        self.check_answer(user, current_q.correct_answer)

    def check_answer(self, user, correct_answer):
        if user.lower() == correct_answer.lower():
            self.score += 1
            print("Well done!")
        else:
            print("Nope!")
        print(f"Your score is {self.score}/{self.q_num}\n")
