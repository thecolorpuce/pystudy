favorite_languages = {
    'jen': 'python', 
    'sarah':'c',
    'edward': 'ruby',
    'phil': 'python'
}

#language = favorite_languages['sarah'].title()
#print(f"Sarah's favorite language is {language.title()}")

#****Modifting this to use a loop. Keeping previous code commented for reference

for k, v in favorite_languages.items():
    print(f"{k.title()}'s favorite languake is {v.title()}")