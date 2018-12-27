def compare(x,y,z):
    t = 0
    if y > x:
        t=x
        x=y
        y=t
    if z>x:
        t=x
        x=z
        z=t
    if z>y:
        t=y
        y=z
        z=t
    return (x,y,z)

x = input('enter x:')
y = input('enter y:')
z = input('enter z:')
a = compare(x,y,z)
print(a)