print("here is the menu:")
menu={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

for key,value in menu.items(): 
 print(key,value)
 total=0

while True:
    try:
      a=menu[input("WHAT YOU WANT TO ORDER: ").title()]
      total=a+total
      print(f"${total:.2f}")

    except EOFError:
       pass
    except KeyError:
       print(f"HERE IS YOUR BILL: ${total:.2f}")
       break