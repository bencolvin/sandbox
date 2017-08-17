name = str(input("Enter your name: "))
while not name:
    name = str(input("Enter a valid name: "))
print(name[::2])