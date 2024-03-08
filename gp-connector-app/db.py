import sqlite3

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('gp_connector.db')
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def setup_db():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL,
                        role TEXT NOT NULL
                      );""")
    conn.commit()
    conn.close()

setup_db()