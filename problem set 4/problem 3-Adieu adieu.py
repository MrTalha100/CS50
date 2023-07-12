import inflect
p=inflect.engine()
d=[]
while True:
    a=input("ENTER NAME:")
    d.append(a)
    if a=="control-d":
       d.remove("control-d")
       break
u=p.join(d)
print("Adieu, adieu, to",u)
