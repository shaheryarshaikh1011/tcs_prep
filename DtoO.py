decimal = int(input("Enter a decimal number :"))

def DtoO(decimal):
    octal = 0
    i = 1
    while (decimal != 0):
        octal = octal + (decimal % 8) * i
        decimal = int(decimal / 8)
        i = i * 10
    return 
    
print("The octal equivalent is :",DtoO(decimal))