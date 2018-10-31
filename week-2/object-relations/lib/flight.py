class Flight:
    _all = []

    def __init__(self, number):
        Flight._all.append(self)
        self._number = number

    @classmethod
    def all(cls):
        print(cls)
        return Flight._all
        
    @property
    def number(self):
        return self._number
    # number = property(number)

    @number.setter
    def number(self, number):
        self._number = number + 2
    # number = number.setter(set_number)
    #
    @property
    def airline(self):
        return self._airline

    # airline = property(airline)

    @airline.setter
    def airline(self, airline):
        self._airline = airline

    # airline = airline.setter(add_airline)

# flight belongs to an airline
# airline has many flights
