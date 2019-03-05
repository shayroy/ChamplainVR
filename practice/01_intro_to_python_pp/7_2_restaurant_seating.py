# Program that askes the user how many people are in their dinner group. If the answer in more than eight,
# print a message saying they'll have to wait for a table. Otherwise, report that their table is ready.
group_size = int(input('Please tell me how many people are in your group: '))

if group_size <= 8:
    print('Your table is ready.')
elif group_size >= 9:
    print('I am sorry, but you will have to wait for a table.')
