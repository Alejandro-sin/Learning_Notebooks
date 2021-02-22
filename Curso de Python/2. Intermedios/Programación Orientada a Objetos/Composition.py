'''


Este chunk tiene como proósito estudiar lo que tiene que ver con
la creación de composiciones.

'''


class Other (object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")


class Child(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()