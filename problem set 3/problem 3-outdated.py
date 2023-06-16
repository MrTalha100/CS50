
def main():
   month=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
   ]
   a=input("enter  month,day,year  like  june 9, 2001 OR 12/7/2011 in  MM/DD/YYYY formate   :")
   i=a.replace("",".")
   u=i.split(".")
   if   "/"   in   u:
        x,p,j=a.split("/")
        if (int(x)<=0   or   int(p)>=13) and (int(p)<=0   or   int(p)>=32):
            print("wrong   month   and   day   value   .   plz   re_enter   value:   \n")
            main()
        else:
            slash(a)
   elif   ","   in   u:
        o="".join(u)
        x,p,j=o.split()
        if x in month and (int(p)<=0   or   int(p)>=32):
            print("wrong   month   and   day   value   .   plz   re_enter   value:   \n")
            main()
        else:
            comma(a)

   



def  slash(a):
      b1,b2,b4=a.split("/")
      if  len(a)==8:   
               print(f"YYYY-MM-DD : {b4}-0{b1}-0{b2}")
      elif len(a)==9:
          if  len(b1)==2:
              print(f"YYYY-MM-DD : {b4}-{b1}-0{b2}")
          elif len(b2)==2:
              print(f"YYYY-MM-DD : {b4}-0{b1}-{b2}")
      else:
              b1,b2,b4=a.split("/")
              print(f"YYYY-MM-DD : {b4}-{b1}-{b2}")

def comma(a):
       i=a.replace("",".")
       u=i.split(".")
       u.remove(",")
       #   print(u)
       g="".join(u)
       #   print(g)
       m,d,y=g.split()
       m=m.capitalize()
       print(m,d,y)
       #   print(m)
       d=int(d)   
       if   m=="January":   
            if   d<10:
               print(f"YYYY-MM-DD :{y}-01-0{d}")
            else:
               print(f"YYYY-MM-DD :{y}-01-{d}")
       elif   m=="February":
            if   d<10:
               print(f"YYYY-MM-DD :{y}-02-0{d}")
            else:
               print(f"YYYY-MM-DD :{y}-02-{d}")
       elif   m=="March":
            if   d<10:
               print(f"YYYY-MM-DD :{y}-03-0{d}")
            else:
               print(f"YYYY-MM-DD :{y}-03-{d}")
       elif   m=="April":
            if   d<10:
               print(f"YYYY-MM-DD :{y}-04-0{d}")
            else:
               print(f"YYYY-MM-DD :{y}-04-{d}")
       elif   m=="May":
            if   d<10:
               print(f"YYYY-MM-DD :{y}-05-0{d}")
            else:
               print(f"YYYY-MM-DD :{y}-05-{d}")
       elif   m=="June":
            if   d<10:
               print(f"YYYY-MM-DD :{y}-06-0{d}")
            else:
               print(f"YYYY-MM-DD :{y}-06-{d}")
       elif   m=="July":
            if   d<10:
               print(f"YYYY-MM-DD :{y}-07-0{d}")
            else:
               print(f"YYYY-MM-DD :{y}-07-{d}")
       elif   m=="August":
            if   d<10:
               print(f"YYYY-MM-DD :{y}-08-0{d}")
            else:
               print(f"YYYY-MM-DD :{y}-08-{d}")
       elif   m=="September":
            if   d<10:
               print(f"YYYY-MM-DD :{y}-09-0{d}")
            else:
               print(f"YYYY-MM-DD :{y}-09-{d}")
       elif   m=="Octobor":
            if   d<10:
               print(f"YYYY-MM-DD :{y}-10-0{d}")
            else:
               print(f"YYYY-MM-DD :{y}-10-{d}")
       elif   m=="November":
            if   d<10:
               print(f"YYYY-MM-DD :{y}-11-0{d}")
            else:
               print(f"YYYY-MM-DD :{y}-11-{d}")
       elif   m=="December":
            if   d<10:
               print(f"YYYY-MM-DD :{y}-12-0{d}")
            else:
               print(f"YYYY-MM-DD :{y}-12-{d}")



try:
      
  main()
except ValueError:
    print("invlid date! .plz enter right date again")
    main()
