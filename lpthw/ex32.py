the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f"this is count {number}")

for fruit in fruits:
    print(f"a fruit of type {fruit}")

for i in change:
    print(f"i got {i}")

elements = []

for i in range(0, 6):
    print(f"adding {i} to the list")
    elements.append(i)

for i in elements:
    print(f"elment was : {i}")