from flask import Flask,request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config["SECRET_KEY"] = "our-secret"
debug = DebugToolbarExtension(app)

responses = []

@app.route("/")
def root_route():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template("satisfaction.html", title = title, instructions = instructions)

@app.route("/questions/<int:q>")
def question(q):
    question = satisfaction_survey.questions[q]
    return render_template("question.html", question = question, number = q)

@app.route("/answer", methods=["POST"])
def answers():
    answer = request.form.get("answer")
    responses.append(answer)
    return redirect(f"/questions/{len(responses)}")