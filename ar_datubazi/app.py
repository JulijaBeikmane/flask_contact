from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/iesniegt', methods = ['POST'])
def iesniegt():
    if request.method == 'POST':
        name = request.form.get('name')
        if name: 
            conn = sqlite3.connect('datubaze2.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO vardi (vards) VALUES (?)", (name,))
            conn.commit()
            conn.close()
        return redirect ('/')
@app.route('/iesniegtie')
def iesniegts():
    return render_template ('iesniegta_info.html')

if __name__ == "__main__":
    app.run(debug=True)