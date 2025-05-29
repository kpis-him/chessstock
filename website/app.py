from flask import Flask, render_template, request, url_for, redirect
import mimetypes
from google import genai

mimetypes.add_type('application/wasm', '.wasm')
app = Flask(__name__)
client = genai.Client(api_key="AIzaSyCia1tPbcRDufrRr5a1J-b1ZTQaeWEh4SI")
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
        if request.method == "POST":
              pgn = request.form.get("pgn")
              color = request.form.get("color")
              elo = request.form.get("elo")
              response = client.models.generate_content(
                model="gemini-2.0-flash", 
                contents=f"Analyze this game, i'm {color}, the pgn is {pgn}, my opponent's elo is about {elo}, give me my 'chess personality type' and some evid for it, make it plain text"
                )
              alpha = response.text
              return render_template("analyzed.html", response=alpha, pgn=pgn)

        
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
        if request.method == "POST":
             return render_template("myopuzzle.html")   
        
@app.route("/pubpuzzles", methods=["GET", "POST"])
def pubpuzzles():
        print("public")
        if request.method == "GET":
             return render_template("pubpuzzles.html")

if __name__ == "__main__":
    app.run()