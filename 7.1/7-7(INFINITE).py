"""
7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press
ctrl-C or close the window displaying the output.)
"""

lo = True
counter = 0
bigList = []

while lo is True:
    counter += 1
    bigList.append(counter)
    for i in bigList:
        print(f"{i}")
    bigList.append(bigList)