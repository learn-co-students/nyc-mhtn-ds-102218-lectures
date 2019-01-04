# data and functions, behavior
# now our functions have to accomodate different data types
# helps us define our data types
# scopes down the capability of a data type
    # tends to promote small code
        # 1. the functions become smaller (handle fewer things)
        # 2. scopes down the functions
    # encapsulation
        



def make_noise(animal):
    if animal['species'] == 'person':
        print('hi my name is ' + animal['name'])
    if animal['species'] == 'dog':
        print('hi my name is ' + animal['name'] + ' woof')
    if animal['species'] == 'chicken':
        print('hi my name is ' + animal['name'] + ' cluck cluck')
    if animal['species'] == 'whale':
        print('hi my name is ' + animal['name'] + 'roar')


billy = {'name': 'billy', 'age': 8, 'species': 'person'}


def construct_person(name, age, species):
    return {'name': name, 'age': age, 'species': species}

sally = {'name': 'sally', 'type': 'person'}

fido = {'name': 'fido', 'age': 3, 'species': 'dog'}

class Dog:
    def make_noise():
        print('hi my name is ' + animal['name'] + ' woof')

class Person:
    def make_noise():
        print('hi my name is ' + animal['name'])

    def walk():
        pass





chicken = {'name': 'foghorn', 'age': 2, 'species': 'chicken'}
whale = {'name': 'willy', 'age': 2, 'species': 'whale'}
turtle = {'name': 'splash', 'age': 2, 'species': 'turtle'}
