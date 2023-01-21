"""
This module contains functions to generate a play.
"""

from helper_functions import gpt

def generate_scene(play_name, scenes_list, scene_name):
    """
    Function to generate a scene for the play.

    Parameters
    ----------
    play_name : str
        The name of the play.
    scenes_list : list
        A list of all the scenes in the play.
    scene_name : str
        The name of the scene to be generated.

    Returns
    -------
    str
        The text of the scene.
    """
    output = gpt(f"""
We are writing a play called {play_name}

The full scene list is:

{scenes_list}

Please write the scene about {scene_name}.

Scene:

""")

    print(f"Scene output for {scene_name}:")
    print(output)

    return output

def generate_play(play_name):
    """
    Function to generate an entire play.

    Parameters
    ----------
    play_name : str
        The name of the play.

    Returns
    -------
    str
        The text of the entire play.
    """
    raw_scenes_list = gpt(f"""
Please generate a list of scenes for a play called {play_name}.
The scenes should follow the logical order of the plot and should create a varied and engaging experience for a viewer.

Scenes:


""")

    scenes_list = raw_scenes_list.split("\n")
    print(f"Scenes list for play {play_name}:")
    print(scenes_list)
    
    output = ""
    for scene_name in scenes_list:
        scene_text = generate_scene(play_name, scenes_list, scene_name)
        output += scene_text
    
    print(f"\nPlay output for {play_name}:")
    print(output)

    return output

if __name__ == "__main__":
    generate_play(input("What would you like me to write a play about? You can give me a single topic like 'True Love'. "))