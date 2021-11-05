import time

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def serve():
    return render_template("index.html", time=time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime()))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
