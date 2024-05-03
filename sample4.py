"""write a program which accepts sequence of comma separated numbers from console and generate
     a list and tuple which contains every number"""

list1 = list(map(str, input("Enter elements inside list:").split(',')))

tuple1 = tuple(list1)

print(list1)
print(tuple1)
