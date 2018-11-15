# -------------------
# prints a list from 0 to 9. (If range (10) is a group of apples, this allows us to decide what to do with each apple.)
for a in range(10):
    print(a)

# ----------------------------------
# can use break and continue within ranges

#for example, to print 012456789, can put continue before 3
#to print 012, can put break before 3
#basic if statement if a == 3: do something
#if and for need tabs on following data lines
#need double equal signs for comparison rather than assigning

#break example (stopping at 3)

for a in range(10):
    if a==3:
        break
    print(a)

#continue example (skips 3)
#refactor menu command will change a value a to b
for b in range (10):
    if b==3:
        continue
    print (b)



