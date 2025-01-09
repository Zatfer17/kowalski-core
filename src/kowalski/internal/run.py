from subprocess import run

def execute(command: str, split=True, shell=False, output: bool = False):
    if split:
        command = command.split(" ")
    if output:
        return run(command, shell=shell, capture_output=True, text=True).stdout
    else:
        run(command, shell=shell)
        return None