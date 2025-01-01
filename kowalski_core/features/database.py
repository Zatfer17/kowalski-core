import os
import chromadb
import time
import logging

from datetime import datetime
from kowalski_core.features.book import Book
from kowalski_core.features.note import Note


logging.getLogger("chromadb").setLevel(logging.CRITICAL)

def flatten(xss):
    return [x for xs in xss for x in xs]

class Database:
    
    def __init__(self, db_base_path:str=os.getenv('HOME'), db_dir:str='.kowalski') -> None:
        self.db_path = os.path.join(db_base_path, db_dir)
        self.client = chromadb.PersistentClient(self.db_path)

    def insert_note(self, book:str, media:str, source:str, content:str) -> None:
        collection = self.client.get_or_create_collection(book)
        timestamp = time.time()
        date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        collection.add(
            documents=[content],
            metadatas=[{'date': date, 'media': media, 'source': source}],
            ids=[str(round(timestamp))]
        )

    def list_books(self):
        return [Book(book, self.client.get_collection(book).count()) for book in self.client.list_collections()]
    
    def list_notes(self, book:str, limit:int):
        notes = self.client.get_collection(book).peek(limit)
        return [Note(book, id, metadata['date'], metadata['media'], metadata['source'], content) for id, metadata, content in zip(notes['ids'], notes['metadatas'], notes['documents'])]
    
    def query_notes(self, keywords: str, book: str, exact: bool):
        if book is None:
            if exact:
                results = [self.client.get_collection(book).get(where_document={'$contains': keywords}) for book in self.client.list_collections()]
                notes = []
                for result in results:
                    notes.append([Note(book, id, metadata['date'], metadata['media'], metadata['source'], content) for id, metadata, content in zip(result['ids'], result['metadatas'], result['documents'])])
                return flatten(notes)
            else:
                results = [self.client.get_collection(book).query(query_texts=keywords) for book in self.client.list_collections()]
                notes = []
                for result in results:
                    notes.append([Note(book, id, metadata['date'], metadata['media'], metadata['source'], content, distance) for id, metadata, content, distance in zip(flatten(result['ids']), flatten(result['metadatas']), flatten(result['documents']), flatten(result['distances']))])
                return sorted(flatten(notes), key=lambda x: x.distance)
        else:
            if exact:
                results = self.client.get_collection(book).get(where_document={'$contains': keywords})
                return [Note(book, id, metadata['date'], metadata['media'], metadata['source'], content) for id, metadata, content in zip(results['ids'], results['metadatas'], results['documents'])]
            else:
                results = self.client.get_collection(book).query(query_texts=keywords)
                notes = [Note(book, id, metadata['date'], metadata['media'], metadata['source'], content, distance) for id, metadata, content, distance in zip(flatten(results['ids']), flatten(results['metadatas']), flatten(results['documents']), flatten(results['distances']))]
                return sorted(notes, key=lambda x: x.distance)
            
    def get_note(self, id: str):
        for book in self.client.list_collections():
            results = self.client.get_collection(book).get(id)
            if results['documents']:
                return [Note(book, id, metadata['date'], metadata['media'], metadata['source'], content, full=True) for id, metadata, content in zip(results['ids'], results['metadatas'], results['documents'])]
            