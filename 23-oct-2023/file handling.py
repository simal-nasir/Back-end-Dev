file = open('test.txt',mode='rb')
data = file.readlines()
print(data,type(data))
file.close()