"""
8-10. Sending Messages: Start with a copy of your program from 
Exercise 8-9. Write a function called send_messages() that prints 
each text message and moves each message to a new list called sent_messages 
as it’s printed. After calling the function, print both of your lists to make 
sure the messages were moved correctly.
"""

#This is appropriate for the sake of simplicity
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

