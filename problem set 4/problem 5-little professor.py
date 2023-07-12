import random

f=0
print("score=",f)
user=input("SELECT LEVEL 1/2/3 . enter level number:")
for r in range(10):
    
     if user=="1":
      while True:
       a=[0,1,2,3,4,5,6,7,8,9]
       b=["+","-","*","/"]
       c=[0,1,2,3,4,5,6,7,8,9]
       a1=random.choice(a)
       b1=random.choice(b)
       c1=random.choice(c)
       if a1<c1:
        continue
       else:
        break
     elif user=="2":
      while True:
       b=["+","-","*","/"]
       a1=random.randint(10,99)
       b1=random.choice(b)
       c1=random.randint(10,99)
       if a1<c1:
        continue
       else:
        break
     elif user=="3":
      while True:
       b=["+","-","*","/"]
       a1=random.randint(100,999)
       b1=random.choice(b)
       c1=random.randint(100,999)
       if a1<c1:
        continue
       else:
        break
     

     if b1=="-":
      d=a1-c1
      for i in range(3):
         try:
           e1=int(input(f"what is result of {a1}-{c1}="))
           if e1==d:
            print("right answer")
            f=f+1
            break
           else:
            print("EEE")
            continue
         except ZeroDivisionError:
           continue
         except ValueError:
           continue
      if e1!=d:
         print(f"result of {a1}-{c1}=",a1-c1)
     
     elif b1=="+":
       d=a1+c1
       for i in range(3):
         try:
           e1=int(input(f"what is result of {a1}+{c1}="))
           if e1==d:
            print("right answer")
            f=f+1
            break
           else:
            print("EEE")
            continue
         except ZeroDivisionError:
           continue
         except ValueError:
           continue
       if e1!=d:
         print(f"result of {a1}+{c1}=",a1+c1)
         
     
     elif b1=="*":
       d=a1*c1
       for i in range(3):
         try:
           e1=int(input(f"what is result of {a1}*{c1}="))
           if e1==d:
            print("right answer")
            f=f+1
            break
           else:
            print("EEE")
            continue
         except ZeroDivisionError:
           continue
         except ValueError:
           continue
       if e1!=d:
         print(f"result of {a1}*{c1}=",a1*c1)
     elif b1=="/":
     
        d=a1/c1
        for i in range(3):
         try:
           e1=int(input(f"what is result of {a1}/{c1}="))
           if e1==d:
            print("right answer")
            f=f+1
            break
           else:
            print("EEE")
            continue
         except ZeroDivisionError:
           continue
         except ValueError:
           continue
        if e1!=d:
         print(f"result of {a1}/{c1}=",a1/c1)
          
print("score=",f)


