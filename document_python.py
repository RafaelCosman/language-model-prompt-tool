from gpt import gpt

def document_python_file(python_code):
    output = gpt(f"""
================
Example
================
If the Python code was:

from helper_functions import ask

def generate_scene(play_name, scenes_list, scene_name):
    output = ask(f\"\"\"
We are writing a play called {{play_name}}

The full scene list is:

{{scenes_list}}

Please write the scene about {{scene_name}}.

Scene:

\"\"\")

    print(f"Scene output for {{scene_name}}:")
    print(output)

    return output

def generate_play(play_name):
    raw_scenes_list = ask(f\"\"\"
Please generate a list of scenes for a play called {{play_name}}.
The scenes should follow the logical order of the plot and should create a varied and engaging experience for a viewer.

Scenes:


\"\"\")

    scenes_list = raw_scenes_list.split("\n")
    print(f"Scenes list for play {{play_name}}:")
    print(scenes_list)
    
    output = ""
    for scene_name in scenes_list:
        scene_text = generate_scene(play_name, scenes_list, scene_name)
        output += scene_text
    
    print(f"\nPlay output for {{play_name}}:")
    print(output)

    return output

if __name__ == "__main__":
    generate_play(input("What would you like me to write a play about? You can give me a single topic like 'True Love'. "))


The correct documented version of this code would be:

\"\"\"
This module contains functions to generate a play
\"\"\"

from helper_functions import ask

def generate_scene(play_name, scenes_list, scene_name):
    \"\"\"
    Function to generate a scene for the play

    Parameters
    ----------
    play_name : str
        The name of the play
    scenes_list : list
        A list of all the scenes in the play
    scene_name : str
        The name of the scene to be generated

    Returns
    -------
    str
        The text of the scene
    \"\"\"
    output = ask(f\"\"\"
We are writing a play called {{play_name}}

The full scene list is:

{{scenes_list}}

Please write the scene about {{scene_name}}.

Scene:

\"\"\")

    print(f"Scene output for {{scene_name}}:")
    print(output)

    return output

def generate_play(play_name):
    \"\"\"
    Function to generate an entire play

    Parameters
    ----------
    play_name : str
        The name of the play

    Returns
    -------
    str
        The text of the entire play
    \"\"\"
    raw_scenes_list = ask(f\"\"\"
Please generate a list of scenes for a play called {{play_name}}.
The scenes should follow the logical order of the plot and should create a varied and engaging experience for a viewer.

Scenes:


\"\"\")

    scenes_list = raw_scenes_list.split("\n")
    print(f"Scenes list for play {{play_name}}:")
    print(scenes_list)
    
    output = ""
    for scene_name in scenes_list:
        scene_text = generate_scene(play_name, scenes_list, scene_name)
        output += scene_text
    
    print(f"\nPlay output for {{play_name}}:")
    print(output)

    return output

if __name__ == "__main__":
    generate_play(input("What would you like me to write a play about? You can give me a single topic like 'True Love'. "))

================
Example
================
If the Python code was:

from helper_functions import ask

def edit(text):
    output = ask(f\"\"\"
Please edit the following text to be as clear and concise as possible:

{{text}}

\"\"\")

    print("Edited version of input text:")
    print(output)

    return output

if __name__ == "__main__":
    edit(input("What text would you like me to edit? Please paste it here. I will make it as clear and concise as possible."))


The correct documented version of this code would be:

from helper_functions import ask

def edit(text):
    \"\"\"
    Function to edit the text to be as clear and concise as possible

    Parameters
    ----------
    text : str
        The text to be edited

    Returns
    -------
    str
        The edited version of the input text
    \"\"\"
    output = ask(f\"\"\"
Please edit the following text to be as clear and concise as possible:

{{text}}

\"\"\")

    print("Edited version of input text:")
    print(output)

    return output

if __name__ == "__main__":
    edit(input("What text would you like me to edit? Please paste it here. I will make it as clear and concise as possible."))
===============================================

Please document the following python code.
- This documentation process should not change the code AT ALL
- It should add function docstrings, module docstrings, and comments, where appropriate
- It should use best practices for documenting Python

Python code:

{python_code}

Documented version of the Python Code:

""")

    print(f"Documented python code:")
    print(output)

    return output

def document_python_file_inplace(file_path):
    with open(file_path, "r") as file:
        python_code = file.read()

    documented_python_code = document_python_file(python_code)

    with open(file_path, "w") as file:
        file.write(documented_python_code)

if __name__ == "__main__":
    document_python_file_inplace(input("Please specify the file path of the python file that you would like documented. "))