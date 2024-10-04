# exception is an unexpected event during the program execution.
#  car--> delhi to mumbai (xyz highway)--

# try:
#    num=int(input("enter numenator:"))
#    den=int(input("enter denomiter:"))
#    print("exception handling program")
#    # print(num/den) 
#    # print("exit")
# except:
#    print("your program has exception error")
# print(dir(locals()["__builtins__"]))
# a=[4,9,6,7,2]
# print(a[20])   
#    
try:
   # num=int(input("enter numenator:"))
   # den=int(input("enter denomiter:"))
   print("exception handling program")
   # print(num/den) 
   a=[4,9,6]
   print(a[1])
   print("exit")
except ZeroDivisionError:
   print("your need to add number above zero")
except IndexError:
   print("bhai put the right index")
    