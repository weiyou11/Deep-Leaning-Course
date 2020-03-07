import math
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
t=int(math.sqrt(b*b-4*a*c))
if t < 0:
    print("无解")
elif t==0:
    x=int(-b/(2*a))
    print("%d" % x)
else:
    x1=int((-b+t)/(2*a))
    x2=int((-b-t)/(2*a))
    print("x1=%d" % x1)
    print("x2=%d" % x2)