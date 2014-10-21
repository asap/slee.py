import time

from flask import Flask
app = Flask(__name__)

@app.route("/sleep/<timeout>")
def sleep(timeout):

    if not timeout:
        timeout = 5

    time.sleep(int(timeout))

    return "z" * int(timeout)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)