from helper_functions import gpt
from generate_journal import generate_journal, generate_article
from generate_python_code import generate_python_code
from generate_textbook import generate_textbook
from generate_play import generate_play
from solve_math_problem_UNSAFE import solve_math_problem_UNSAFE

def general_solver(prompt):
    suggested_function = gpt(f"""
We are trying to solve the following prompt:

{prompt}

Which of the following functions might be useful to solve this problem?

A. generate_article
B. generate_journal
C. generate_python_code
D. generate_textbook
E. generate_play
F. solve_math_problem_UNSAFE

Suggested function (please respond with one of the above options):
""")

    print("suggested_function:", suggested_function)

    if suggested_function == "A. generate_article":
        topic = gpt(f"""
The user has asked:

{prompt}

As one step of solving this, we are going to write an article using the generate_article function.

What string should we pass into that function? It should be the topic of an article that will help us respond to the user's prompt.

Topic:

""")
        output = generate_article(topic)
    elif suggested_function == "B. generate_journal":
        topic = gpt(f"""
The user has asked:

{prompt}

As one step of solving this, we are going to write an entire journal using the generate_journal function.

What string should we pass into that function? It should be a topic that will help us respond to the user's prompt.

Topic:

""")
        output = generate_journal(topic)
    elif suggested_function == "C. generate_python_code":
        problem = gpt(f"""
The user has asked:

{prompt}

As one step of solving this, we are going to write python code using the generate_python_code function.

What string should we pass into that function? It should be the description of a problem or program that will help us respond to the user's prompt.

Topic:

""")
        output = generate_python_code(problem)
    elif suggested_function == "D. generate_textbook":
        topic = gpt(f"""
The user has asked:

{prompt}

As one step of solving this, we are going to write an textbook using the generate_textbook function.

What string should we pass into that function? It should be the topic of a textbook that will help us respond to the user's prompt.

Topic:

""")
        output = generate_textbook(topic)
    elif suggested_function == "E. generate_play":
        play_name = gpt(f"""
The user has asked:

{prompt}

As one step of solving this, we are going to write an play using the generate_play function.

What string should we pass into that function? It should be the topic of a play that will help us respond to the user's prompt.

Topic:

""")
        output = generate_play(play_name)
    elif suggested_function == "F. solve_math_problem_UNSAFE":
        problem = gpt(f"""
The user has asked:

{prompt}

As one step of solving this, we are going to solve a math problem using the solve_math_problem_UNSAFE function.

What string should we pass into that function? It should be a math problem that will help us respond to the user's prompt.

Problem:

""")
        output = solve_math_problem_UNSAFE(problem)
    else:
        output = "No suitable function found."

    print(f"\nOutput for {prompt}:")
    print(output)

    return output

if __name__ == "__main__":
    general_solver(input("What would you like me to solve? Please give me a problem in plain language, like 'Find the factorial of a number'. "))