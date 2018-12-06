class Cat:
    name = ""
    age = 0
    registered = False

# def is function within class
# need two underscores init two underscores
# first variable refers to itself, Brendan usually called self. It is ignored (indicated by purple) but is needed.
# What is contained within self (the cat) is name and age.

    def __init__(self, input_name, input_age):
        self.name = input_name
        self.age = input_age

        if input_age > 2:
            self.registered = True

# To give this some life, we can define multiple functions in the class.
# A function name is usually a verb.

    def meow(self, number_time):
        for m in range(number_time):
            print("Meow")

    def meow(self, number_time, phrase="", tone):
        for m in range(number_time):
            print("Meow" + phrase)
# The second def meow overloads the function. Not needed or really works here. Brenden will
# come back with better implementation. It is a more advanced feature to call or
# implement the most appropriate method.
# Inside function meow, want to be able to access all the things in the Class, although in this case, we are not
# taking anyting else.

c1 = Cat("Jack", 2)
# this is intatiation. In other languages called constructor. Brendan wants the cat to automatically registered if
# greater than 2 years old.
c2 = Cat("Samantha", 9)
print("Cat c1 registation state is " + str(c1.registered))
print("Cat c2 registation state is " + str(c2.registered))
#use dot to evoke method
c1.meow(5, "TEST", None)




