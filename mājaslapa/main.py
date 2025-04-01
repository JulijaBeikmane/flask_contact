from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def sakums():

    return render_template("index.html")


@app.route('/forma', methods=["GET", "POST"])
def forma():
    if request.method == "POST":
        name = request.form.get('name')
        epasts = request.form.get('email')
        return render_template('layout.html', iesniegt=True, name=name, email=epasts)
    else:
        return render_template('layout.html', iesniegt=False)

 

@app.route('/atteli')
def atteli():
    return render_template("atteli.html")

if __name__ == "__main__":
    app.run(debug=True)