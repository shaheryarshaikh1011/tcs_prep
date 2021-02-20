#take inputs
x=int(input("Enter starting range"))
y=int(input("Enter ending range"))
if(x<y and x>0):
    for i in range(x,y+1):
        sum=0
        temp=i
        while temp>0:
            dig=temp%10
            sum+=dig**3
            temp//=10
        if i==sum:
            print(sum)
else:
    print("wrong input")
