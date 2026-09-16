numbers = [10, 15, 22, 33, 40, 51, 60]
even = []
odd = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)