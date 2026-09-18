import sqlite3

from src.questions import INITAL_QUESTIONS
from db.queries import CREATE_ANSWERS_TABLE, CREATE_QUESTIONS_TABLE, CREATE_TABLE, GET_ALL_QUESTIONS, INSERT_QUESTION
DATABASE = 'open.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn 

def init_db():
    conn = get_db()
    conn.execute(CREATE_TABLE)
    conn.execute(CREATE_QUESTIONS_TABLE)
    conn.execute(CREATE_ANSWERS_TABLE)

    if not conn.execute(GET_ALL_QUESTIONS).fetchall():
        for q_text, q_answer in INITAL_QUESTIONS:
            conn.execute(INSERT_QUESTION, (q_text, q_answer))
        conn.commit()

    conn.close()
    
