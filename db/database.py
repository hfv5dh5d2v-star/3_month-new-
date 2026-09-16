import sqlite3

from db.queries import CREATE_ANSWERS_TABLE, CREATE_QUESTIONS_TABLE, CREATE_TABLE

DATABASE = 'quez.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3 
    return conn 

def init_db():
    conn = get_db()
    conn.execute(CREATE_TABLE)
    conn.execute(CREATE_QUESTIONS_TABLE)
    conn.execute(CREATE_ANSWERS_TABLE)
    conn.commit()
    conn.close()
    
