class AmpleHills:
    def __init__(self, location):
        # reject
        # coerce
        # {'address': '', zip: integer}
        self.validate_location(location)
        self._location = location

    @property
    def location(self):
        return 'zip: {zipcode}'.format(zipcode = self._location['zipcode'])
#
    # get_location = property(location)
    # decorator pattern

    @location.setter
    def location(self, location):
        self.validate_location(location)
        self._location = location

    # whatever = location.setter(location)
# manhattan.set_location

    def validate_location(self, location):
        raise Exception('must be of type dict') if not isinstance(location, dict)
