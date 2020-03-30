from flask import Flask


app = Flask(__name__)
times = 0


@app.route('/')
def hello():
    global times
    times += 1
    return 'Hello TEAM this has been viewed  time(s). ' + str(times)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)