import os
from pathlib import Path

folder = Path(os.getcwd())
print(folder == Path.cwd())
print((folder / "notes.txt").name)
print(Path("lesson.py").suffix)
