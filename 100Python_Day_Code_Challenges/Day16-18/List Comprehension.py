# list: a collection of data inside brackets.
# Comprehension lists: a one line exoression inside brackets.

import string

names = 'pybites mike bob julian tim sara guido'.split()
for i in names:
    print(i.title()) # captial the first letter

First_half_alphapet = list(string.ascii_lowercase)[:13]
print(First_half_alphapet)

new = []
for name in names: 
    if name[0] in First_half_alphapet:
        new.append(name.title())
print(new)

                        # one Line:
pythonist = [name.title() for name in names if name[0] in First_half_alphapet]
print(pythonist)