import sys
import os

def get_supposed_venv_path() -> str:
    bin_path = path_get_prevfolder(sys.executable)
    svenv_path = path_get_prevfolder(bin_path)
    return svenv_path

def path_get_prevfolder(pathstr) -> str:
    return os.path.split(pathstr)[0]

def check_if_in_venv() -> bool:
    path_of_this_script = os.path.dirname(os.path.realpath(__file__))
    path_of_this_folder = path_get_prevfolder(path_of_this_script)
    path_of_supposed_venv = get_supposed_venv_path()
    is_venv = path_of_supposed_venv.startswith(path_of_this_folder)
    return is_venv

if __name__ == "__main__":
    print()
    current_py = sys.executable
    if check_if_in_venv():
        binpath = os.path.split(current_py)[0]
        venvpath = os.path.split(binpath)[0]
        venvname = os.path.split(venvpath)[1]
        print(
            "MATRIX STATUS: Welcome to the construct", 
            f"Current Python: {current_py}",
            f"Virtual Environment: {venvname}",
            f"Environment Path: {venvpath}",
            "",
            "SUCCESS: You're in an isolated environment!",
            "Safe to install packages without affecting the global system.",
            "",
            "Package installation path:",
            f"Environment Path: {sys.path[-1]}",
            sep = "\n",
            )
    else:
        print(
            "MATRIX STATUS: You're still plugged in", 
            f"Current Python: {current_py}",
            "Virtual Environment: None detected",
            "",
            "WARNING: You're in the global environment!",
            "The machines can see everything you install.",
            "",
            "To enter the construct, run:",
            "python -m venv matrix_env",
            "source matrix_env/bin/activate # On Unix",
            "matrix_env\\Scripts\\activate # On Windows",
            "Then run this program again.",
            sep = "\n",
            )


"""
To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env\\Scripts\\activate # On Windows
Then run this program again.






"""
