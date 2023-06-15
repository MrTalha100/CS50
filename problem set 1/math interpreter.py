'''1st VERSION OF MATH INTERPRETER'''
a=input("tell us mastr what operation do u want to perform and between which two  values but give space btw operand and operartor: ").strip()
a1=a.split()
# print(a1)
b=float(a1[0])
c=a1[1]
d=float(a1[2])

if c=="+":
    print(f"{b}+{d}=",round(b+d,2))
elif c=="-":
    print(f"{b}-{d}=",round(b-d,2))
elif c=="*":
    print(f"{b}*{d}=",round(b*d,2))
elif c=="/":
    print(f"{b}/{d}=",round(b/d,2))
elif c=="%":
    print(f"{b}%{d}=",round(b%d,2))
elif c=="//":
    print(f"{b}//{d}=",round(b//d,2))
elif c=="**":
    print(f"{b}**{d}=",round(b**d,2))
else:
    print("not a arithematic number")


'''ALTERNATE VERSION OF MATH INTERPRETER but with  2 integer input and 1 arithematic operator input individually'''

# user=input("tell us mastr what arithematic operation do u want to perform and between which two  values but give space btw operand and operartor: ").strip()
# b , c ,d =user.split()
# b=float(b)
# d=float(d)

# if c=="+":
#     print(f"{b}+{d}=",b+d)
# elif c=="-":
#     print(f"{b}-{d}=",b-d)
# elif c=="*":
#     print(f"{b}*{d}=",b*d)
# elif c=="/":
#     print(f"{b}/{d}=",b/d)
# elif c=="%":
#     print(f"{b}%{d}=",b%d)
# elif c=="//":
#     print(f"{b}//{d}=",b//d)
# elif c=="**":
#     print(f"{b}**{d}=",b-d)
# else:
#     print("invalid vlaues")


'''ALTERNATE VERSION OF MATH INTERPRETER but with  2 integer input and 1 arithematic operator input individually'''

# b=int(input("enter 1st operand: "))
# c=input("enter operator: ")
# d=int(input("enter 2nd operand: "))

# if c=="+":
#     print(f"{b}+{d}=",b+d)
# elif c=="-":
#     print(f"{b}-{d}=",b-d)
# elif c=="*":
#     print(f"{b}*{d}=",b*d)
# elif c=="/":
#     print(f"{b}/{d}=",b/d)
# elif c=="%":
#     print(f"{b}%{d}=",b%d)
# elif c=="//":
#     print(f"{b}//{d}=",b//d)
# elif c=="**":
#     print(f"{b}**{d}=",b-d)
# else:
#     print("invalid values")


