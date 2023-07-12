from random import randint

while True:
  try: 
   a=int(input("LEVEL:"))
   if a<1:
    print("enter level again, level should be >=1:")
    continue
   else:
    b=randint(1,a)
    break
  except ValueError:
    continue

while True:
  
 try:   
  c=int(input("GUESS:"))
  if c==b:
    print("Just right")
    break
  elif c==0:
    print("enter again:")
    continue
  elif c<1:
    print("negative number .enter again:")
    continue
  elif c<b:
    print("too small")
    continue
  elif c>b:
    print("too lagre")
    continue
 except ValueError:
    continue
  
