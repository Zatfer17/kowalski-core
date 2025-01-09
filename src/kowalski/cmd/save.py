from kowalski.internal.parse import get_content
from kowalski.cmd.add        import add_cmd


def save_cmd(url: str):

    content = get_content(url)

    add_cmd(content)