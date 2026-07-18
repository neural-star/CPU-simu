from pathlib import Path

def create_file(path: str):
    file_path = Path(path)

    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    if not file_path.exists():
        file_path.touch()

def file_status(path) -> tuple[bool,bool,str]:
    status = [False, False, ""]
    file = Path(path).expanduser()

    status[0] = file.exists()
    status[1] = file.is_file()
    status[2] = file.suffix
    
    return tuple(status)
