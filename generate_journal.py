from helper_functions import ask

from editor import edit

def generate_article(topic):
    output = ask(f"""
Please write an article about {topic}.

Article:

""")

    print(f"\nArticle output for topic {topic}:")
    print(output)
    
    edited_output = editor(output)
    print(f"\nEdited article output for topic {topic}:")
    print(edited_output)

    return edited_output

def generate_journal(topic):
    raw_topics_list = ask(f"""
Please generate a list of topics for articles to be included in a journal on {topic}.

Topics:


""")

    topics_list = raw_topics_list.split("\n")
    print(f"Topics list for journal on {topic}:")
    print(topics_list)
    
    output = ""
    for topic in topics_list:
        article = generate_article(topic)
        output += article
    
    print(f"\nJournal output for topic {topic}:")
    print(output)

    return output

if __name__ == "__main__":
    generate_journal(input("What would you like me to write a journal about? You can give me a signle topic like 'Geopolitics'. "))