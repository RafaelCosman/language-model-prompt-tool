"""
This module contains functions to write a new python file using GPT
"""

import sys
import os
from generate_python_code import generate_python_code

def write_python_file(filename, description):
    """
    Function to write a python file

    Parameters
    ----------
    filename : str
        The name of the python file
    description : str
        A description of the desired functionality of the python file

    Returns
    -------
    str
        The generated code
    """
    code = generate_python_code(f"Write a python file called '{filename}' that will live in this repo and does the following: {description}")

    with open(filename, "w") as f:
        f.write(code.lstrip())
    
    print(f"File {filename} successfully written!")

    return code

if __name__ == "__main__":
    filename = input("What would you like to name the python file? (e.g. test.py) ")
    description = input("Please provide a description of the desired functionality of the python file. ")
    write_python_file(filename, description)