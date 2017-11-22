rules_table = {
    'xxx': 128,
    'xx.': 64,
    'x.x': 32,
    'x..': 16,
    '.xx': 8,
    '.x.': 4,
    '..x': 2,
    '...': 1
}


def generate_pattern_map(pattern):
    pattern_map = {}
    i = 128
    while i >= 1:
        if pattern >= i:
            pattern_map[int(i)] = 'x'
            pattern = pattern - i
        else:
            pattern_map[int(i)] = '.'
        i = i / 2
    return pattern_map


def cellular_automaton(string, pattern, generation):
    if generation == 0:
        return string
    pattern_map = generate_pattern_map(pattern)
    next_string = ''
    n = len(string)
    for i in range(0, n):
        pattern_string = string[i - 1] + string[i] + string[(i + 1) % n]
        next_string = next_string + pattern_map[rules_table[pattern_string]]
    return cellular_automaton(next_string, pattern, generation - 1)


print(generate_pattern_map(218))
print(cellular_automaton('.x.x.x.x.', 17, 2))
print(cellular_automaton('.x.x.x.x.', 249, 3))
print(cellular_automaton('...x....', 125, 1))
print(cellular_automaton('...x....', 125, 2))
print(cellular_automaton('...x....', 125, 3))
print(cellular_automaton('...x....', 125, 4))
print(cellular_automaton('...x....', 125, 5))
print(cellular_automaton('...x....', 125, 6))
print(cellular_automaton('...x....', 125, 7))
print(cellular_automaton('...x....', 125, 8))
print(cellular_automaton('...x....', 125, 9))
print(cellular_automaton('...x....', 125, 10))
print(cellular_automaton('.x.', 248, 2))
print(cellular_automaton('.x.x.x.x.', 218, 3))
