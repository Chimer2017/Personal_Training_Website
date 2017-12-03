from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Andrew's Personal Training Website"


if __name__ == "__main__":
    app.run(debug=True)
