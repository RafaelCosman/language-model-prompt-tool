import collect_documentation

def update_collected_docstrings():
    """
    Function to update collected_docstrings.txt
    """
    collected_docstrings = collect_documentation.collect_documentation()

    with open("collected_docstrings.txt", "w") as file:
        file.write(collected_docstrings)

if __name__ == "__main__":
    update_collected_docstrings()