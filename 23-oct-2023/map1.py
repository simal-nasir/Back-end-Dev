num =[1,2,3,4,5]
def multiplication(n):
    return n*2
map_n = map(multiplication,num)
print(map_n)
for x in map_n:
    print(x)