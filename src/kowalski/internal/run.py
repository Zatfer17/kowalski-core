from subprocess import run


def execute(command):
    return run(command.split(" "))