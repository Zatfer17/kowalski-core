from ollama import chat
from kowalski_core.features.note import Note


class Magician():

    def __init__(self, model_name: str = 'llama3.2:1b'):
        self.model_name = model_name

    def trick(self, note: Note, intent: str):
        messages = [
            {'role': 'system', 'content': 'You are an AI assistant specialized in summarizing content'},
            {'role': 'user'  , 'content': note.content}
        ]
        stream = chat(
            model=self.model_name,
            messages=messages,
            stream=True,
        )
        content = ''
        for chunk in stream:
            piece = chunk['message']['content']
            if piece:
                print(piece, end='', flush=True)
                content += piece
            else:
                break
        media = 'note'
        source = 'magic'
        return media, source, content