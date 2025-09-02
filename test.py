import math

# p1 (3,5) 
# p2 (-2,4)

x1 = 3
x2 = -2
y1 = 5
y2 = 4

dx = x2 - x1
dy = y2 - y1
print(dx)
print(dy)

distance = math.sqrt((dx ** 2) + (dy ** 2))

print(f"{distance:.1f}")