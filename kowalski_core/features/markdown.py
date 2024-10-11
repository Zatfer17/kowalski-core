import re


METADATA_REGEX = r"\[_metadata_:(\w+)\]:-\s+\"(.*?)\""
CONTENT_REGEX  = r"\n\n([\s\S]+)$"

def get_metadata(content:str):
    matches = re.findall(METADATA_REGEX, content)    
    return {key: value for key, value in matches}

def get_content(content: str):
    content_match = re.search(CONTENT_REGEX, content)

    if content_match:
        return content_match.group(1).strip()