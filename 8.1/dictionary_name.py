import myLib as m

person = m.build_person('riley', 'asp', age=28)

for k, v in person.items():
    print(f"{k} {v}")