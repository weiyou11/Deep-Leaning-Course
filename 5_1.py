import numpy as np
t=int(input("t="))
i=0
j=1
np.random.seed(612)
while i<1000:
    x=np.random.uniform(0,1)
    if i%t==0:
        print("%d\t %d\t %f\t" %(j,i,x))
        j=j+1
    i=i+1