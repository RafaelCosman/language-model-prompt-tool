from gpt import gpt
from generate_python_code import generate_python_code

def solve_math_problem_UNSAFE(problem):
    python_code = generate_python_code(f"""{problem}

- Please write your solution as a single expression that can be passed to python's eval() function
- If possible, please write it such that it requires 0 or as few as possible imports
    """)

    print(f"\nPython code generated for {problem}:")
    print(python_code)

    result = eval(python_code)
    print(f"\nResult of running the python code on {problem}:")
    print(result)

    return result

if __name__ == "__main__":
    solve_math_problem_UNSAFE(input("What math problem would you like me to solve? Please give me a problem in plain language, like 'Find the factorial of a number'. "))