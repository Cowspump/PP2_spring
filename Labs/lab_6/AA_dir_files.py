#Python Directories and Files exercises

import os



def list_directories(path):
    """List all directories in the specified path."""
    try:
        directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        print("Directories:")
        for directory in directories:
            print(directory)
    except FileNotFoundError:
        print(f"Error: The specified path '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for the path '{path}'.")


def list_files(path):
    """List all files in the specified path."""
    try:
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        print("Files:")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Error: The specified path '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for the path '{path}'.")


def list_all(path):
    """List all directories and files in the specified path."""
    try:
        items = os.listdir(path)
        print("All directories and files:")
        for item in items:
            print(item)
    except FileNotFoundError:
        print(f"Error: The specified path '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for the path '{path}'.")


if __name__ == "__main__":
    specified_path = input("Enter the path: ").strip()

    print("\n--- Listing Directories ---")
    list_directories(specified_path)

    print("\n--- Listing Files ---")
    list_files(specified_path)

    print("\n--- Listing All (Directories and Files) ---")
    list_all(specified_path)
    print()


#task2

def task2(path):
    if os.path.exists(path):
        result = 'Path is '

        result += 'readable, ' if os.access(path, os.R_OK) else 'not readable, '

        result += 'writable, ' if os.access(path, os.W_OK) else 'not writable, '

        result += 'executable' if os.access(path, os.X_OK)else 'not executable.'

        print(f'Path {path} exists\n{result}')

    else:
        print(f'Path {path} does not exists')

if __name__ == "__main__":
    specified_path = input("Enter the path: ").strip()
    task2(specified_path)
    print()



def task3(path):
    if os.path.exists(path):
        print(f'Path {path} exists')
        directory, filename = os.path.split(path)
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print(f'Path {path} does not exists')

if __name__ == "__main__":
    specified_path = input("Enter the path: ").strip()
    task3(specified_path)
    print()

def task4(file):
    with open(file, 'r') as file:
        lines = file.readlines()
        print(f'Numbers of lines = {len(lines)}')

if __name__ == "__main__":
    file_name = input("Enter the file name: ").strip()
    task4(file_name)
    print()


nums = ['1', '2', '3']

def task5(path, l):

    with open(path, 'w') as file:
        file.write(' '.join(l))


if __name__ == "__main__":
    specified_path = input("Enter the path: ").strip()
    task5(specified_path, nums)
    print()



def task6():
    from string import ascii_uppercase
    for letter in ascii_uppercase:
        with open(f'{letter}.txt', 'w'):
            pass

    # delete these 26 files
    for letter in ascii_uppercase:
        os.remove(f'{letter}.txt')



def task7(pt1, pt2):

    with open(path1, 'r') as file1, open(path2, 'a') as file2:
        file2.write(file1.read())

if __name__ == "__main__":
    path1 = input("Enter the path to the first file: ").strip()
    path2 = input("Enter the path to the second file: ").strip()
    task7(path1, path2)


def task8(pt):
    if os.access(path, os.F_OK):
        os.remove(path)
        print('File exists and has been removed')
    else:
        print(f"Error: File '{path}' does not exist.")

if __name__ == "__main__":
    path = input("Enter the path to the file: ").strip()
    task8(path)

