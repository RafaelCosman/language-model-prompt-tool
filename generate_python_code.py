from gpt import gpt

with open('collected_docstrings.txt', 'r') as f:
    # Read the file into a string
    documentation = f.read()

def generate_python_code(problem):
    """
    Function to generate python code for a given problem.

    Parameters
    ----------
    problem : str
        The problem for which python code needs to be generated.

    Returns
    -------
    str
        The generated python code for the input problem.
    """

    output = gpt(f"""
For reference, here is the documentation for this entire repo. These functions may or may not be helpful for solving the problem below.

{documentation}

Please generate python code to do the following:

{problem}

- The code should be as concise as possible
- It should minimize side effects and never take dangerous actions like deleting files etc.

Python code:
""")

    print(f"Python Code for {problem}:")
    print(output)

    return output

if __name__ == "__main__":
    generate_python_code(input("What would you like to generate python code for? For example, you could say 'Accept an integer and list its factors'. "))