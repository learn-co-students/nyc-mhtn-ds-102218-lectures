from environment import *

twa = Airline('twa')
delta = Airline('delta')
fivefortyfive = Flight(545)
six_forty_six = Flight(646)
seven_forty_six = Flight(746)

fivefortyfive.airline = twa
six_forty_six.airline = twa
seven_forty_six.airline = delta

pilot.airlines
    # [<airline>]
airline.pilots
    # [<pilot>, <pilot>]

# airline.flights
# flight.pilot
# airline.pilots

# pilot.flights
# pilot.airlines

# flight
# pilot has many airlines
# airline has many pilots

# pilot has many flights
# flight belongs to pilot
# airline
# 1. answer the question with brain
# 2. deconstruct brain
    # a. get a list of all flights
    # b. see which flights have an airline that pertains to that airline

# twa.flights
# # [<fivefortyfive>, <six_forty_six>]
#
# delta.flights
# # [<seven_forty_six>]
