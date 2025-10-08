import os

if not os.path.exists("d_folder"):
    os.mkdir("d_folder")
    print("Created directory: d_folder")
else:
    print("Directory 'd_folder' already exists.")

try:
    os.rmdir("d_folder")
    print("Directory 'd_folder' removed.")
except FileNotFoundError:
    print("Directory 'd_folder' not found.")
except OSError:
    print("Directory 'd_folder' is not empty, cannot remove.")

print("Contents after mkdir:", os.listdir())

os.mkdir("d_folder")
os.chdir("d_folder")
print("Now inside:", os.getcwd())
