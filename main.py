from flask_validation import CreateGreetingForm
from flask import Flask, redirect, request, render_template
from flask.wrappers import Request  # import the Flask library and redirect function
from flask_logic import check_logic, create_logic
from werkzeug.wrappers.response import Response

app = Flask(__name__)  # Initialize Flask app object


@app.route("/")
def hello() -> str:
    return (
        "Create your greeting by POST /create_greeting"
        " with form contains from_greeting, to, title, content, date"
    )

@app.route("/create_greeting", methods=["POST"])
def create_greeting() -> str:
    form = CreateGreetingForm(request.form)
    if form.validate():
        greeting_id = create_logic()
        return str(greeting_id)
    return render_template("flask_validation_error.html", form=form)


@app.route("/check_greeting/<greeting_id>", methods=["GET"])
def check_greeting(greeting_id: int) -> Response:
    # check if greeting with id is ready
    print(f"Greeting id requested: {greeting_id}")
    greeting_location = check_logic(greeting_id)
    if greeting_location:
        return redirect(greeting_location)
    return Response("Not ready yet")


if __name__ == "__main__":
    app.run(debug=True, port=80)  # Run the app
