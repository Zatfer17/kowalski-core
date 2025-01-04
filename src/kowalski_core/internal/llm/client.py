from abc                         import ABC, abstractmethod
from kowalski_core.internal.note import Note


class Client(ABC):

    @abstractmethod
    def completion(self, prompt: str, note: Note) -> str:
        pass