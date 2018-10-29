greeting = 'hello'
# global variable

class IceCreamShop():
    # something_here = 'something'
    # print(greeting)
    # kindness = 'you are nice'
    available_discounted_flavors = ['vanilla', 'chocolate', 'strawberry']
    # class attributes - we can access on the class
    #


    def __init__(self, goodbye):
        location = None

        self.goodbye = goodbye

    def say_something(self):
        print(greeting)

    def say_goodbye(self):
        print(self.goodbye)

    def start_goodbye(self, goodbye):
        # local
        may_be_nice = 'have a good day'
        self.goodbye = goodbye

    def set_discounted_flavor(self, flavor):
        if flavor not in self.flavors raise('not in flavors')
        
