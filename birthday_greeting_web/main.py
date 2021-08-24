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

@app.route("/create_greeting", methods=["GET"])
def create_greeting_page() -> str:
    return render_template("create_greeting.html")

@app.route("/create_greeting", methods=["POST"])
def create_greeting() -> str:
    form = CreateGreetingForm(request.form)
    if form.validate():
        greeting_id = create_logic({
            'from_greeting': form.from_greeting.data,
            'to': form.to.data,
            'title': form.title.data,
            'content': form.content.data,
            'date': form.date.data.strftime('%d/%M/%Y')
        })
        return greeting_id
    return render_template("flask_validation_error.html", form=form)


@app.route("/check_greeting/<greeting_id>", methods=["GET"])
def check_greeting(greeting_id: str) -> Response:
    # check if greeting with id is ready
    print(f"Greeting id requested: {greeting_id}")
    greeting_location = check_logic(greeting_id)
    if greeting_location:
        return redirect(greeting_location)
    return Response("Not ready yet")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)  # Run the app
