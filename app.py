from flask import Flask, render_template, jsonify, request
from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

app = Flask(__name__)

# Build question bank
question_bank = [Question(q["question"], q["correct_answer"]) for q in question_data]
quiz = QuizBrain(question_bank)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/next_question")
def next_question():
    if quiz.still_has_questions():
        current_q = quiz.q_list[quiz.q_num]
        return jsonify({
            "question": current_q.question,
            "score": quiz.score,
            "q_num": quiz.q_num + 1
        })
    else:
        return jsonify({"question": "Quiz Finished!", "score": quiz.score, "finished": True})


@app.route("/answer", methods=["POST"])
def answer():
    data = request.json
    user_answer = data["answer"]
    current_q = quiz.q_list[quiz.q_num]

    # Check answer and send feedback message
    if user_answer.lower() == current_q.correct_answer.lower():
        quiz.score += 1
        result_msg = "Well done! ✅"
    else:
        result_msg = "Nope! ❌"

    quiz.q_num += 1
    return jsonify({"score": quiz.score, "message": result_msg})


if __name__ == "__main__":
    app.run(debug=True)
