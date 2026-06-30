def print_list(lst,idx):
    if idx == len(lst):
        return

    print(lst[idx])

    print_list(list,idx+1)
list=[1,2,3,4,5,6,7,8,9]
print_list(list,0)


