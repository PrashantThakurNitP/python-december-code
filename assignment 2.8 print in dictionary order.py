x=input("input first string :")
y=input("enter second string : ")
z=input("enter third string : ")
if x>=y:
   if y>=z:
    print("the string in dictionary order are")
    print(z,y,x,sep="\n")
   elif z>x:
    print("the string in dictionary order are")
    print(y,x,z,sep="\n")
   else:
    print("the string in dictionary order are")
    print(y,z,x,sep="\n")
       
else :
   if z>=y:
    print("the string in dictionary order are")
    print(x,y,z,sep="\n")
   elif x>=z:
    print("the string in dictionary order are")
    print(z,x,y,sep="\n")
   else:
    print("the string in dictionary order are")
    print(x,z,y,sep="\n")
    

    
    
    
