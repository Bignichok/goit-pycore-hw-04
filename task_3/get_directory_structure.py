import sys
from pathlib import Path
from colorama import Fore

def create_directory_structure(directory):
    tree = {}
    for item in directory.iterdir():
        if item.is_dir():
            tree[item.name] = create_directory_structure(item)
        elif item.is_file():
            tree.setdefault('files', []).append(item.name)
    return tree
    
def get_directory_structure(path: str) -> dict:
    path = Path(path)
    
    if path.exists():
        return {path.name: create_directory_structure(path)}
    else:
        raise FileNotFoundError(f"Directory '{path}' does not exist.")
    
def create_directory_structure_string(directory_structure: dict, indent:int = 0) -> str:
    template = ''
    for directory_name, contents in directory_structure.items():
        if directory_name != 'files':
            template += ' ' * indent + f"{Fore.BLUE}{directory_name}{Fore.RESET}\n"
        if isinstance(contents, dict):
            template += create_directory_structure_string(contents, indent + 4)
        elif isinstance(contents, list):
            template += ''.join([' ' * indent + f"{Fore.GREEN}{item}{Fore.RESET}\n" for item in contents])
    return template

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)
    try:
        directory_structure = get_directory_structure(sys.argv[1])
        print(create_directory_structure_string(directory_structure))
    except FileNotFoundError as e:
        print(e)


