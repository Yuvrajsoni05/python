list1 = [1, 2, 3, 4,7]
list2 = [3, 4, 5, 6]

common = list(set(list1) & set(list2))

n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()