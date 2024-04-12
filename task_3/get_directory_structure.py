import sys
from pathlib import Path
from colorama import Fore

def create_directory_structure(directory):
    tree = {}
    for item in directory.iterdir():
        if item.is_dir():
            tree[item.name] = create_directory_structure(item)
        elif item.is_file():
            parent_dir = tree.get('files', [])
            parent_dir.append(item.name)
            tree['files'] = parent_dir
    return tree
    
def get_directory_structure(path: str) -> dict:
    path = Path(path)
    
    if path.exists():
        return {path.name: create_directory_structure(path)}
    else:
        print("file does not exist")
        return {}
    
def create_directory_structure_string(directory_structure: dict, indent:int = 0) -> str:
    template = ''
    for directory_name, contents in directory_structure.items():
        if directory_name != 'files':
            template += ' ' * indent + Fore.BLUE + directory_name + Fore.RESET + '\n'
        if isinstance(contents, dict):
            template += create_directory_structure_string(contents, indent + 4)
        elif isinstance(contents, list):
            for item in contents:
                template += ' ' * indent + Fore.GREEN + item + Fore.RESET + '\n'
    return template

directory_structure = get_directory_structure(sys.argv[1])
print(create_directory_structure_string(directory_structure))


