from subprocess import run


def execute(command: str, split=True, shell=False, output: bool = False):
    if split:
        command = command.split()
    result = run(command, shell=shell, capture_output=output, text=True)
    if output:
        return result.stdout
    return None