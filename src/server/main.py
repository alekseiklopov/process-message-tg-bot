from flask import Flask, request

app = Flask(__name__)


@app.route("api/test")
def test():
    return "Test success\n"


if __name__ == "__main__":
    app.run(port=4000, host="0.0.0.0", debug=False)

