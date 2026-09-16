numbers = [10, 45, 23, 67, 12, 89, 34]
lar = numbers[0]


for number in numbers:
    if number > lar:
        lar = number
print(lar)