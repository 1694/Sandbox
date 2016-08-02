import os

print("The Files and Folders in {} are:".format(os.getcwd()))
items = os.listdir('.')
for item in items:
    print(item)

