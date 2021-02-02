from flask import Flask, render_template, request

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
    literal = "Object"
    value = ""
    input1 = ""
    input2 = ""
    if request.method == "POST":
        value = literal
        input1 = request.form["input1"]
        input2 = request.form["input2"]
    return render_template(
        "openInput.html", literal=literal, value=value, input1=input1, input2=input2
    )


if __name__ == "__main__":
    app.run(debug=True)