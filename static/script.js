let currentQuestionNum = 0;

function loadQuestion() {
    fetch("/next_question")
    .then(res => res.json())
    .then(data => {
        if (data.finished) {
            document.getElementById("question").innerText = data.question;
            document.getElementById("true-btn").disabled = true;
            document.getElementById("false-btn").disabled = true;
            document.getElementById("score").innerText = `Final Score: ${data.score}`;
        } else {
            document.getElementById("question").innerText = data.question;
            document.getElementById("score").innerText = `Score: ${data.score}`;
            currentQuestionNum = data.q_num;
        }
    });
}

function sendAnswer(answer) {
    fetch("/answer", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({answer: answer})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("score").innerText = `Score: ${data.score}`;
        document.getElementById("feedback").innerText = data.message; // show feedback

        // Load next question after 1 second
        setTimeout(() => {
            document.getElementById("feedback").innerText = "";
            loadQuestion();
        }, 1000);
    });
}

// Button listeners
document.getElementById("true-btn").addEventListener("click", () => sendAnswer("True"));
document.getElementById("false-btn").addEventListener("click", () => sendAnswer("False"));

// Initial load
loadQuestion();
