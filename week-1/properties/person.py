class Person:

    def __init__(self, first, last):
        self._interests = ['baby food']
        self._first_name = first
        self._last_name = last





    def get_first_name(self):
        return self._first_name


    def set_first_name(self, first_name):
        # me referencing the reciever of the method call
        # whatever is to the left of the dot

        self._first_name = first_name.capitalize()
    first_name = property(get_first_name, set_first_name)
    

    def add_interest(self, interest):
        upper_interest = interest.capitalize()

        self._interests.append(upper_interest)




    def last_name(self, last_name):
        return last_name

    def full_name(self, first_name, last_name):
        return first_name + last_name

# bob = Person()
# bob.first_name()
