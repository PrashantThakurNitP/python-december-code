a=[1,2,3]
b=[4,5,6]
c=a+b# list are appended
c#it donot print element of list if written in file,it print only when written
#in shell,not here
print("after appending")
print(c)
c.insert(-1,100)#index start from right and in decreasing index ie 0,-1,-2etc
#other element left and at that positin move to left when 100 insert
print("inserting 100 at -1")
print(c)#last index 5
c.insert(10,200)#it insert at index 6
print(" tring to insert 200 at 10 which is not possible ")
print(c)
c.append(500)
print("appending 500")
print(c)
x=c.pop()#remove last element
print("the last element popped is",x)
print("the list after poping is {}".format(c))
y=c.pop(1)#remove element ar index 1 and return it to y
print("the list after pop is {} and element popped is {}".format(c,y))
y=c.remove(4)#remove remove first occurence of 4 but it is not returned
print("the list after remove operation  is {} and element popped is {}".format(c,y))
#y contain None as remove donot return unlike  pop
c.sort()
print("the sorted list is ",c)
print(" list a is",a)
a=a*3
print("after repet operation a is ",a)
print("intially b has",b)
x=b.pop(1)
print("the element in b after pop at index 1 are {}and popped element is {}".format(b,x))
