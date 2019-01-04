1. Describe what is happening in the `environment.py`
  what is each line doing?
  Why do we need to do this?

2. What is happening in seed.py file
  - Note that we can run the `seed` file in interactive mode with the line `python -i seed.py`
  What do we have access to if we do that?  Why?

3. Note that we have an airline class and a flight class.  Describe the relationship between airlines and flights.


4. Build out the following
- Build the following getter and setter methods
  For airline: name, year
    (ie. the year of incorporation)
  For flight: name

  (To do the following, look up class methods and class attributes in Python)
  - Airline.all()
    -> should return all of the Airlines that have been initialized
  - Flight.all()
    -> should return all of the flights that have been initialized

Bonus!!
  - Build the following instance method
    - airline.add_flight(flight)
      You should pass through a *flight instance* to the add_flight method
      After passing through a flight to the add_flight() method, you should be able to call airline.flights -> [flight]
      (ie it should return a list with the flight you added, in the list)
    - Bonus
      - delta = Airline()
      - flight = Flight()
      - After calling  delta.add_flight(flight)
      then, without doing anything else, if I call...
     flight.airline() -> delta
     (it should return delta)
