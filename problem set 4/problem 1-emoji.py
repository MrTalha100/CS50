# import random
# import sys
# while True:
#  print("........................................")

#  for a in range(3):
#   c=random.randint(1,100)
#   print(c)
 
#   if c==50:
#     print("you are mister talha qasim")
#     sys.exit()
#   else:
    
#     continue
import emoji
h=input("(NOTE: If emoji name consists of two or more words then input '_' between them)\n ENTER CLDR EMOJI SHORT NAME:")
h1=h.replace("",".")
h2=h1.split(".")
if ":" in h2:
    h3=h.strip(":")
    a=(f"\t\t:{h3}:")
    y=emoji.emojize(a,language='alias')
    if y==(f"\t\t:{h3}:"):
       print("not a emoji or either not a proper name")
    else:
        print(emoji.emojize(a,language='alias'))
    
elif ":" not in h2:
    a=(f"\t\t:{h}:")
    
    y=emoji.emojize(a,language='alias')
    if y==(f"\t\t:{h}:"):
       print("not a emoji or either not a proper name")
    else:
        print(emoji.emojize(a,language='alias'))

 
