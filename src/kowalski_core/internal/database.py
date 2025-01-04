import os
import sqlite3

from kowalski_core.internal.note import Note


class Database():

    NAME = "notes.db"

    def __init__(self):
        self.path = os.path.join(os.getenv("KOWALSKI_DIR"), self.NAME)
    
    def delete(self):
        try:
            os.remove(self.path)
        except:
            pass

    def initialize(self):
        os.makedirs(os.getenv("KOWALSKI_DIR"), exist_ok=True)
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS notes (
                    id TEXT PRIMARY KEY,
                    slug TEXT NOT NULL,
                    book TEXT NOT NULL,
                    updated_at DATETIME NOT NULL,
                    media TEXT NOT NULL,
                    source TEXT,
                    content TEXT NOT NULL
                )
            """)
            conn.commit()

    def insert(self, note: Note):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO notes (id, slug, book, updated_at, media, source, content) VALUES (?,?,?,?,?,?,?)", (note.id, note.slug, note.book, note.updated_at, note.media, note.source, note.content))
            conn.commit()

    def remove(self, id: str):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM notes WHERE id = '{}'".format(id))
            conn.commit()

    def list_books(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT book, COUNT() AS count FROM notes GROUP BY book ORDER BY count DESC")
            return cursor.fetchall()
        
    def list_notes(self, book: str):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT book, updated_at, media, source, content FROM notes WHERE book = '{}' ORDER BY updated_at DESC".format(book))
            return cursor.fetchall()
        
    def get_note(self, slug:str):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, book, content FROM notes WHERE slug = '{}'".format(slug))
            return cursor.fetchone()


