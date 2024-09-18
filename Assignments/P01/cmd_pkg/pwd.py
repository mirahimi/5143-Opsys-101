from pathlib import Path

def pwd():
    current_dir = Path.cwd()
    print(current_dir)
    return current_dir

if __name__ == "__main__":
    pwd()