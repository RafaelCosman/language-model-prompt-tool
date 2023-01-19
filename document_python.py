from helper_functions import ask

def document_python_file(python_code):
    output = ask(f"""
Example:
===============================================
If the Python code was:

from helper_functions import ask

def edit(text):
    output = ask(f\"\"\"
Please edit the following text to be as clear and concise as possible:

{{text}}

\"\"\")

    print("Edited version of input text:")
    print(output)

    return output

if __name__ == "__main__":
    edit(input("What text would you like me to edit? Please paste it here. I will make it as clear and concise as possible."))

The correct output would be:

from helper_functions import ask

def edit(text):
    \"\"\"
    Function to edit the text to be as clear and concise as possible.

    Parameters
    ----------
    text : str
        The text to be edited.

    Returns
    -------
    str
        The edited version of the input text.
    \"\"\"
    output = ask(f\"\"\"
Please edit the following text to be as clear and concise as possible:

{{text}}

\"\"\")

    print("Edited version of input text:")
    print(output)

    return output

if __name__ == "__main__":
    edit(input("What text would you like me to edit? Please paste it here. I will make it as clear and concise as possible."))
===============================================

Please document the following python code.
- Note that your documented version should include ALL of the original code, exactly as-is.
- It should not make ANY changes to the original code.
- It should add docstrings, comments, etc. where appropriate.
- It should use best practices for Python programming, and all the latest standards.

Python code:

{python_code}

Documented version of the Python Code:

""")

    print(f"Documented python code:")
    print(output)

    return output

def document_python_file_inplace(file_path):
    with open(file_path, "r") as file:
        python_code = file.read()

    documented_python_code = document_python_file(python_code)

    with open(file_path, "w") as file:
        file.write(documented_python_code)

if __name__ == "__main__":
    document_python_file_inplace(input("Please specify the file path of the python file that you would like documented. "))