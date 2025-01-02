import os
import sqlite3


class Database():
    
    def __init__(self, db_base_path: str = os.getenv('HOME'), db_folder: str = '.kowalski', db_name: str = 'notes.db'):
        self.db_parent_path = os.path.join(db_base_path, db_folder)
        self.db_path = os.path.join(db_base_path, db_folder, db_name)
        if not os.path.exists(self.db_path):
            self._initialize()

    def _initialize(self):
        os.makedirs(self.db_parent_path, exist_ok=True)
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    name TEXT PRIMARY KEY NOT NULL,
                    notes_count INT NOT NULL
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    book TEXT NOT NULL,
                    date TEXT NOT NULL,
                    media TEXT NOT NULL,
                    source TEXT,
                    content TEXT NOT NULL
                )
            """)
            conn.commit()

    def insert_note(self, book: str, date: str, media: str, source: str, content: str):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO books (name, notes_count) VALUES (?, 1) ON CONFLICT(name) DO UPDATE SET notes_count = notes_count + 1", (book,))
            cursor.execute("INSERT INTO notes (book, date, media, source, content) VALUES (?,?,?,?,?)", (book, date, media, source, content,))
            conn.commit()

    def update_note(self, id: str, date: str, content: str):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE notes SET date = ?, content = ? WHERE id = ?""", (date, content, id))
            conn.commit()

    def list_books(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books ORDER BY notes_count DESC")
            return cursor.fetchall()
        
    def list_notes(self, book: str, limit: int):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM notes WHERE book = '{book}' ORDER BY date DESC LIMIT {limit}")
            return cursor.fetchall()
        
    def find_note(self, keywords: str, book: str):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            if book is None:
                cursor.execute(f"""
                    SELECT
                        *
                    FROM notes
                    WHERE 1=1
                        AND content LIKE '%{keywords}%'
                    ORDER BY date DESC
                """)
            else:
                cursor.execute(f"""
                    SELECT
                        *
                    FROM notes
                    WHERE 1=1
                        AND book = '{book}'
                        AND content LIKE '%{keywords}%'
                    ORDER BY date DESC
                """)
            return cursor.fetchall()
        
    def view_note(self, id: str):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM notes WHERE id = '{id}'")
            return cursor.fetchone()
        
    def get_recent_notes(self, hours: int):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM notes WHERE datetime(date) >= datetime('now', 'localtime', '-{hours} hours')")
            return cursor.fetchall()
            