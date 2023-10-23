items=[1,2,3,4,5]
items=items[6]
try:
  print(items)
except Exception as e:
  print("Something went wrong",e)