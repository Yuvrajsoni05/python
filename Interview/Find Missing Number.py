numbers = [1, 2, 3, 5, 6]
n = len(numbers) + 1
print(n)
ex = n * (n + 1) // 2
print(ex)
actual_sum = sum(numbers)
print(actual_sum)
missing = ex- actual_sum
print(missing)