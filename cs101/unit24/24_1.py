ada_family = {'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'],
              'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'],
              'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'],
              'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'],
              'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'],
              'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'],
              'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'],
              'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion']}


def ancestors(genealogy, person):
    if person in genealogy:
        parents = genealogy[person]
        result = parents
        for parent in parents:
            result = result + ancestors(genealogy, parent)
        return result
    return []


print(ancestors(ada_family, 'Dave'))
print(ancestors(ada_family, 'Augusta Ada King'))
