#5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
#as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.

num = [1,2,3,4,5,6,7,8,9]

for val in num:
    if val == 1:
        print(f"{val}st")
    elif val == 2:
        print(f"{val}nd")
    elif val == 3:
        print(f"{val}rd")
    elif val == 4:
        print(f"{val}th")
    elif val == 5:
        print(f"{val}th")
    elif val == 6:
        print(f"{val}th")
    elif val == 7:
        print(f"{val}th")
    elif val == 8:
        print(f"{val}th")
    elif val == 9:
        print(f"{val}th")
    else:
        print("Please enter a valid integer")