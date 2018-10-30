from environment import *

twa = Airline('twa')
delta = Airline('delta')
fivefortyfive = Flight(545)
six_forty_six = Flight(646)
seven_forty_six = Flight(746)

fivefortyfive.airline = twa
six_forty_six.airline = twa
seven_forty_six.airline = delta


# twa.flights
# # [<fivefortyfive>, <six_forty_six>]
#
# delta.flights
# # [<seven_forty_six>]
