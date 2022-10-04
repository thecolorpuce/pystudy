"""
8-9. Messages: Make a list containing a series of short text messages. Pass the
list to a function called show_messages(), which prints each text message.
"""

def show_messages(messages):
    """Simple function to print out each message in a list."""
    
    for message in messages:
        print(message)

messages = ['lol', 'r u ok?', 'lmao what a ting!', 'Hey there BridgeBoy!', 'Life before death. Strength before weakness. Journey before destination.']

show_messages(messages)