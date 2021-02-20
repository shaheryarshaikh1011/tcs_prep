lower = int(input("Enter Lower bound of the range"))
upper = int(input("enter Upperbound of the range"))

print("Prime numbers between", lower, "and", upper, "are:")
#initialize variable to store sum of prime numbers
sum=0;
for num in range(lower + 1, upper ):
# all prime numbers are greater than 1
    if num == 1:
        break;
    else:
        for i in range(2, num):
           if (num % i) == 0:
               break
        else:
           print(num)
           sum=sum+num;           
print("Sum of prime numbers between ",lower," and ",upper," is ",sum)