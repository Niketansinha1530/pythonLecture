from pathlib import Path
folder = Path(r"D:\Python\Oops\bank.py")
print("Folder Name:", folder.name)
print("Parent Directory:", folder.parent)
print("Is Directory?", folder.is_dir())
print("Is File?", folder.is_file())
print("Size (bytes):", folder.stat().st_size)