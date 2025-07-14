from .commands import RESPONSES

def get_response(command: str) -> str:
    return RESPONSES.get(command.lower().strip(), "bash: command not found")
