import sys
from colorama import init, Fore

init(autoreset=True)

class TmxFileNotFoundError(Exception):
    message = "ERROR <TmxFileNotFoundError> no such file or directory -> {path}"
    def __init__(self, path: str) -> None:
        print(Fore.RED + f"{self.message.format(path=path)}")
        sys.exit(0)

class TmxParseError(Exception):
    message = "ERROR <TmxParseError> {description}"
    def __init__(self, description: str) -> None:
        print(Fore.RED + f"{self.message.format(description=description)}")
        sys.exit(0)