from pathlib import Path

if __name__ == '__main__':
    cwd = Path.cwd()
    file_path = cwd / 'test.txt'
    print(file_path.read_text())