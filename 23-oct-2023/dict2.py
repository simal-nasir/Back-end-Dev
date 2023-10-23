file = {"jpg" : 10 ,"txt" : 14,"csv" : 2 ,"py" : 23}
print(file["py"])
for extension in file:
    print(extension)
for ext, amount in file.items():
    print("There are {} files with the .{} extension".format(amount,ext))
