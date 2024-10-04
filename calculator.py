# num1=int(input("enter a num1: "))
# num2=int(input("enter a num2: "))
# print("add of",num1,"+",num2,"=",num1+num2)
# print("sub of",num1,"-",num2,"=",num1-num2)
# print("mul of",num1,"*",num2,"=",num1*num2)
# print("div of",num1,"/",num2,"=",num1/num2)
# print("power of",num1,"**",num2,"=",num1**num2)

#calculator
# a=input("enter expression: ")
# print(eval(a))

# print(eval(input("enter expression: ")))

# num1=int(input("enter a num1:"))
# num2=int(input("enter a num2:"))
# print("add of",num1,"+",num2,"=",num1+num2)
# print("sub of",num2,"-",num1,"=",num2-num1)
# print("mul of",num1,"*",num2,"=",num1*num2)
# print("div of",num1,"/",num2,"=",num1/num2)
# print("power of",num1,"**",num2,"=",num1**num2)
# # calculator
# expression=input("enter a mathemetical expression: ")
# print(eval(expression))

# advanced calculator
import math
def advanced_calculator():
    print("select operation: ")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. division ")
    print("5. power ")
    print("6.square root ")
choice=input("enter choice(1/2/3/4/5/6):")
if choice in ['1','2','3','4','5',"6"]:
    num1=float(input("enter anum1:"))
    num2=float(input("enter a num2:"))
    if choice=='1':
        print(f"{num1}+{num2}={num1+num2}")
    elif choice=='2' :
        print(f"{num2}-{num1}={num2-num1}")
    elif choice=='3':
     print(f"{num1}*{num2}={num1*num2}")
    elif choice=='4':
      print(f"{num1}/{num2}={num1/num2}")   
    
    elif choice=="5":
      print(f"{num1}^{num2}={num1**num2}")
    elif choice=="6":

         print(f"square root of {num1}={math.sqrt(num1)}")




















