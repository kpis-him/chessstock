from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    print("yo")
    if request.method == "GET":
        return render_template("index.html")

if __name__ == "__main__":
    app.run()