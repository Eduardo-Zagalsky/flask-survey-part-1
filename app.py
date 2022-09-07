from flask import Flask,request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config["SECRET_KEY"] = "our-secret"
debug = DebugToolbarExtension(app)

responses = []
objresponses = {}

@app.route("/")
def root_route():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template("satisfaction.html", title = title, instructions = instructions)

@app.route("/questions/<int:q>")
def question(q):
    if len(responses) == len(satisfaction_survey.questions):
        return redirect("/thankyou")
    if len(responses) != q:
        flash(f"{q} is not the next sequential question")
        return redirect(f"/questions/{len(responses)}")
    question = satisfaction_survey.questions[q]
    return render_template("question.html", question = question, number = q)

@app.route("/answer", methods=["POST"])
def answers():
    answer = request.form.get("answer")
    objresponses[satisfaction_survey.questions[len(responses)].question] = answer
    responses.append(answer)
    return redirect(f"/questions/{len(responses)}")

@app.route("/thankyou")
def completed():
    return render_template("completed.html",responses=objresponses)