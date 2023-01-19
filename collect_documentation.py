from inspect import getmembers, isfunction  

import generate_python_code
import generate_textbook
import generate_play
import solve_math_problem_UNSAFE
import document_python

def collect_documentation():
    output = ""

    for module in [generate_python_code, generate_textbook, generate_play, solve_math_problem_UNSAFE, document_python]:
        output += f"""
================
Module {module.__name__}
Docstring: {module.__doc__}
"""

        for item in getmembers(module):
             if isfunction(item[1]):
                function = item[1]
                output += f"""
function: {function.__name__}
docstring: {function.__doc__}
"""
        
    print(output)

    return output

if __name__ == "__main__":
    collect_documentation()