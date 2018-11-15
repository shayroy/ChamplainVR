# While loop means you do something and if the test is true it keeps running and if not it stops. test - do.
# the += is to avoid it running for ever. Equivalent to a=a+1
# if running for ever, press stop

a=1
while a < 10:
    print(a)
    a +=1

# next example Message being equal to nothing at least creates message. (I commented out to avoid interfering with the next application
#message = ""
#while message != 'quit':
#    message = input("Enter command :")
#    print(message)

#remember to press enter before finishing an application for it to run correctly

# try to switch it for a do - test. There is a logic to have it do something first before testing. Trick is to run the while loop
# infinately with while True.
# ctrl/ will comment out selection.

while True:
    message = input ("Enter command :")
    print(message)
    if message == "quit":
        break
#



