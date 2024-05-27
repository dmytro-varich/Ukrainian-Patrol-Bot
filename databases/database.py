import sqlite3 as sq

async def create_db():
    try:
        global db, cur
        db = sq.connect('databases/database.db')
        cur = db.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS group_filter_states (
                        chat_id INTEGER PRIMARY KEY,
                        filter_states BOOL , 
                        last_active_keyboard_id TEXT, 
                        swear_state_control BOOL 
                        )''')

        db.commit()

        return db, cur

    except Exception as e:
        print(f"Error initializing database: {e}")
        return None, None


async def update_filter_state(chat_id: int, state: bool, attribute: str) -> None:
    cur.execute(f'INSERT OR REPLACE INTO group_filter_states (chat_id, {attribute}) VALUES (?, ?)', (chat_id, state))
    db.commit()


async def check_filter_state(chat_id: int, attribute: str) -> bool:
    cur.execute(f'SELECT {attribute} FROM group_filter_states WHERE chat_id = ?', (chat_id,))
    
    result = cur.fetchone()
    
    if result:
        return bool(result[0])  
    else:
        await update_filter_state(chat_id, False, attribute)
        return False
    

async def set_last_active_keyboard_id(chat_id: int, last_active_keyboard_id: str = None) -> None:
    cur.execute('INSERT OR REPLACE INTO group_filter_states (chat_id, last_active_keyboard_id) VALUES (?, ?)',
                   (chat_id, last_active_keyboard_id))
    db.commit()


async def get_last_active_keyboard_id(chat_id: int) -> str:
    cur.execute('SELECT last_active_keyboard_id FROM group_filter_states WHERE chat_id = ?', (chat_id,))
    result = cur.fetchone()[0]
    return result