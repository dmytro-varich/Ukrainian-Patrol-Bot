import sqlite3 as sq

async def create_storage():
    try:
        global db, cur
        db = sq.connect('databases/words_storage.db')
        cur = db.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS allowed_words (
                        id INTEGER PRIMARY KEY,
                        chat_id INTEGER,
                        word TEXT, 
                        FOREIGN KEY (chat_id) REFERENCES group_filter_states (chat_id)   
                        )''')

        db.commit()

        return db, cur

    except Exception as e:
        print(f"Error initializing database: {e}")
        return None, None


async def add_allowed_words(chat_id: int, words: list) -> None:
    get_words = await get_allowed_words(chat_id)
    for word in words:
        if word not in get_words:
            cur.execute('INSERT OR IGNORE INTO allowed_words (chat_id, word) VALUES (?, ?)', 
                        (chat_id, word.lower()))    
    db.commit()


async def get_allowed_words(chat_id: int) -> list:
    cur.execute('SELECT word FROM allowed_words WHERE chat_id = ?', (chat_id,))
    words = [row[0] for row in cur.fetchall()]
    return words


async def delete_allowed_words(chat_id: int, word: str) -> None:
    cur.execute('DELETE FROM allowed_words WHERE chat_id = ? AND word = ?', (chat_id, word))
    db.commit()