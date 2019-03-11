def sort_int(a, b, c,d):
    L = [a, b, c, d]
    L.sort()
    return L

x=int(input("x:"))
y=int(input("y:"))
z=int(input("z:"))
w=int(input("w:"))
x, y, z = sort_int(x,y,z,w)
print(x, y, z,w)
