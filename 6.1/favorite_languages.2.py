favorite_languages = {
    'jen': 'python', 
    'sarah':'c',
    'edward': 'ruby',
    'phil': 'python'
}

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language.title()}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")