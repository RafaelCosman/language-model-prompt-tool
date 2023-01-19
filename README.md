# Language Model Prompt Tool (LMPT)

LMPT is a library with functions to construct powerful, multi-step language model prompts. For example, using the write_book() function, you can ask in a single function call ask an arbitrary language model to write an entire book for you. This, under the hood, uses a structured series of prompts designed for this purpose that you can find in the write_book.py file.

# Installation

1. Install the LMTK library using `pip install -U lmtk`

Please see [the LMTK documentation](https://github.com/veered/lmtk) if you have any issues with that install

2. Run the relevant script from this repo using ones of the examples below.

_If you have any issues with installing or using this code, please reach out to me (rafaelcosman@alumni.stanford.edu)._

# Example Usage

## Generation

### Textbooks - textbook_writing.py

Just run:
`python textbook_writing.py`

You should then see on your prompt:
`What would you like to write a textbook on? You can just give me a single topic, like 'Bioethics'.`

Let's say you input `Bioethics`.

You should then see on your prompt:

1. A list of the chapters for the Bioethics textbook
2. An outline for each chapter
3. Each chapter written out, section by section

This third step can take 30-60 minutes, please be patient. It's important that your internet connection is not interrupted during this process! Note also that textbook generation requires a LOT of queries to the OpenAI API, so if you have a limited budget this may eat into it very quickly.

### Journals - journal_writing.py

Similar to writing textbooks, just run:
`python journal_writing.py`

You should then see in your prompt:
`What would you like me to write a journal about? You can give me a signle topic like 'Geopolitics'.`

Let's say you input `Geopolitics`.

You should then see on your prompt:

1. A list of the journal article topics
2. Each journal article written out in turn

## Editing and Evaluation

### Editing - edit.py

edit.py will edit text to be clear and concise. It is used by other functions such as journal/article generation. To use it directly, just run `python edit.py`

<img width="857" alt="image" src="https://user-images.githubusercontent.com/1255944/213333190-43c1cfa7-1869-4d0a-9e8a-10e2bdecea77.png">

