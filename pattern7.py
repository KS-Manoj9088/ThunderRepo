# to print square pattern with digits

n = int(input("Enter no of rows : "))
for i in range(n):
    for j in range(n):
        print(str(j+1),end=" ")
    print()