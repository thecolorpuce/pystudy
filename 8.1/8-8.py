"""
8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
"""


def make_album(artist_name, album_title, number_songs=None):
    """Create a dictionary storing the provided information"""
    
    dictionary = {}
    
    dictionary['artist_name'] = artist_name
    dictionary['album_title'] = album_title
    dictionary['number_songs'] = number_songs
    
    return dictionary

music = []
questioning = True

while questioning is True:
    artist_name = input("\nPlease enter the artist's name: ")
    album_title = input("\nPlease enter the album's title: ")
    multiple_songs = input("\nWould you like to specify how many songs are on the album? (yes/no)")
    if multiple_songs == 'y':
        number_songs = input("\nHow many songs?: ")
        music.append(make_album(artist_name, album_title, multiple_songs))
    else:
        music.append(make_album(artist_name, album_title))
        
    print("\nThank you!")
    print("\nThis is the current library you have added")
    print(f"\n\t{music}")
    again = input("\nWould you like to add another album? (yes/no)?: ")
    if again == 'n':
        break



