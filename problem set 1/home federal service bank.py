a=((input("greetings: ").lower()).strip(""))
a3=a
print(a3)
a1=a3.replace("",".")
print(a1)
a2=a1.split(".")
print(a2)
if a=="hello":
    print("$0")
elif a2[0]=="h" or a2[1]=="h":
    print("$20")
else:
    print("$100")

'''greetings alternate version'''

# a=input("greetings:")
# if a[0:5]=="hello":
#     print("$0")
# if a[0]=="h":
#     print("$20")
# else:
#     print("you didn't say hello , now give me $100 dollars")


