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
