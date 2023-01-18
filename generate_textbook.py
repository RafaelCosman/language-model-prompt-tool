from helper_functions import ask

def generate_textbook_outline(topic):
    output = ask(f"""
Please list the 6-12 (absolute max of 12) chapters for a textbook on {topic}.
These chapters are numbered 1., 2., 3., etc.

Outline:

""")

    print(f"Textbook Outline for topic {topic}:")
    print(output)

    return output

def generate_textbook_chapter_outline(topic, textbook_outline, section):
    output = ask(f"""
We are writing a textbook on {topic}. The chapters are:

{textbook_outline}

Your job is to write the outline for chapter {section}.
- This outline can include anywhere from 3-10 sub-points.
- These sub-points should be enumerated A., B., C., etc. and should NOT have sub-sub-points within them.

{section} Outline:

""")

    print(f"\n{section}")
    print(output)

    return output

def generate_subsection(topic, textbook_outline, chapter, chapter_outline, subsection):
    output = ask(f"""
We are designing a course on {topic}. The overall textbook outline is:

{textbook_outline}

The outline for chapter {chapter} is

{chapter_outline}

Your job is to write subsection {subsection}.
- This subsection could be anywhere from a few paragraphs to several pages of text.
- Please include details, examples, and practice problems where appropriate.
- Please use markdown wherever you can, including code blocks (```js), bulleted lists (- item), enumerated lists (1. item), bold, italics, sub-sub-headings (### heading) and more.

{subsection} Content:

""")

    print(f"\n## {subsection}\n")
    print(output)

    return output

def generate_textbook(topic):
    textbook_outline = generate_textbook_outline(topic)

    section_and_outlines = [(section, generate_textbook_chapter_outline(topic, textbook_outline, section)) for section in textbook_outline.splitlines()]

    for (section, section_outline) in section_and_outlines:
        print()
        print("#", section)
        print()
        written_texts = [(section, subsection, generate_subsection(topic, textbook_outline, section, section_outline, subsection)) for subsection in section_outline.splitlines()]

if __name__ == "__main__":
    generate_textbook(input("What would you like to write a textbook on? You can just give me a single topic, like 'Bioethics'. "))