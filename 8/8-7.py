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

upFlag = True

def makeAlbum(artist_name, album_name, song_number=None):
    """Make a dictionary of the artist, album, and # of songs"""
    album = {'artist': artist_name, 'album': album_name}
    if song_number:
        album['song_number'] = song_number
    return album

while upFlag:
    print("We're going to make 3 albums")
    
    print("Album 1: ")
    artName = input("Artist: ")
    albName = input("Album: ")
    songs = input("Songs: ")
    
    album1 = makeAlbum(artName, albName, songs)
    
    print("Album 2: ")
    artName = input("Artist: ")
    albName = input("Album: ")
    songs = input("Songs: ")
    
    album2 = makeAlbum(artName, albName, songs)
    
    print("Album 3: ")
    artName = input("Artist: ")
    albName = input("Album: ")
    songs = input("Songs: ")
    
    album3 = makeAlbum(artName, albName, songs)
    
    print("Would you like to quit?: ")
    quit = input('q: ')
    if quit == 'q':
        upFlag = False
        break

print(album1)
print(album2)
print(album3)