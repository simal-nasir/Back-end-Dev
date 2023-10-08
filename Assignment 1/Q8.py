# 8. Finally, add a break statement directly after the print statement inside the if condition for
# finding the number.
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
for index , n in enumerate(num_list):
    if (n == 36):
        print('Number found at position :',index)
        break