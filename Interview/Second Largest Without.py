numbers = [10, 25, 5, 40, 30]

large = float("inf")
seco = float("-inf")

for number in numbers:
    if number > large:
        seco = large
        large = number
    elif number > seco and number != large:
        seco = number
print(seco)