"""8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop."""

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

#I actually made 8-8 while making 8-7