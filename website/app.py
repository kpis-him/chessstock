from flask import Flask, render_template, request, url_for, redirect
import mimetypes
from openai import OpenAI

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
    
@app.route("/analyze", methods=["GET", "POST"])
def analyze():
        print("analyzing")
        if request.method == "GET":
             return render_template("analysis.html")
        
@app.route("/chess", methods=["GET", "POST"])
def chess():
        print("chess")
        if request.method == "GET":
             return render_template("chess.html")
        
@app.route("/myopuzzle", methods=["GET", "POST"])
def myopuzzle():
        print("makingyourownpuzzle")
        if request.method == "GET":
             return render_template("myopuzzle.html")
        
@app.route("/pubpuzzles", methods=["GET", "POST"])
def pubpuzzles():
        print("public")
        if request.method == "GET":
             return render_template("pubpuzzles.html")

if __name__ == "__main__":
    app.run()