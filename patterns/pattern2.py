#We are goin to draw a Square pattern something like a box.
#Dynamically taking input from user , we will generate n x n square box.

n = int(input("Enter the no of rows and columns : "))
for i in range(n):
    print("* "*n)