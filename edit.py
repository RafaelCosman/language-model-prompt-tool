"""
This module contains functions to edit text.
"""

from helper_functions import gpt

def edit(text):
    """
    Function to edit the text to be as clear and concise as possible.

    Parameters
    ----------
    text : str
        The text to be edited.

    Returns
    -------
    str
        The edited version of the input text.
    """
    output = gpt(f"""
Please edit the following text to be as clear and concise as possible:

{text}

""")

    print("Edited version of input text:")
    print(output)

    return output

if __name__ == "__main__":
    edit(input("What text would you like me to edit? Please paste it here. I will make it as clear and concise as possible."))