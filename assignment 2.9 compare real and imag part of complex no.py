x=complex(input("Enter a complex no"))#convert string returned by input to complex no
y=x.real#real part
z=x.imag#imaginary part
print("the real part is {} ,the complex part is {}".format(y,z))
print("the complex no is {}".format(x))
print("the complex no is ",end="->")#again  printing in other method
#no new line b/w these print statements
print(y,z,sep="+",end="j")
print("\n")
if y>z:
    print("the real part {} is greater than imaginary part{}".format(y,z))

elif y==z:
    print("the real part {} is equal to imaginary part{}".format(y,z))
else:
     print("the real part {} is less than than imaginary part{}".format(y,z))
#indentataion of if elif and else must match
     # ie sentence inside elif or else and if may have different indentation
     #but else must lie below if and else must lie below elif
