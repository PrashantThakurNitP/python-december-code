s="don't avoid practice"#print  don't avoid practice
s1='"life is precious"'#print   "life is precious"
s2="""life is precious """#print   life is precious
s3='''life is precious''' #print life is precious
s4="'life is pecious'" #print 'life is pecious'
s5='''don't avoid practice'''
#s6="""teachers day is "my day""""   #it gives error
s7='''teachers day is "my day"'''#print   teachers day is "my day"
s8="teacher day is my day"""#print   teacher day is my day
s9=  """hi there !
        i am prashant thakur
        i can code in python"""
    #multi line only possible in triple quotes
#    s10=  "hello
#           everyone"
#
print(s)#print don't avoid practice
print(s1)#print "life is precious"
print(s2)#print life is precious
print(s3)#print life is precious
print(s4)#print 'life is pecious'
print(s5)#print don't avoid practice
#print(s6)
print(s7)
print(s8)
print(s9)
#print(s10) it gives error as multi line sting not possible through double codes
print("printing all sublstring seperated by space")
s.split(' ')
l1=[]
for x in s.split(' '):
    
    print(x)
    l1.append(x)
i=0;
print("printing item of list")
for x in l1:
    print(l1[i])
    i+=1#i++ not available here




    

