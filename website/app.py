from flask import Flask, render_template, request, url_for, redirect
import mimetypes
from google import genai
import markdown
from bs4 import BeautifulSoup
import re
import spotipy


mimetypes.add_type('application/wasm', '.wasm')
app = Flask(__name__)
client = genai.Client(api_key="AIzaSyBbmk-ZMKpywSb_GMCBtjkiGamltst9k2Q")
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
              clean_pgn = re.sub(r"\[.*?\]", "", pgn)
              clean_pgn = clean_pgn.strip()
              color = request.form.get("color")
              elo = request.form.get("elo")
              response = client.models.generate_content(
                model="gemini-2.0-flash", 
                contents=f"Analyze this game, i'm {color}, the pgn is {pgn}, my opponent's elo is about {elo}, give me my 'chess personality type' and some evid for it, make it encouraging"
                )
              text = response.candidates[0].content.parts[0].text
              text1 = BeautifulSoup(text, "html.parser").get_text()
              pgn1 = clean_pgn
              print(pgn1)
              response = markdown.markdown(text1)
              return render_template("analyzed.html", response=response, pgn=pgn1)

        
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
        if request.method == "POST":
               aggressive = 0
               calculator = 0
               tactical = 0
               random = 0
               name = request.form.get("name")
               pressure = request.form.get("pressure")
               if pressure == "loveit":
                    aggressive +=1
                    calculator += 0.5
                    tactical +=1
                    random+=1
               if pressure == "calm":
                    aggressive +=1
                    calculator +=1
                    tactical += 1
                    random+=0
               if pressure == "panic":
                    aggressive +=0
                    calculator +=0
                    tactical += 0
                    random += 1
               if pressure == "avoid":
                    aggressive +=0
                    calculator +=1
                    tactical += 0
                    random+=1
               personality = request.form.get("personality")
               if personality == "aggressive":
                    aggressive+=1
                    calculator+=0.5 
                    tactical+=0.5
                    random+=1
               if personality == "tactics":
                    aggressive+=0.0
                    calculator+=1 
                    tactical+=1
                    random+=0.0
               if personality == "sneaky":
                    aggressive+=0.5
                    calculator+=1
                    tactical+=1
                    random+=0
               if personality == "random":
                    aggressive+=1
                    calculator+=0
                    tactical+=0
                    random+=1
               traits = request.form.get("traits")
               if traits == "attack":
                    aggressive += 1
                    calculator += 0.5
                    tactical +=1
                    random+=1
               if traits == "develop":
                    aggressive+=0.5
                    calculator+=1
                    tactical+=1
                    random+=0
               if traits == "positional":
                    aggressive += 0
                    calculator += 1
                    tactical +=1
                    random+=0
               if traits == "random":
                    aggressive+=1
                    calculator+=0
                    tactical+=0
                    random+=1
               sac = request.form.get("sac")
               if sac == "volunteering":
                    aggressive += 1
                    calculator += 0.5
                    tactical +=0
                    random+=1
               if sac == "loved":
                    aggressive+=0.5
                    calculator+=1
                    tactical+=1
                    random+=0
               if sac == "drinking":
                    aggressive += 0
                    calculator += 1
                    tactical +=1.5
                    random+=0.5
               if sac == "random":
                    aggressive+=1
                    calculator+=0
                    tactical+=0
                    random+=1.5
               think = request.form.get("think")
               if think == "gut":
                    aggressive += 1
                    calculator += 0
                    tactical +=0
                    random+=1
               if think == "calculate":
                    aggressive+=0.5
                    calculator+=1
                    tactical+=1
                    random+=0
               if think == "scenario":
                    aggressive += 0.5
                    calculator += 0.5
                    tactical +=0.5
                    random+=1
               if think == "hope":
                    aggressive+=1
                    calculator+=0
                    tactical+=0
                    random+=1
               leader = request.form.get("leader")
               if leader == "queen":
                    aggressive += 1
                    calculator += 0.5
                    tactical +=0
                    random+=1
               if leader == "knight":
                    aggressive+=0.5
                    calculator+=1
                    tactical+=1
                    random+=0
               if leader == "bishop":
                    aggressive += 0.5
                    calculator += 1
                    tactical +=1
                    random+=0
               if leader == "pawn":
                    aggressive+=0.5
                    calculator+=0.5
                    tactical+=0.5
                    random+=1
               approach = request.form.get("approach")
               if approach == "dominate":
                    aggressive += 1
                    calculator += 0.5
                    tactical +=0
                    random+=0
               if approach == "slowly":
                    aggressive+=0
                    calculator+=1
                    tactical+=1
                    random+=0
               if approach == "wait":
                    aggressive += 0
                    calculator += 1
                    tactical +=1
                    random+=0
               if approach == "surprise":
                    aggressive+=0.5
                    calculator+=0.0
                    tactical+=0.5
                    random+=1
               elo = request.form.get("elo")
               variables = {"aggressor": aggressive, "calculative": calculator, "tactical": tactical, "wild-type":random}
               songs = {"aggressor": "hip-hop", "calculative": calculator, "tactical": tactical, "wild-type":random}
               winner = max(variables, key=variables.get)
               print(winner)
               response1 = client.models.generate_content(
                    model="gemini-2.0-flash", 
                    contents=f"{name}'s chess persona type is {winner} and my elo is {elo}, give me my strengths,weaknesses and famous comp based on my persona, make it buzzfeed description, short and sweet"
               )
               text = response1.candidates[0].content.parts[0].text

               text1 = BeautifulSoup(text, "html.parser").get_text()
               print(text1)
               response = markdown.markdown(text1)
               return render_template("bot.html", winner=winner, response=response, name=name, elo=elo)


if __name__ == "__main__":
    app.run()