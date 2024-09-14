#To print square pattern with digits in descending order

n = int(input("enter no of rows : "))
for i in range(n):
    print((str(n-i)+" ")*n)