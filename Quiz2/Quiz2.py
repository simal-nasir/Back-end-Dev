def skip_elements(elements):
    obj1 = list(enumerate(elements,1))
    for x ,elements in obj1:
        if x % 2 != 0:
            print(elements)
    return obj1
print(skip_elements(["a","b","c","d","e","f","g"]))
print(skip_elements(['Orange','Pineapple','Strawberry','Kiwi','Peach']))