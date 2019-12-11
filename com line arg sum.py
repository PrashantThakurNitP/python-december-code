from sys import argv
print("Inside com line arg sum.py program")
count=0
y=0
for x in argv:
    if x=='com line arg sum.py':
        continue
    y=y+int(x)
    count+=1
print("Total no of argument is {} and the sum of argument is {}".format(count,y))
    
    
