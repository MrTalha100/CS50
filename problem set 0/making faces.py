# 1st method for making faces
def main():
 a = input("how are feeling happy':)' OR sad':(' make an emoji = ")
 result = convert(a)
 print(result)
def convert(a):
 if a==":)":
  m1=a.replace(":)","happy🙂")
  return m1
 elif a==":(":
  m2=a.replace(":(","sad🙁")
 return m2 
 
main()

# # second method for making faces.
# def emoji():
#     if a==":)":
#         print("🙂")
#     elif a==":(":
#         print("🙁")
#     else:
#         print("wrong input. have no emoji for that ") 

# a=input("how r u feeling today express it by making a emoji: ") 
# emoji()       


 

