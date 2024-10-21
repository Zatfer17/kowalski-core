import re
import uuid
import os

from kowalski_core.features.collect.markdown import parse_note
from kowalski_core.config                    import NOTES_PATH
from kowalski_core.features.collect.youtube  import get_yt_content
from kowalski_core.features.collect.url      import get_url_content

from datetime            import datetime
from typing              import Tuple
from importlib.resources import open_text


class Note():

    def __init__(self, source: str, is_path: bool=False) -> None:
        if not is_path:
            self.id                               = self.get_id()
            self.media, self.source, self.content = self.get_media_source_and_content(source)
            self.created_at                       = self.get_created_at()
            self.transform_path                   = self.get_transform_path()
        else:
            metadata, content = parse_note(source)
            self.id             = metadata['id']
            self.media          = metadata['media']
            self.source         = metadata['source']
            self.content        = content
            self.created_at     = metadata['created_at']
            self.transform_path = metadata['transform_path']
    
    def get_id(self):
        return str(uuid.uuid4())

    def get_media_source_and_content(self, source: str) -> Tuple[str, str, str]:
        URL_REGEX = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
        YT_REGEX  = r"(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+"
        if re.match(YT_REGEX, source):
            media   = 'yt'
            content = get_yt_content(source)
        elif re.match(URL_REGEX, source):
            content = get_url_content(source)
            media   = 'url'
        else:
            media   = 'note'
            content = source
            source  = 'None'
        return media, source, content
    
    def get_created_at(self):
        return datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    
    def get_path(self, mode: str) -> str:
        note_name = f'{self.media}_{self.created_at}.md'
        return os.path.join(NOTES_PATH, mode, note_name)
    
    def get_transform_path(self) -> str:
        note_name = f'{self.media}_{self.created_at}.md'
        return os.path.join(NOTES_PATH, 'transform', note_name)
    
    def write_note(self, mode: str) -> None:
        note_config = {
            'id'            : self.id,
            'media'         : self.media,
            'source'        : self.source,
            'created_at'    : self.created_at,
            'transform_path': self.transform_path,
            'content'       : self.content
        }
        note_template = open_text('kowalski_core.features.collect.templates', 'note.md')
        path = self.get_path(mode)
        with open(path, 'w', encoding="utf-8") as f:
            f.write(note_template.read().format(**note_config))
            return path

    