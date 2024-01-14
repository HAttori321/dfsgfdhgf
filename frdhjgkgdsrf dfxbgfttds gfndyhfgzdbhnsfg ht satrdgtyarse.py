def sum(x,y):
    return x+y 
def riznica(x,y):
    return x-y
def mnozhenja(x,y):
    return x*y
def dilenja(x,y):
    if y!=0:
        return x/y
    else:
        return "Ne dilutsa"

print("Choose operation:")
print("1.Suma")
print("2.Riznica")
print("3.Mnozhenja")
print("4.Dilenja")
choice=input("Enter menu number:")
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
if choice=='1':
    print(num1,"+",num2,"=",sum(num1,num2))
elif choice=='2':
    print(num1,"-",num2,"=",riznica(num1,num2))
elif choice=='3':
    print(num1,"*",num2,"=",mnozhenja(num1,num2))
elif choice=='4':
    print(num1,"/",num2,"=",dilenja(num1,num2))
