from lib.flight import Flight
class Airline:

    _all = []

    def __init__(self, name):
        # self
        Airline._all.append(self)
        self._name = name

    @property
    def name(self):
        return self._name

    @classmethod
    def all(cls):
        print(cls)
        return Airline._all

    @property
    def flights(self):
        # a. get a list of all flights
        # [<seven_forty_six>, <six_forty_six>, ]
        all_flights = Flight.all()
        # b. see which flights have an airline that pertains to that airline
        selected_flights = []
        for flight in all_flights:
            if flight.airline == self:
                selected_flights.append(flight)
        return selected_flights
