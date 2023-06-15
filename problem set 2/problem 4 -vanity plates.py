'''problem 4
"""vanity plates"""'''

def main():
    plate = input("input what you want to display on your plate Plate: ").lower()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(p):
     if 6>= len(p) >=2 and p[0:2].isalpha() and p.isalnum():
        for char in p:
          if char.isdigit():
            index=p.index(char)
            if p[index:].isdigit() and int(char) !=0:
                return True
            else:
                return False
        return True        
main()



####2nd method but one condition doesn't work (The first number used cannot be a ‘0’.)#####

# def main(plate,v):
#   num=[1,2,3,4,5,6,7,8,9]
#   print(plate)
#   print(v)
#   if v<2:
#      return "invalid"
#   elif v>6:
#      return "invalid"
#   elif (plate.isalpha()):
#      return "valid"
#   elif (v==3):
#     if(plate[0:1].isalpha()) and( plate[2]!="0"):
#       return "valid"
#     else:
#       return "invalid"
#   elif (v==4):
#     if((plate[0:1].isalpha()) and( plate[2]!="0" and plate[3].isdecimal())):
#       return "valid"
#     elif(plate[0:2].isalpha()) and( plate[3]!="0" ):
#       return "valid"
#     else:
#       return "invalid"
#   elif (v==5):
#     if((plate[0:1].isalpha()) and( plate[2]!="0" and plate[3:4].isdecimal())):
#       return "valid"
#     elif((plate[0:2].isalpha()) and( plate[3]!="0" and plate[4].isdecimal())):
#       return "valid"
#     elif (v==5)and((plate[0:3].isalpha()) and( plate[4]!="0")):
#       return "valid"
#     else:
#       return "invalid"
#   elif (v==6):
#      if((plate[0:1].isalpha()) and( plate[2]!="0" and plate[3:5].isdecimal())):
#        return "valid"
#      elif (v==6)and((plate[0:2].isalpha()) and( plate[3]!="0" and plate[4:5].isdecimal())):
#        return "valid"
#      elif (v==6)and((plate[0:3].isalpha()) and( plate[4]!="0" and plate[5].isdecimal())):
#        return "valid"  
#      elif (v==6)and((plate[0:4].isalpha()) and( plate[5]!="0")):
#       return "valid"
#   else:  
#    return "invalid"



# plate = input("input what you want to display on your vanity Plate:") 
# v=len(plate)
# if main(plate,v)=="valid":
#   print("valid")
# else:   
#   print("invalid")

####################### rules of vanity plates #####################################
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#   “All vanity plates must start with at least two letters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”