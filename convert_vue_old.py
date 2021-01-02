
import os
import glob
import sys
from pathlib import Path

views_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "frontend", "src", "views")
python_files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "code-examples", "examples")

def replace_string(filename_vue_file):
    vue_base_file = open(filename_vue_file, "rt")
    vue_target_file = open(filename_vue_file.replace("_base", ""), "wt")
    paths = Path(python_files_path).glob('**/*.py')
    filename_python_file = None
    print(filename_vue_file)
    print(python_files_path)
    for path in paths:
        if path.name == f"{filename}.py":
            filename_python_file = str(path)
            print(f"Using python file: {filename_python_file}")
            output_file = open(os.path.join(os.path.dirname(filename_python_file), "output.txt"), "rt")
            output_file_lines = [l for l in output_file]
            output_file.close()
    if not filename_python_file:
        raise Exception("No python file found")
    python_file = open(filename_python_file, "rt")
    python_code = python_file.read()
    python_code = python_code.replace('"""', '')
    python_code = python_code.replace('# ```', '```')
    python_code = python_code.replace('`', '\`')
    python_code_parts = python_code.split("#-#-#-#")
    for vue_line in vue_base_file:
        line_added = False
        # first part = setup, last part = cleanup [1:-1]
        for i, python_code_part in enumerate(python_code_parts[1:-1]):
            if f"CONTENT{i}" in vue_line:
                line_added = True
                text_without_write_lines = ''
                output_lines_counter = 0
                python_lines = python_code_parts[i+1].split("\n")
                for python_lin_index, python_line in enumerate(python_lines):
                    if python_line.startswith("output_file.write"):
                        continue
                    if python_line.startswith("# Output:"):
                        python_line = python_line.replace("# Output:", ">>> ") + output_file_lines[output_lines_counter].replace("\n", "")
                        output_lines_counter+= 1
                    text_without_write_lines+= python_line + "\n"
                vue_target_file.write(vue_line.replace(f"CONTENT{i}", f'{text_without_write_lines}'))
        if not line_added:
            vue_target_file.write(vue_line)
    vue_base_file.close()
    vue_target_file.close()


filename = sys.argv[1]
print(f"Filename: {filename}")
paths = Path(views_path).glob('**/*.vue')
for path in paths:
    if path.name == f"{filename}_base.vue":
        filename_vue_file = str(path)
        print(f"Using file: {filename_vue_file}")
        replace_string(filename_vue_file)
