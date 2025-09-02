import math

## A right angled triangle has hypothenuse
#  c = 7.0 and a cathetus a = 5.0 length units. 
# Compute the other cathetus and round to one decimal.
# a^2 + b^2 = c^2


a = 5
c = 7

a2 = pow(a, 2)
c2 = pow(c, 2)

b = math.sqrt(c2-a2)


print(f"{b:.1f} units of lenght")


