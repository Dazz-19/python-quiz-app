from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for q in question_data:
    q=Question(q["question"],q["correct_answer"])
    question_bank.append(q)

quiz=QuizBrain(question_bank)
try:
 while quiz.still_has_questions():
        quiz.next_question()
except IndexError:
    print(f"done with quiz !! your final score was {quiz.score}")



