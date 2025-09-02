# Ask the user to input three angles and check if the triangle has a right angle.
# Your code should make sure that all three angles are valid and make up a triangle.

print("give me three angles of a triangle of your choosing")

a = int(input("Ange första vinkeln: "))
b = int(input("Ange andra vinkeln: "))
c = int(input("Ange tredje vinkeln: "))

if a + b + c == 180 and (a == 90 or b == 90 or c == 90):
    print("wow u managed to do a triangle and it is a right-angled triangle")
elif a + b + c == 180:
    print("wow u managed to do a triangle")
else:
    print("ojojoj en triangle har totalt 180 grader")
