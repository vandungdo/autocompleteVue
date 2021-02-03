from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    valueButton = "input text"
    valueInput = ""
    if request.method == "POST":
        valueInput = valueButton

    return render_template("first.html", valueButton=valueButton, valueInput=valueInput)


@app.route("/open_input", methods=["GET", "POST"])
def openInput():
    literals = ["Object1", "Object2", "Object3", "Object4"]
    value = ""
    input1 = ""
    input2 = ""
    if request.method == "POST":
        input1 = request.form["input1"]
        input2 = request.form["input2"]
    return render_template(
        "openInput.html",
        literals=literals,
        input1=input1,
        input2=input2,
        literalsJson=json.dumps(literals),
    )


if __name__ == "__main__":
    app.run(debug=True)