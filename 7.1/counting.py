from multiprocessing import current_process


current_number = 1

def inc5(number):
    while number <= 5:
        print(number)
        number += 1

inc5(current_number)