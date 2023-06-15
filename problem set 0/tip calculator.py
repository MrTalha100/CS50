# 1st methd

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d_without_dollar_sign =d.replace("$","")
    return float(d_without_dollar_sign)

def percent_to_float(p):
    p_without_percent = float(p.replace("%",""))
    p_converted = p_without_percent / 100
    return p_converted
main()



# # 2nd method

# def main():
#     dollars = dollars_to_float(input("How much was the meal? "))
#     percent = percent_to_float(input("What percentage would you like to tip? "))
#     tip = dollars * percent
#     print(f"Leave ${tip:.2f}")


# def dollars_to_float(d):
#     c=float(d.strip("$"))
#     # print(c)
#     return c

# def percent_to_float(p):

#     h=p.strip("%")
#     new_h=(float(h))/100
#     # print(new_h)
#     return new_h

# main()



# # 3rd method

# def main():
#     d = float((input("How much was the meal? ")).strip("$"))
#     p = (float((input("What percentage would you like to tip? ")).strip("%")))/100
#     dollars=d
#     percent=p

#     tip = dollars * percent
#     print(f"Leave ${tip:.3f}")

# main()