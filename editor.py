from helper_functions import ask

def editor(text):
    output = ask(f"""
Please edit the following text to be as clear and concise as possible:

{text}

""")

    print("Edited version of input text:")
    print(output)

    return output