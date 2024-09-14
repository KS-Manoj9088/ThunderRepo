# To print square pattern with digits in descending order

n = int(input("Enter no of rows : "))
for i in range(n):
    for j in range(n):
        print(str(n-j),end=" ")
    print()