def sum_of_number(n):
    if n == 0:
        return 0
    else:
        return  sum_of_number(n-1) + n
        
print(sum_of_number(5))
