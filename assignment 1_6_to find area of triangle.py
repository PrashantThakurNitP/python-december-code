from math import sqrt
x=float(input("enter first side"))
y=float(input("enter second side"))
z=float(input("enter third side"))
s=(x+y+z)/2# semiperimeter

if x+y>=z and y+z>=x and x+z>=y:# triangle is valid
  a=sqrt(s*(s-x)*(s-y)*(s-z))

  print("the 1st side  is {},2nd side is {} , third side is {} and area is {}".format(x,y,z,a))
  print(x,y,z,a,end=";",sep=":")
else:#if sum of two side is less than third
   if  x+y<z:
      print("sum of 1st and 2nd side is {} which is less than 3rd side which is {}".format(x+y,z))
   elif  x+z<y:
      print("sum of 1st and 3rd side is {} which is less than 2nd side which is {}".format(x+z,y))
   else:#z+y<x
      print("sum of 2nd and 3rd side is {} which is less than 1st side which is {}".format(z+y,x))

