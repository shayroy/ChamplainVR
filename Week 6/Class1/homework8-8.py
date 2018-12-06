"""8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop."""

def make_album(artist_name, album_title):
    """Return a dictionary of information about albums."""
    entry = {'artist':artist_name, 'title':album_title}
    return entry

while True:

    print("\nPlease tell me the name of an artist and the title of one of their albums. ")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist name: ")
    if artist =='q':
        break

    album = input("Album title: ")
    if album == 'q':
        break

    print(make_album(artist, album))






# entry0 = make_album('The Beatles', 'Abby Road')
# entry1 = make_album('The Rolling Stones', 'Exile on Main St.')
# entry2 = make_album('Joni Mitchell', 'Blue')
# entry3 = make_album('Nirvana', 'Nevermind', '8')

# print(entry0)
