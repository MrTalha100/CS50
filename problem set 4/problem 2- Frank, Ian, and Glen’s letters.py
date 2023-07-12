
from pyfiglet import Figlet
from random import choice
user=input("ENTER A OPTION NUMBER: \n 1:DO YOU WANT SYSTEM GIVEN RANDOM FONT FOR  OUTPUT TEXT.\n 2:OR YOU WANT TO GIVE YOUR OWN FONT FOR  OUTPUT TEXT.\n ")
if user=="1":
 f = Figlet()
 b = f.getFonts()
 c=choice(b)
 print("system choosen font:",c)
 f = Figlet(font=c)
 a = input("ENTER TEXT:")
 print(f.renderText(a))
elif user=="2":
 f = Figlet()
 b = f.getFonts()
 print("LIST OF DIFFERENT AVAILABLE FONTS:\n\t",b,"\n\t")
 
 c=input("\nCHOOSE YOUR FONT NAME FROM ABOVE LIST:")
 if c in b:
   f = Figlet(font=c)
   a = input("ENTER TEXT:")
   print(f.renderText(a))
 else:
  print("FONT not FOUND!!!")
else:
 print("invalid value")