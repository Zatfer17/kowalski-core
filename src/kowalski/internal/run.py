from subprocess import run, PIPE


def execute(command):
    return run(command.split(" "))

def execute_with_stdout(command):
    return run(command.split(" "), capture_output=True, text=True).stdout