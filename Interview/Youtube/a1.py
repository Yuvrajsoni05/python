


def common_letters():
    str1 = "Naina"
    str2 = "Reena"
    str1.lower()
    str2.lower()
    s1 = set(str1)
    s2 = set(str2)
    lst = s1 & s2
    print(lst)
    # print(s1)
    # print(s2)
def freq_words():
    str = input("Enter a string: ")
    li = str.split()
    de = {}
    for i in li:
        if i not in de.keys():
            print(i)

            de[i] = 0
            de[i] = de[i] + 1

    print(li)
    print(de)


freq_words()
# common_letters()

