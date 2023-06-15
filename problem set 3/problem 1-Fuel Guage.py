# ''problem 1
# ***""""FUEL GUAGE""""***'''
while True:
 try:
   a=input("Fraction :")
   a1,a2=a.split("/")
   b=int(a1)/int(a2)
   if a=="1/2":
    print("50%")
   elif a=="4/4" or round(b)==99:
    print("F")
   elif a=="0/1" or round(b)==1 or round(b)==0:
    print("E")
   else:
    b1,b2=str(b).split(".")
    print(f"{b2}%")

   break
 except ZeroDivisionError: 
   print("ZeroDivisionError")
 except ValueError:
   print("ValueError")
 except NameError:
   print("NameError. enter value again")
 if a1>a2 or a2==0:
   continue