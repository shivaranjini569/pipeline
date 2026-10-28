from flask import Flask, render_template, request

app = Flask(__name__)

OPERATIONS = {
    "add": "Addition",
    "subtract": "Subtraction",
}


def calculate(a, b, operation):
    if operation == "add":
        return a + b
    if operation == "subtract":
        return a - b
    raise ValueError("Invalid operation")


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None
    if request.method == "POST":
        try:
            a = float(request.form.get("a", ""))
            b = float(request.form.get("b", ""))
            operation = request.form.get("operation", "")
            result = calculate(a, b, operation)
        except (ValueError, TypeError):
            error = "Enter valid numbers and select an available operation."
    return render_template(
        "index.html", operations=OPERATIONS, result=result, error=error
    )


@app.get("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)