'''1st meyhod of meal time '''
a=input("what time it is in 24 hour format: ")
hour , minute=a.split(":")
hours=int(hour)
minutes=int(minute)

if hours==7 and minutes<=59:
    print("its time for break fast!")
elif hours==8 and minutes==00:
    print("its time for break fast!")
elif hours==12 and minutes<=59:
    print("its time for lunch!")
elif hours==13 and minutes==00:
    print("its time for lunch!")
elif hours==18 and minutes<=59:
    print("its time for dinner!")
elif hours==19 and minutes==00:
    print("its time for dinner!")
else:
    print("no time for breakfast , lunch  or dinner")


'''alternative meal time code using user define function , while loop and if else conditionals'''

# def meal(hours,minutes):
#   if hours==7 and minutes<=59 or  hours==8 and minutes==00:
#     print("its time for break fast!")
#   elif hours==12 and minutes<=59 or hours==13 and minutes==00:
#     print("its time for lunch!")
#   elif hours==18 and minutes<=59 or hours==19 and minutes==00:
#     print("its time for dinner!")
#   else:
#     print("not a time for breakfast , lunch or either for diner ")
   

# while True:
#  a=input("what time it is in 24 hour format: ")
#  hour , minute=a.split(":")
#  hours=int(hour)
#  minutes=int(minute)

#  meal(hours,minutes)

#  user=input("do you want to continue or exit program. to exit enter  exit ,to continue enter continue: ")

#  if user=="continue":
#     continue
#  else:
#     print("thanks for using our time checking service🙂🙂🙂🙂") 
#     break
  
  