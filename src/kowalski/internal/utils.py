import os
import re

from datetime import datetime


def get_date_from_filename(filepath: str):

    filename = os.path.basename(filepath)

    date_part, time_part = filename.split('-')[0], filename.split('-')[1][:6]

    return datetime.strptime(f"{date_part} {time_part}", "%d%b%Y %H%M%S")

def split_text(text: str):

    PATTERN = r'(.*?)(\.+)$'.format()

    match = re.match(PATTERN, text)

    if match:

        part1 = match.group(1).strip()
        part2 = match.group(2).strip()

        return part1, part2
    
    else:

        return text, ""


def colored(r: int, g: int, b: int, text: str):

    text, dots = split_text(text)

    return f"\033[38;2;{r};{g};{b}m{text}\033[0m{dots}"

def bold(text: str):

    text, dots = split_text(text)

    return f"\033[1m{text}\033[0m{dots}"