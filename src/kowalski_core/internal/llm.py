import os

from abc                         import ABC, abstractmethod
from openai                      import OpenAI
from kowalski_core.internal.note import Note


class Client(ABC):

    @abstractmethod
    def completion(self, prompt: str, note: Note):
        pass

class OpenAIClient(Client):

    def __init__(self):
        super().__init__()
        self.client = OpenAI()

    def completion(self, prompt: str, content: str, model: str):

        stream = self.client.chat.completions.create(
            messages = [
                {'role': 'system', 'content': prompt},
                {'role': 'user'  , 'content': content}
            ],
            model=model,
            stream=True,
        )

        for chunk in stream:
            print(chunk.choices[0].delta.content or "", end="")