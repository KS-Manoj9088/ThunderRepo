# Square pattern with alphabet symbols in dictionary order

n = int(input("Enter the no of rows : "))
for i in range(n):
    for j in range(n):
        print(chr(65 + j), end=" ")
    print()  # print() is used to print in a new line
    