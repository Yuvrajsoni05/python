text = "Python Developer"

a = "aeiou"
count = 0
for c in text.lower():
    if c in a:
        count += 1
        print(c)
print(count)