from helper_functions import ask

from editor import editor

def write_article(topic):
    query = f"""
Please write an article about {topic}.

Article:

"""

    output = ask(query)
    print(f"\nArticle output for topic {topic}:")
    print(output)
    
    edited_output = editor(output)
    print(f"\nEdited article output for topic {topic}:")
    print(edited_output)

    return edited_output

def write_journal(topic):
    query = f"""
Please generate a list of topics for articles to be included in a journal on {topic}.

Topics:


"""

    topics_list = ask(query).split("\n")
    print(f"Topics list for journal on {topic}:")
    print(topics_list)
    
    output = ""
    for topic in topics_list:
        article = write_article(topic)
        output += article
    
    print(f"\nJournal output for topic {topic}:")
    print(output)

    return output

if __name__ == "__main__":
    write_journal(input("What would you like me to write a journal about? You can give me a signle topic like 'Geopolitics'. "))