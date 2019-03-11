import operator
x=int(input("x:"))
y=int(input("y:"))
z=int(input("z:"))
w=int(input("w:"))
tmp = {'x', 'y', 'z','w'}
sorted(tmp.iteritems(),key=operator.itemgetter(1),reverse=False)
print ' > '.join(tmp.keys())
