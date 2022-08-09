"""8-11. Archived Messages: Start with your work 
from Exercise 8-10. Call the function send_messages() 
with a copy of the list of messages. After calling 
the function, print both of your lists to show that 
the original list has retained its messages."""

def messages_messages(messages):
    """We're just trying to print some messages here. 
    Unfortunately, I corrode with haste"""
    
    for message in messages:
        print(messages)

def sendMessages(messages, printedMessages):
    """What's this, am I unclear? Yes"""
    while messages:
        message = messages.pop()
        printedMessages.append(message)

messages = ['one', 'two', 'three']
printedMessage = []