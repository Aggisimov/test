import math

# A: 4,4
# B: 0,-1
# k= delta a / delta b
# y= kx + m

y1 = 4
y2 = 1
x1 = 4
x2 = 0

k = (y2-y1)/(x2-x1)
print(k)

m = y1-(k*x1)

print(m)
