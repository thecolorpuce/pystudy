"""
8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album’s dictionary. Make at least
one new function call that includes the number of songs on an album.
"""

def make_album(artist_name, album_title, number_songs=None):
    """Create a dictionary storing the provided information"""
    
    dictionary = {}
    
    dictionary['artist_name'] = artist_name
    dictionary['album_title'] = album_title
    dictionary['number_songs'] = number_songs
    
    return dictionary

album1 = make_album('The Midnight', 'A Name', 13)
album2 = make_album('Gunship', 'Dark All Day')
album3 = make_album('Eluveitie', 'Somnos', 1)

print(album1)
print(album2)
print(album3)