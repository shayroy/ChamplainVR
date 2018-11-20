# page 50

print("Store at least 5 locations in a list . Make sure the list is not in alphabetical order.")
places = ['iceland', 'scotland', 'sri lanka', 'russia', 'bhutan']
print("Print your list in its original order . Don’t worry about printing the list neatly, just print it as a raw Python list.")
print(places)
print("Use sorted() to print your list in alphabetical order without modifying the actual list.")
print(sorted(places))
print("Show that your list is still in its original order by printing it again.")
print(places)
print("Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.")
print(sorted(places, reverse=True))
print("Show that your list is still in its original order by printing it again.")
print(places)
print("Use reverse() to change the order of your list. Print the list to show that its order has changed.")
places.reverse()
print(places)
print("Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.")
places.reverse()
print(places)
print("Use sort() to change your list so it’s stored in alphabetical order . Print the list to show that its order has been changed.")
places.sort()
print(places)
print("Use sort() to change your list so it’s stored in reverse alphabetical order . Print the list to show that its order has changed .")
places.sort(reverse=True)
print(places)



