from db.database import get_db
from db.queries import GET_USER_BY_TG_ID, INSERT_USER, GET_ALL_USERS, DELETE_USER


def get_user(telegram_id: int):
    conn = get_db()
    user = conn.execute(GET_USER_BY_TG_ID, (telegram_id,)).fetchone()
    conn.close()
    return dict(user) if user else None

def create_user(username: str, telegram_id: int):
    conn = get_db()
    conn.execute(INSERT_USER, (username, telegram_id))
    conn.commit()
    conn.close()
    return get_user(telegram_id)

def get_all_users():
    conn = get_db()
    users = conn.execute(GET_ALL_USERS).fetchall()
    conn.close()
    return [dict(row) for row in users]

def delete_user(telegram_id: int):
    conn = get_db()
    conn.execute(DELETE_USER, (telegram_id,))
    conn.commit()
    conn.close()


