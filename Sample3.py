"""With a given integral number n, write a program to generate dictionary that contains
    (i, i*i) such that is an integral number between 1 and n(both included). and then the program
    should print the dictionary"""

while True:
    try:
        user_input = int(input("Please, enter a number:"))
        break
    except:
        print("Please enter valid number.")

dict1 = {}

for i in range(1, user_input + 1):
    dict2 = {i: i*i}
    dict1.update(dict2)

print(dict1)
