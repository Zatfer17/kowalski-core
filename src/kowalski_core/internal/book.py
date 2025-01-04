import click


class Book():

    def __init__(self, book: str, count: int):
        self.book = book
        self.count = count

    def __str__(self):
        return "{} -> {}".format(
            click.style(f"[{self.book}]", fg="yellow", bold=True),
            click.style(f"[{self.count}]", fg="green", bold=False)
        )