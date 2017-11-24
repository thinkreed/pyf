def hexes_to_udaciousness(n, spread, target):
    if n >= target:
        return 0
    return 1 + hexes_to_udaciousness(n * (spread + 1), spread, target)


print(hexes_to_udaciousness(100000, 2, 36230))
print(hexes_to_udaciousness(50000, 2, 150000))
print(hexes_to_udaciousness(50000, 2, 150001))
print(hexes_to_udaciousness(20000, 2, 7 * 10 ** 9))
print(hexes_to_udaciousness(15000, 3, 7 * 10 ** 9))
