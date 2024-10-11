import re
import uuid
import os

from kowalski_core.config           import NOTES_PATH
from kowalski_core.features.intent  import Intent
from kowalski_core.features.youtube import get_yt_content
from kowalski_core.features.url     import get_url_content

from datetime import datetime
from typing import Tuple
from importlib.resources import open_text

URL_REGEX = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
YT_REGEX  = r"(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+"

class Note():

    def __init__(self, source: str, intent: Intent) -> None:
        self.media, self.source, self.content = self.get_media_source_and_content(source)
        self.created_at = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        self.id = str(uuid.uuid4())
        self.intent = intent
        self.name = f'{self.media}_{self.created_at}.md'

    def get_media_source_and_content(self, source: str) -> Tuple[str, str, str]:
        if re.match(YT_REGEX, source):
            media = 'yt'
            content = get_yt_content(source)
        elif re.match(URL_REGEX, source):
            content = get_url_content(source)
            media = 'url'
        else:
            media = 'note'
            content = source
            source = 'None'
        return media, source, content
    
    def get_note_path(self) -> str:
        return os.path.join(NOTES_PATH, 'collect', self.name)
    
    def get_intent_path(self) -> str:
        return os.path.join(NOTES_PATH, 'transform', self.name)

    def get_note(self) -> str:
        metadata = {
            'media' : self.media,
            'source': self.source,
            'created_at': self.created_at,
            'id': self.id,
            'intent': self.intent,
            'intent_output': self.get_intent_path(),
            'content': self.content
        }
        note_template = open_text('kowalski_core.templates', 'note.md')
        return note_template.read().format(**metadata)
    
    def write_note(self) -> None:
        note_path = self.get_note_path()
        with open(note_path, 'w', encoding="utf-8") as f:
            f.write(self.get_note())

    