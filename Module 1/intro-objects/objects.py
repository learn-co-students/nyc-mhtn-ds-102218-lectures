# OOP - consists of classes and instances of those classes
# class
    # factory
        # Where classes allow us to construct instances of a data type
        # construct unique instances of a class
        # Dog()
    # blueprint
        # define the capabilities (the methods) of those instances
# instances of that class
    # share methods
    # unique data
        # name 'fido' != 'avalanche'


# look at the style guide for airbnb
    # parentheses after dog
    # camelcase vs snake case

class Dog:
    def _begin_running(self):
        print('putting on my shoes')

    def runs(self, distance):
        self._begin_running()
        print('I am running ' + distance)
