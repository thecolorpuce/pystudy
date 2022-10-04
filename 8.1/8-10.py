"""
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it’s printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly.
"""

def show_messages(messages, sentMessages):
    """Simple function to print out each message in a list."""
    
    while messages:
        currentMessage = messages.pop()
        print(currentMessage)
        sentMessages.append(currentMessage)

messages = ['lol', 'r u ok?', 'lmao what a ting!', 'Hey there BridgeBoy!', 'Life before death. Strength before weakness. Journey before destination.']
sentMessages = []

show_messages(messages, sentMessages)

print(f"\n'messages' list: \n\t{messages}")
print(f"\n'sentMessages' list: \n\t{sentMessages}")