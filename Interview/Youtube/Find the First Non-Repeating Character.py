text = "aabbcdde"

cha_f = {}
for char in text:
    cha_f[char] = cha_f.get(char, 0) + 1

# print(cha_f)
for c in text:
    if cha_f[c] == 1:
        print(c)
# print(d)