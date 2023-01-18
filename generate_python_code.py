from helper_functions import ask

def generate_python_code(problem):
    output = ask(f"""
Please generate python code to {problem}.
- The code should be as concise as possible
- It should minimize side effects and never take dangerous actions like deleting files etc.

Python code:
""")

    print(f"Python Code for {problem}:")
    print(output)

    return output

if __name__ == "__main__":
    generate_python_code(input("What would you like to generate python code for? For example, you could say 'Accept an integer and list its factors'. "))