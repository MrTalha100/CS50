######1st method but it show values in key value pair ########

def main():
 glist=[]
 dictionary={}
 r=1
 print("WELCOME ! ENTER YOUR ITEMS WHEN DONE ENTER 'list plz'  and we will give you the list of your items🙂")

 while True:
  b=input("ENTER ITEMS:")
  if b not in dictionary:
    dictionary.update({b:1})
    glist.append(b)
    cont=glist.count(b)
      
  elif b in dictionary:
        s=dictionary.get(b)
        h=s+r
        dictionary.update({b:h})
        glist.append(b)
  if "list plz" not in dictionary:
      continue
  else:
      dictionary.popitem()
      for key in dictionary:
          print("THANKS FOR USING OUR SERVICE🙂🙂🙂\n HERE ARE YOUR ITEMS !")
          print(dictionary[key],key)
      break

try:
 main()
except ValueError:
   print("value error. enter again.")
   main()



######2nd method but it always hide some values ########
# def main():
#  print("ENTER YOUR ITEMS WHEN DONE ENTER 'list plz' and we will give you the list of your items🙂")
#  grocery_list=[]
#  t=3
#  while t>2:
#   grocery_list.append(input("ENTER ITEMS:"))
#   if "list plz" not in grocery_list:
#    continue
#   else:
#    grocery_list.remove("list plz")
#    print("THANKS FOR USING OUR SERVICE🙂🙂🙂\n HERE ARE YOUR ITEMS !")
#    for h in grocery_list:
#     a=grocery_list.count(h)
#     b=h
#     print(grocery_list.count(h),h)
#     if a>1:
#      while True:
#       if b in grocery_list:
#         grocery_list.remove(b)
#       elif b not in grocery_list:
#        break
#    break
# try:
#  main()
# except KeyError:
#  print("invalid entry . enter again.")