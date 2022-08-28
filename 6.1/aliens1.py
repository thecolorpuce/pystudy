aliens = []

#Make 30 green aliens

for v in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#Show the first 5 aliens

for v in aliens[:5]:
    print(aliens)
    print("\n")

print('....')

#Show how many aliens have been created.

print(f"Total number of aliens: {len(aliens)}")