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
    
@app.route('/vardi')
def paradi_vardus():
    conn = sqlite3.connect('datubaze2.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, vards FROM vardi")
    vardi = cursor.fetchall()
    conn.close()
    return render_template ('vardi.html', vardi=vardi)

@app.route('/dzest/<int:id>')
def dzest_vardu(id):
    conn = sqlite3.connect('datubaze2.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM vardi WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect ('/vardi')

@app.route('/rediget/<int:id>', methods = ['GET', 'POST'])
def rediget_vardu(id):
    conn = sqlite3.connect('datubaze2.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        new_name = request.form.get('name')
        cursor.execute("UPDATE vardi SET vards=? WHERE id=?", (new_name, id))
        conn.commit()
        conn.close()
        return redirect ('/vardi')
    else:
        cursor.execute("SELECT vards FROM vardi WHERE id=?", (id,))
        vards = cursor.fetchone()
        conn.commit()
        conn.close()
        return render_template ('rediget.html', vards=vards, id=id)

if __name__ == "__main__":
    app.run(debug=True)