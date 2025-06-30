# utils/file_loader.py

def load_binary_file(path: str) -> bytes:
    with open(path, 'rb') as f:
        return f.read()
