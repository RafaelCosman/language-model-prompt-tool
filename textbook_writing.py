from helper_functions import ask

def outline_textbook(topic):
    query = f"""
Please list the 6-12 (absolute max of 12) chapters for a textbook on {topic}.
These chapters are numbered 1., 2., 3., etc.

Outline:

"""

    output = ask(query)
    print(f"Textbook Outline for topic {topic}:")
    print(output)

    return output

def outline_textbook_chapter(topic, outline, section):
    query = f"""
We are writing a textbook on {topic}. The chapters are:

{outline}

Your job is to write the outline for chapter {section}.
- This outline can include anywhere from 3-10 sub-points.
- These sub-points should be enumerated A., B., C., etc. and should NOT have sub-sub-points within them.

{section} Outline:

"""

    output = ask(query)
    print(f"\n{section}")
    print(output)

    return output

def write_subsection(topic, outline, chapter, chapter_outline, subsection):
    query = f"""
We are designing a course on {topic}. The overall outline is:

{outline}

The outline for chapter {chapter} is

{chapter_outline}

Your job is to write subsection {subsection}.
- This subsection could be anywhere from a few paragraphs to several pages of text.
- Please include details, examples, and practice problems where appropriate.
- Please use markdown wherever you can, including code blocks (```js), bulleted lists (- item), enumerated lists (1. item), bold, italics, sub-sub-headings (### heading) and more.

{subsection} Content:

"""

    output = ask(query)
    print(f"\n## {subsection}\n")
    print(output)

    return output

def write_textbook(topic):
    textbook_outline = outline_textbook(topic)

    section_and_outlines = [(section, outline_textbook_chapter(topic, textbook_outline, section)) for section in textbook_outline.splitlines()]

    for (section, section_outline) in section_and_outlines:
        print()
        print("#", section)
        print()
        written_texts = [(section, subsection, write_subsection(topic, textbook_outline, section, section_outline, subsection)) for subsection in section_outline.splitlines()]

if __name__ == "__main__":
    write_textbook(input("What would you like to write a textbook on? You can just give me a single topic, like 'Bioethics'. "))