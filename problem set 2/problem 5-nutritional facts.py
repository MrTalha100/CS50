'''problem 5
"""nutritional facts"""'''

#method 1

a={"Apple":130,"Avacado":50,"Banana":110,"Cantaloupe":50,"Grapes":90,"Honeydew Melon":50,"Kiwifruit":90,"Lemon":15,"Lime":20,"Nectarine":60,"Orange":80,"Peach":60,"Pair":100,"Pineapple":50,"Plums":70,"Strawberries":50,"Sweet Cherries":100,"Tengerine":50,"Watermelons":80}
b=input("welcome enter a fruit to know its calories: ")
if b.lower():
    v=b.title()
    t=a.get(v)
    print(t)
else:
    t=a.get(b)
    print("CALORIES: ",t)

#method 2

# a={"Apple":130,"Avacado":50,"Banana":110,"Cantaloupe":50,"Grapes":90,"Honeydew melon":50,"Kiwifruit":90,"Lemon":15,"Lime":20,"Nectarine":60,"Orange":80,"Peach":60,"Pair":100,"Pineapple":50,"Plums":70,"Strawberries":50,"Sweet Cherries":100,"Tengerine":50,"Watermelons":80}
# t=a.get(input("welcome enter a fruit to know its calories: "))
# print(t)






