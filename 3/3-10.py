#List of stuff. I'll just do some 40k chapters

chapter = ['salemanders','fists','angels','scars']

#From here on out, I'm making use of each function from earlier

print(f"\n Welcome to the table {chapter[0].title()}")

#Let's go through the effort of adding

chapter.append('malevolant')

print(f"\n The newest chapter appended was {chapter[4].title()}")
print(f"\n To be fair {chapter[4].title()} are a bunch of dicks, so let's remove them")

cya = chapter.pop()

print(f"\n Goodbye {cya.title()}")

print(f"\n Why not get rid of {chapter[2].title()} as well?")

remove = "angels"
chapter.remove(remove)

print(f"\n Here is the new list {chapter}")


print("Here is a sorted list")
print(sorted(chapter,reverse=True))