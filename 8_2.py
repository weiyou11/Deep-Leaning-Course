import tensorflow as tf
x=tf.constant([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y=tf.constant([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])
xy=tf.multiply(x,y)
sx=sy=sxy=xsq=0
n=10
for i in range(10):
    sx=sx+x[i]
    sy=sy+y[i]
    sxy=sxy+xy[i]
    xsq=xsq+x[i]*x[i]
w=(n*sxy-sx*sy)/(n*xsq-sx**2)
b=(sy-w**sx)/n
print("w:",w)
print("b:",b)