aliens = []

#Make 30 aliens

for val in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#Make first yellow

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] == 'yellow'
        alien['speed'] == 'medium'
        alien['points'] == 10

#Show first 5 
for val in aliens[:5]:
    print(val)

print("...")

#Show total number of aliens created
print(f"Total number of aliens: {len(aliens)}")

