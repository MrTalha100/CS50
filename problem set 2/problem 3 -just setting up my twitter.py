'''problem 3
"""just setting up my twttr"""'''
a=input("enter what you want to say (string): ")
b=a.replace("","...")
print(b)
r=b.split("...")
print(r)

while True:
 if  "a" in r:
   r.remove("a")
 if  "a" not in r:
   break
while True:
 if  "e" in r:
   r.remove("e")
 if  "e" not in r:
   break
while True:
 if  "i" in r:
   r.remove("i")
 if  "i" not in r:
   break
while True:
 if  "o" in r:
   r.remove("o")
 if  "o" not in r:
   break
while True:
 if  "u" in r:
   r.remove("u")
 if  "u" not in r:
   break

print(r)
a1="".join(r)
print("a1= \n",a1)
