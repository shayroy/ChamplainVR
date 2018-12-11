import random

random_number = random.randint(1, 101)
print(random_number)

guess = input("Please guess a number between 1 and 100: ")
counter = 0
while counter <= 5:

    for x in guess:
        if int(x) < random_number:
            print("Wrong guess, you guessed too low (attempt" + str(counter) + "): "+ str(guess))
            counter = counter + 1

        if int(x) > random_number:
            print("Wrong guess, you guessed to high .")
            counter = counter + 1

        if int(x) == random_number:
            print("Correct! You win.")
            break

        if counter == 6:
            break

    x = int(x) + 1

