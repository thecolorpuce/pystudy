aliens = []

#Make 30 green aliens

for alien in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#Change the first 3 aliens to the Yellow Setting

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
        print('Test Output') 
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
        print('TEST2')

#Show the first 5 aliens

for alien in aliens[:5]:
    print(alien)
    print("\n")

print('....')

#Show how many aliens have been created.

print(f"Total number of aliens: {len(aliens)}")