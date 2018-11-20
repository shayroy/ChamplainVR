# While loop means you do something and if the test is true it keeps running and if not it stops. test - do.
# the += is to avoid it running for ever. Equivalent to a=a+1
# if running for ever, press stop

a=1
while a < 10:
    print(a)
    a +=1

# next example Message being equal to nothing at least creates message. (I commented out to avoid interfering with the next application
# When I tried it Nov 19 it printed out "quit" when I entered "quit". Shouldn't it have not printed "quit"?
#while message != 'quit':
#    message = input("Enter command :")
#    print(message)

#remember to press enter before finishing an application for it to run correctly

# try to switch it from a test-do to a do-test, the opposite. There is a logic to have it do something first before testing. Trick is to run the while loop
# infinately with while True.
# ctrl/ will comment out selection.
#When I tried on Nov 19 it printed out "quit" after I entered quit, which is the intent, but it kept working rather than breaking.

while True:
    message = input ("Enter command :")
    print(message)
    if message == "quit":
        break
#



