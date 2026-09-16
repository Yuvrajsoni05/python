text = "Python Devloper"
fre = {}

for char in text:
    print(char)
    if char != "":
        fre[char] =  fre.get(char, 0) + 1
print(fre)