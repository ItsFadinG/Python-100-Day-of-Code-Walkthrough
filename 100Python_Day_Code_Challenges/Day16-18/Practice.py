# Convert names to title case


NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

def title():
    titled = [name.title() for name in NAMES]
    return titled
print(title())

# Reverse the first and last name
def reverse(name):
    first, last = name.split()
    return f'{last} {first}'
RE = [reverse(name) for name in NAMES]
print(RE)

# Get the first name only 
# Title Case them
# get these names randmly with other names
import random
def gen():
    first_names = [name.split()[0].title() for name in NAMES]
    # one, second = random.sample(first_names, 2)
    # return f'{one} teams up with {second}'
    
    while True:
        one, second = random.sample(first_names, 2)
        yield f'{one} teams up with {second}'

pairs = gen() 
for i in range(10):
    print(next(pairs))
