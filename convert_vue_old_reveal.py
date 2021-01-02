
import os
import glob
import sys
from pathlib import Path

views_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "frontend", "src", "views")
python_files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "code-examples", "examples")

def replace_string(filename_vue_file):
    vue_base_file = open(filename_vue_file, "rt")
    vue_target_file = open(os.path.join(views_path, category_1, category_2, filename + ".vue"), "wt")
    paths = Path(python_files_path).glob('**/*.py')
    filename_python_file = None
    print(filename_vue_file)
    print(python_files_path)
    for path in paths:
        if path.name == f"{filename}.py":
            filename_python_file = str(path)
            print(f"Using python file: {filename_python_file}")
            try:
                output_file = open(os.path.join(os.path.dirname(filename_python_file), "output.txt"), "rt")
                output_file_lines = [l for l in output_file]
                output_file.close()
            except Exception:
                print("Could not find output.txt")
    if not filename_python_file:
        raise Exception("No python file found")
    python_file = open(filename_python_file, "rt")
    python_code = python_file.read()
    python_code = "".join(python_code.split("#-#-#-#")[1:-1])
    python_code = python_code.replace('"""', '')
    for vue_line in vue_base_file:
        if f"CONTENT" in vue_line:
            vue_target_file.write(python_code)
        elif "SlideBase" in vue_line:
            vue_target_file.write(vue_line.replace("SlideBase", filename))
        else:
            vue_target_file.write(vue_line)
    vue_base_file.close()
    vue_target_file.close()


category_1 = sys.argv[1]
category_2 = sys.argv[2]
filename = sys.argv[3]
print(f"Filename: {filename}")
paths = Path(views_path).glob('**/*.vue')
for path in paths:
    if path.name == f"SlideBase.vue":
        filename_vue_file = str(path)
        print(f"Using file: {filename_vue_file}")
        replace_string(filename_vue_file)
