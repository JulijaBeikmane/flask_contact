import sqlite3

def veido_datubazi():
    conn = sqlite3.connect("datubaze2.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vardi (
                   id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   vards TEXT)''')
    conn.commit()
    conn.close()


if __name__ == "__main__":
    veido_datubazi()