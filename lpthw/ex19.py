def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"you have {cheese_count} cheese")
    print(f"you have {boxes_of_crackers} boxes of crackers")
    print("Man that's enought for a party")
    print("get an blanket")


print("we can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("or we can use variables from out script")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("we can do math inside too")
cheese_and_crackers(10 + 20, 5 + 6)
print("we can combine the two, variable and math")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
