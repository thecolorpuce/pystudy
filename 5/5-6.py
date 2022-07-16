#5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
#stage of life. Set a value for the variable age, and then:

age = 90

#less than 2 years old
if age < 2:
    print("You are a baby")
elif age >= 2 and age < 4:
    print("You are a toddler")
elif age >= 4 and age < 13:
    print("You are a kid")
elif age >= 13 and age < 20:
    print("You are a teenager")
elif age >= 20 and age < 65:
    print("You are an adult")
elif age >= 65:
    print("You are an elder")