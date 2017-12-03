from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    for i in range(0,100):
        print "Workout"
    return "Andrew's Personal Training Website"


if __name__ == "__main__":
    app.run(debug=True)
