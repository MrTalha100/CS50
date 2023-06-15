'''1st method'''

a=input("enter a file name with its extension \n\n") 
b=a.split(".") 
print(b)
print(f"your file has extension .{b[1]}")


'''2nd method'''

# a=input("enter a file name with its extension \n\n") 
# file_name , extension=a.split(".") 
# print(f"your file has extension .{extension}")