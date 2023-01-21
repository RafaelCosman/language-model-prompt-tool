from gpt import gpt
from generate_journal import generate_journal, generate_article
from generate_python_code import generate_python_code
from generate_textbook import generate_textbook
from generate_play import generate_play
from solve_math_problem_UNSAFE import solve_math_problem_UNSAFE
from write_python_file import write_python_file

def general_solver(prompt):
    # Load the collected documentation
    with open("collected_docstrings.txt", "r") as f:
        collected_docstrings = f.read()

    # Ask GPT for a function and what to pass into it
    function_to_call = gpt(f"""
For reference, here is the documentation of this entire repo:

{collected_docstrings}

We now have a prompt and would like you to figure out which function in this repo should be used to solve the propmt, and what should be passed into that function

For example, if the prompt was "Please generate for me a play about love", you would output:
generate_play("Love")

If the prompt was "Write me a journal article about technology" you would output:
generate_article("Technology")

If the prompt was "Write me a short story about aliens" you would notice that there is no function in the repo for generating short stories, and therefore you would output:
write_python_file("generate_short_story.py", "Please write me a file that generates short stories based on a topic. It should rely on the gpt function (similar to generate_textbook() or generate_journal()) and should be based on the fundamental structure that short stories have (e.g. characters, a narrative arc, etc.).")

If the prompt was "Please write me an anthology of stories about Exploration"
You would NOT use the generate_textbook() function, because that function is specific for generating textbooks. It does not work for anthologies.
You would instead output:
write_python_file("generate_short_story_anthology.py", "Please write me a file that generates an anthology of short stories based on a topic. It should rely on the gpt function (similar to generate_textbook() or generate_journal()) and should be based on the fundamental structure that anthologies of short stories have.")

Note that you CANNOT use functions that do not exist. For example, if you don't see a generate_business_plan() function in the docs, you cannot call it.
You must instead use write_python_file() to generate that file for later use. 

================
Now here is the actual prompt we are trying to solve:

{prompt}

Please now give us the function and the input to that function. Please do not output anything else.

Function and input:
""")

    print(function_to_call)

    output = eval(function_to_call)

    print(output)

if __name__ == "__main__":
    general_solver(input("What would you like me to solve? Please give me a problem in plain language, like 'Write me a textbook on American History'. "))