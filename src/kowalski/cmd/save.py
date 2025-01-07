from kowalski.internal.parse import get_type_source_content
from kowalski.cmd.add        import addCmd


def saveCmd(note: str):
    _, _, content = get_type_source_content(note)
    addCmd(content)