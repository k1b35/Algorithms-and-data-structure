masti = ['tref', 'chervi', 'byben', 'pik']
names = ['valet', 'queen', 'king', 'tyz']
mast = input()
masti.remove(mast)
print(masti)
for i in range(2, 11):
    for elem in masti:
        print(i, elem)
for j in range(4):
    for el in names:
        for elem in masti:
                print(el, elem)