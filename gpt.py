import lmtk

# Helper functions
chat = lmtk.modes.raw_gpt.RawGPTMode()

def gpt(query):
    return "".join(chat.ask(query))