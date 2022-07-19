currentNumber = 0

while currentNumber < 10:
    currentNumber += 1
    if currentNumber % 2 == 0:
        continue
    
    print(currentNumber)