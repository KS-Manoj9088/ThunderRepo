#  To  print square pattern with alphabet symbols

n  = int(input("Enter no of rows : "))
for i in range(n):
    print((chr(65+i)+" ")*n)