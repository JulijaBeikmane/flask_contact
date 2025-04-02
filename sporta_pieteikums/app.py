from flask import Flask, render_template, request

app = Flask(__name__)

#izveido globālo mainūgo, kas satur sporta veidus
SPORTS = ['basketbols', 'futbols', 'hokejs', 'teniss', 'volejbols']
REGISTRETIE = {}

@app.route("/")
def index():
    return render_template('index.html', disciplina=SPORTS)

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    if not name:
        return render_template ('kluda.html', zina='Lūdzu, ievadi vārdu!')
    sport = request.form.get('sports')
    if not sport:
        return render_template ('kluda.html', zina='Lūdzu, ievadi sportu!')
    # if not request.form.get('name') or not name or request.form.get('sports') or request.form.get('sports') not in SPORTS:
    #     return render_template('kluda.html')
    if sport not in SPORTS:
        return render_template ('kluda.html', zina='Nav pieejams šāds sports veids')
    
    REGISTRETIE[name] = sport
    return render_template('apstiprinats.html')

@app.route('/registretie')
def registretie():
    return render_template ('registretie.html', registretie=REGISTRETIE)

if __name__ == "__main__":
    app.run(debug=True)