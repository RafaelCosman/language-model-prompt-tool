from helper_functions import ask

def generate_scene(play_name, scenes_list, scene_name):
    output = ask(f"""
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
    raw_scenes_list = ask(f"""
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