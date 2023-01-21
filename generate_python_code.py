from gpt import gpt

with open('collected_docstrings.txt', 'r') as f:
    # Read the file into a string
    documentation = f.read()
with open('gpt.py', 'r') as f:
    gpt_code = f.read()
with open('solve_math_problem_UNSAFE.py', 'r') as f:
    solve_math_problem_UNSAFE_code = f.read()
with open('generate_python_code.py', 'r') as f:
    generate_python_code_code = f.read()

def generate_python_code(problem):
    """
    Function to generate python code for a given problem

    Parameters
    ----------
    problem : str
        The problem for which python code needs to be generated

    Returns
    -------
    str
        The generated python code for the input problem
    """

    # Note that as of this writing, the following prompt uses ~2,000 tokens.
    # This gives us about 2000 tokens with which to write code, which is perfect.
    output = gpt(f"""
For reference, here is the documentation for this entire repo. These functions may or may not be helpful for solving the problem below.

{documentation}

Also for reference, here are the contents of some files in this repo:

================
gpt.py
================

{gpt_code}

================
generate_python_code.py
================

{generate_python_code_code}

================
solve_math_problem_UNSAFE.py
================

{solve_math_problem_UNSAFE_code}

Now please generate python code to do the following:

{problem}

- The code should be as concise as possible
- It should minimize side effects and never take dangerous actions like deleting files etc.
- It should make sure to import anything that it uses
- GPT is a Large Language Model (LLM) that is used to complete text. You can give it all kinds of english prompts and it will complete/answer them. You can access GPT using the gpt() function.
- If the code will live in this repo and needs to use the gpt() function, it should import it using `from gpt import gpt` and NOT call `lmtk.modes.raw_gpt.RawGPTMode()`

Python code:
""")

    print(f"Python Code for {problem}:")
    print(output)

    return output

if __name__ == "__main__":
    generate_python_code(input("What would you like to generate python code for? For example, you could say 'Accept an integer and list its factors'. "))