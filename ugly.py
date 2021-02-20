#divison function to check no has remainder or get fully divided
def divideBy(a, b):
    while a % b == 0:
        a = a / b
    return a
 
# Function to check if a number gets divided by 2,3,5 or not
def checkNo(no):
    no = divideBy(no, 2)
    no = divideBy(no, 3)
    no = divideBy(no, 5)
    return 1 if no == 1 else 0
 
# Function to get the nth number
def getNthElement(n):
    i = 1
     
    # number count
    count = 1 
 
    # Check for all integers untill
    # count becomes n
    while n > count:
        i += 1
        if checkNo(i):
            count += 1
    return i
 
 
# Driver code
no=int(input("enter number: "))
ans=getNthElement(no)
print("nth element no. is ", ans)
