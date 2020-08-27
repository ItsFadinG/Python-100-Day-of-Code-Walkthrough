NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    titled = []
    [titled.append(name.title()) for name in names]
    return list(dict.fromkeys(titled))
# print(dedup_and_title_case_names())


def sort_by_surname_desc():
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(NAMES)
    # ...
    return sorted(names, key=lambda x: x.split(" ")[-1], reverse=True)
# print(sort_by_surname_desc())

def shortest_first_name():
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(NAMES)
    # ...
    lowest = []
    for name in names:
        lowest.append(name.split()[0])
    return min(lowest)
    # for i in names:
    #     i = i.split()
    #     lowest.append({'name':i[0], 'surname': i[1]})
    # short_name_sort = sorted(lowest, key=lambda k: len(k['name']))
    # return short_name_sort[0]['name']
print(shortest_first_name())
