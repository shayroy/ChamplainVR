"""8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number
of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album."""

def make_album(artist_name, album_title, number_of_tracks=0):
    """Return a dictionary of information about albums."""
    entry = {'artist':artist_name, 'title':album_title, 'tracks':number_of_tracks}
    return entry

entry0 = make_album('The Beatles', 'Abby Road')
entry1 = make_album('The Rolling Stones', 'Exile on Main St.')
entry2 = make_album('Joni Mitchell', 'Blue')
entry3 = make_album('Nirvana', 'Nevermind', '8')

print(entry0, entry1, entry2, entry3)







