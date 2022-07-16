#4-10. Slices: Using one of the programs you wrote in this chapter, add several
#lines to the end of the program that do the following:

cubes = [value**3 for value in range(1, 11)]

firstCubes = cubes[:3]
secCubes = cubes[3:6]
thirdCubes = cubes[6:]


#print the first 3
for val in firstCubes:
    print(val)

#print middle 3
for val in secCubes:
    print(val) 

#print the remainder (Should be 3, but it's the spirit that matters here)
for val in thirdCubes:
    print(val) 
