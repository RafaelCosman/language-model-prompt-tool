from helper_functions import ask

def editor(text):
    query = f"""
Please edit the following text to be as clear and concise as possible:

{text}

"""

    output = ask(query)
    print(f"Edited version of input text:")
    print(output)

    return output