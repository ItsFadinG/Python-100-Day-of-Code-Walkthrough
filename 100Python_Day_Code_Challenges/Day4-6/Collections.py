from collections import Counter, defaultdict, namedtuple, OrderedDict, deque

                    # Counter

# Counter(): return a count of the values as a dictionary
Repeated = Counter('abcacdabcacd')
print(Repeated)

# element(): Returns a list of each element and If an element’s count is less than one, it is ignored
c = Counter(a=3, b=2, c=1, d=-2)
print(sorted(c.elements()))

# most_common(n): print the most comman items
common = "the lazy dog jumped over another lazy dog dog"
words = common.split()
print(Counter(words).most_common(3))

# Tuples are unchangeable, or immutable lists
tuple = ('apple', 'banna', 'cherry')
print(tuple)

# namedtuple(): give an ability to Tuples to pass an identifier rather than an integer indexes
fruit = namedtuple('fruit', 'color, type')
guava = fruit(color='green', type='sugary')
print(guava)

# Dictionary: is a collection which is unordered(but now it is), changeable and indexed
# useless now >> OrderedDict(): dictionary subclass that remembers the order in which that keys were first inserted
ordered_dict = OrderedDict()
ordered_dict['ME'] = 'Muhammad'
ordered_dict['He'] = 'friend'
print(ordered_dict['He'])

# defaultdict(): Returns 0 if the intended value isn't exist
default_dict = defaultdict(list)
default_dict['ME'] = 'Muhammad'
default_dict['He'] = 'Friend'

print(default_dict['She'])

# deque(): it is like lists but it provide a fast way to append and pop from list
list = ['adle', 'Hello', "It's", "Me"]
deque = deque(list)
print(deque)
deque.append('again')
print(deque)
deque.appendleft('again')
print(deque)
deque.pop()
print(deque)
deque.popleft()
print(deque)
