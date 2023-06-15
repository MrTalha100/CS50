'''problem 2
"""coke machine"""'''

rs=50
while rs>0:
  
  a=int(input("insert coins 25 or 10 0r 5: "))
  if a in [25,10,5]:
   rs=rs-a
   if rs>0:
    print("amount due: ",rs)
   elif rs<=0:
    change_owed=abs(rs)

    print("change_owed: ",change_owed)