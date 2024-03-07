
import nbformat
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
import subprocess
import os
import glob

# Clone the repository
subprocess.run(['git', 'clone', 'https://github.com/ratfactor/ziglings.git'])

# Path to the exercises directory in the cloned repo
exercises_path = 'ziglings/exercises/'

# Populate the list of exercise files
exercise_files = sorted(glob.glob(os.path.join(exercises_path, '*.zig')))

# Read the contents of each exercise file
exercise_content = []
for filepath in exercise_files:
    with open(filepath, 'r') as file:
        exercise_content.append(file.read())

# Adjust file names to be just the filenames, not the full path
exercise_files = [os.path.basename(filepath) for filepath in exercise_files]

# Create a new notebook object
notebook = new_notebook()

# First cell: Instructions to install Zig
notebook.cells.append(new_markdown_cell("# Install Zig on Google Colab"))
install_commands = """
!wget https://ziglang.org/download/0.11.0/zig-linux-x86_64-0.11.0.tar.xz
!tar -xf zig-linux-x86_64-0.11.0.tar.xz && rm zig-linux-x86_64-0.11.0.tar.xz

import os
os.environ['PATH'] += ":/content/zig-linux-x86_64-0.11.0"
"""
notebook.cells.append(new_code_cell(install_commands))

# Loop through each exercise file
for filename, content in zip(exercise_files, exercise_content):
    # Add a markdown cell for the filename
    notebook.cells.append(new_markdown_cell(filename))
    
    # Add a code cell to write the file contents
    notebook.cells.append(new_code_cell(f"%%writefile {filename}\n\n{content}"))
    
    # Add a code cell to run the file
    notebook.cells.append(new_code_cell(f"!zig run {filename}"))

# Saving the notebook
nbformat.write(notebook, 'Ziglings_on_Colab.ipynb')
