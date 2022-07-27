"""8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album’s dictionary. Make at least
one new function call that includes the number of songs on an album."""

def make_album(artist_name, album_title, songs=0):
    """Return a dictionary with the appropriate information"""
    album = {'artist': artist_name, 'album': album_title}
    return album

while True:
    print("Please enter an artist and album1: ")
    print("Enter 'Q' to quit at any time")
    artist = input("Artist: ")
    if artist == 'q':
        break
    
    album = input("Album ")
    if album == 'q':
        break
    
    album1 = make_album(artist, album)
    
while True:
    print("Please enter an artist and album2: ")
    print("Enter 'Q' to quit at any time")
    artist = input("Artist: ")
    if artist == 'q':
        break
    
    album = input("Album ")
    if album == 'q':
        break
    
    album2 = make_album(artist, album)
    
while True:
    print("Please enter an artist and album2: ")
    print("Enter 'Q' to quit at any time")
    artist = input("Artist: ")
    if artist == 'q':
        break
    
    album = input("Album ")
    if album == 'q':
        break
    
    album3 = make_album(artist, album)
    
while True:
    print("Please enter an artist and album2: ")
    print("Enter 'Q' to quit at any time")
    artist = input("Artist: ")
    if artist == 'q':
        break
    
    album = input("Album ")
    if album == 'q':
        break
    song = input('#ofsongs')
    if song == 'q':
        break
    album4 = make_album(artist, album, song)
print(album1)
print(album2)
print(album3)
print(album4)