class Pilot:
    _all = []

    def __init__(self, name):
        Pilot._all.append(self)
        self._name = name

    @classmethod
    def all(cls):
        print(cls)
        return Pilot._all

    @property
    def name(self):
        return self._name
