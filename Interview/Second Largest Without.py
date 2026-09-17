numbers = [10, 25, 5, 40, 30]

# FIX: Initialize large to negative infinity
large = float("-inf")
seco = float("-inf")

for number in numbers:
    if number > large:
        seco = large       # Old largest becomes second largest
        large = number     # Update largest
    elif number > seco and number != large:
        seco = number      # Update second largest if it's smaller than large

print(seco)

# numbers = [10, 25, 5, 40, 30]
# large = float("inf")
# seco = float("-inf")
# for num in numbers:
#     if num > large:
#         seco = large
#         large = num
#     elif num > seco and num != large:
#         seco = num
# print(seco)