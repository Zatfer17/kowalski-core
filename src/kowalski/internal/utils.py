import os

from datetime import datetime


def get_date_from_filename(filepath: str):

    filename = os.path.basename(filepath)

    date_part, time_part = filename.split('-')[0], filename.split('-')[1][:6]

    return datetime.strptime(f"{date_part} {time_part}", "%d%b%Y %H%M%S")