import os

dirname = "TestDir"

def create_dir_if_not_existing(name):
    """Checks the existance of a directory and creates it if necessary."""
    if not os.path.isdir(name): # if not statement is negation of if statement.
        # can also use and add another part, such as another if not
        os.mkdir(name)
        print("Directory " + name + "created.")

    else:
        print("The supplied name is a directory that already exists.")

create_dir_if_not_existing(dirname)

