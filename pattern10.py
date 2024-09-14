# To print square pattern with alphabets in reverse dictionary order.

n = int(input("Enter no of rows : "))
for i in range(n):
    print((chr(65+n-i-1)+" ")*n)