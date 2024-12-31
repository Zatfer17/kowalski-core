import subprocess


def run(command):
    return subprocess.run(command.split(' '))