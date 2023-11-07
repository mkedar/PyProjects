# compile_script.py
from PyInstaller.__main__ import run

# The path to the script you want to compile into an executable
script_path = 'C:/Desktop/closer.py'

# The options you would normally pass in the command line
# "--onefile" creates a single executable file
# "--windowed" is for windowed apps, omit this for console applications
# "--name" names the output file
# "--clean" cleans the build folder
options = [
    '--onefile',
    '--clean',
    f'--name=your_executable_name',
    script_path
]

run(options)
