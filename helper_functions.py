import lmtk

# Helper functions
chat = lmtk.modes.raw_gpt.RawGPTMode()

def gpt(query):
    reply_generator = chat.ask(query)
    reply = "".join([token for token in reply_generator])
    return reply