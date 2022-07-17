#6-6. Polling: Use the code in favorite_languages.py (page 97).

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

untaken = ['riley', 'ean', 'phil']

for val in untaken:
    if val in favorite_languages:
        print(f"Thanks for taking the poll {val.title()}.")
    else:
        print(f"Please take the poll {val.title()}.")