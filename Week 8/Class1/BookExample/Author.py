class Author:
    """This class repreents an Author"""
    def __init__(self, name, pen):
        self.name = name

        # This is the nickname of the....
        self.pen_name = pen

    def printpen(self):

        print(self.pen_name)
