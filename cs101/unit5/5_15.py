def find_second(search_string, target_string):
    return search_string.find(target_string, search_string.find(target_string) + 1)

danton = "De l'audace, encore de l'audace, toujours de l'audace"
print(find_second(danton, 'audace'))