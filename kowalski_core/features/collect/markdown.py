import re


METADATA_REGEX = r"\[_metadata_:(\w+)\]:-\s+\"(.*?)\""
CONTENT_REGEX  = r"\n\n([\s\S]+)$"

def get_metadata(note:str):
    matches = re.findall(METADATA_REGEX, note)    
    return {key: value for key, value in matches}

def get_content(note: str):
    match = re.search(CONTENT_REGEX, note)

    if match:
        return match.group(1).strip()

def parse_note(source: str):
    with open(source) as f:
        note = f.read()
    return get_metadata(note), get_content(note)