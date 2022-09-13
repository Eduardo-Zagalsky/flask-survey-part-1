from flask import Flask,request, redirect, render_template, flash , session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config["SECRET_KEY"] = "our-secret"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

objresponses = {}

@app.route("/")
def root_route():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template("satisfaction.html", title = title, instructions = instructions)

@app.route("/start")
def set_up():
    session["responses"]=[]
    return redirect("/questions/0")

@app.route("/questions/<int:q>")
def question(q):
    responses = session.get("responses")
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
    responses = session["responses"]
    objresponses[satisfaction_survey.questions[len(session["responses"])].question] = answer
    responses.append(answer)
    session["responses"] = responses    
    return redirect(f"/questions/{len(responses)}")

@app.route("/thankyou")
def completed():
    return render_template("completed.html",responses=objresponses)