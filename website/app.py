from flask import Flask, render_template, request, url_for, redirect
import mimetypes

mimetypes.add_type('application/wasm', '.wasm')
app = Flask(__name__)
@app.after_request
def add_coop_coep_headers(response):
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    print("yo")
    if request.method == "GET":
        return render_template("index.html")

if __name__ == "__main__":
    app.run()