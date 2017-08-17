name = input("Enter your name: ")
while not name:
    name = input("Enter a valid name!: ")
print(name[::2])
