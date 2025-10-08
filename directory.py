import os

def make_directory(name):
    try:
        os.mkdir(name)
        print(f"Directory '{name}' created.")
    except FileExistsError:
        print(f"Directory '{name}' already exists.")

def remove_directory(name):
    try:
        os.rmdir(name)
        print(f"Directory '{name}' removed.")
    except FileNotFoundError:
        print(f"Directory '{name}' not found.")
    except OSError:
        print(f"Directory '{name}' is not empty, cannot remove.")

def list_directory(path="."):
    print(f"Contents of '{os.path.abspath(path)}':")
    for item in os.listdir(path):
        print(" -", item)

def get_working_directory():
    return os.getcwd()

def change_directory(path):
    try:
        os.chdir(path)
        print(f"Changed working directory to: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Directory '{path}' not found.")

print("Current directory:", get_working_directory())

make_directory("test_folder")
list_directory()

change_directory("test_folder")
print("Now inside:", get_working_directory())

change_directory("..")
remove_directory("test_folder")


