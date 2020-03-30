import tensorflow as tf
x=tf.constant([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y=tf.constant([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])
x_x1=tf.reduce_mean(x)
y_y1=tf.reduce_mean(y)
s=s1=0
for i in range(10):
    s=s+(x[i]-x_x1)*(y[i]-y_y1)
    s1=s1+(x[i]-x_x1)**2
    print("x:",x[i])
w=s/s1
b=y_y1-w*(x_x1)
print("w:",w)
print("b:",b)