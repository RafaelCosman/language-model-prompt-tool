from inspect import getmembers, isfunction  

import gpt
import generate_python_code
import generate_textbook
import generate_play
import solve_math_problem_UNSAFE
import document_python
import edit
import generate_journal
import collect_documentation
import general_solver
import write_python_file

def trim_leading_whitespace(string):
    lines = string.split('\n')
    trimmed_lines = [line.lstrip() for line in lines]
    return '\n'.join(trimmed_lines)

def collect_documentation():
    """
    Function to collect the documentation of all the modules and functions in the given modules

    Returns
    -------
    str
        The collected documentation
    """

    output = ""

    for module in [gpt, generate_python_code, generate_textbook, generate_play, solve_math_problem_UNSAFE, document_python, edit, generate_journal, collect_documentation, general_solver, write_python_file]:
        output += f"""
================
{module.__name__}.py
================
"""
        if module.__doc__:
            output += module.__doc__

        for item in getmembers(module):
            if isfunction(item[1]) and item[1].__module__ is module.__name__:
                function = item[1]
                output += f"\nfunction {function.__name__}"

                if function.__doc__:
                    output += f"{trim_leading_whitespace(function.__doc__)}"

                output += "\n"
        
    print(output)

    return output

if __name__ == "__main__":
    collect_documentation()