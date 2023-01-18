from helper_functions import ask

def edit(text):
    output = ask(f"""
Please edit the following text to be as clear and concise as possible:

{text}

""")

    print("Edited version of input text:")
    print(output)

    return output

if __name__ == "__main__":
    edit(input("What text would you like me to edit? Please paste it here. I will make it as clear and concise as possible."))