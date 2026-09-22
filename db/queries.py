CREATE_TABLE = '''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    telegram_id INTEGER NOT NULL UNIQUE
    )'''

CREATE_QUESTIONS_TABLE = '''CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_text TEXT NOT NULL,
    correct_answer TEXT NOT NULL
    )'''
CREATE_ANSWERS_TABLE = '''
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        question_id INTEGER NOT NULL,
        is_correct BOOLEAN NOT NULL DEFAULT 0,

        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
    )
'''


GET_USER_BY_TG_ID = 'SELECT * FROM users WHERE telegram_id = ?'
INSERT_USER = 'INSERT OR IGNORE INTO users(username, telegram_id) VALUES (?, ?)'
UPDATE_USER_USERNAME = 'UPDATE users SET username = ? WHERE telegram_id = ?'
DELETE_USER = 'DELETE FROM users WHERE telegram_id = ?'
GET_ALL_USERS = 'SELECT * FROM users'

GET_USER_BY_TG_ID = 'SELECT * FROM users WHERE telegram_id = ?'

INSERT_USER = 'INSERT OR IGNORE INTO users (username, telegram_id) VALUES (?, ?)'

UPDATE_USER_USERNAME = 'UPDATE users SET username = ? WHERE telegram_id = ?'

DELETE_USER = 'DELETE FROM users WHERE telegram_id = ?'



GET_ALL_QUESTIONS = 'SELECT * FROM questions'

GET_QUESTION_BY_ID = 'SELECT * FROM questions WHERE id = ?'

INSERT_QUESTION = 'INSERT INTO questions (question_text, correct_answer) VALUES (?, ?)'



INSERT_RESULT = """
    INSERT INTO results(user_id, question_id, is_correct) VALUES (?, ?, ?)
"""

GET_SCORE_BY_USER_ID = """
    SELECT COUNT(*) AS total, 
    SUM(is_correct) AS correct

    FROM results
    WHERE user_id = ?
"""

GET_HISTORY = '''
    SELECT q.question_text, r.is_correct
    FROM results AS r

    INNER JOIN users AS u
        ON r.user_id = u.id

    INNER JOIN questions AS q
            ON r.question_id = q.id

    WHERE u.telegram_id = ?
    ORDER BY r.id DESC
    LIMIT 5
'''

GET_TOP = '''
    SELECT u.username,
           COUNT(*) AS total,
           SUM(r.is_correct) AS correct
    FROM results AS r

    INNER JOIN users AS u
    ON r.user_id = u.id
    GROUP BY r.user_id
    ORDER BY correct DESC
    LIMIT ?
'''

GET_HARDEST = '''
    SELECT q.question_text,
           ROUND(AVG(r.is_correct) * 100, 1) AS success_rate
    FROM results AS r
    INNER JOIN questions AS q
    ON r.question_id = q.id
    GROUP BY r.question_id
    ORDER BY success_rate ASC
    LIMIT 1
'''