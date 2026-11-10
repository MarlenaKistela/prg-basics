###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
def triangle_area(a,b,c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    # Calculate the area using Heron's formula
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

print('The area of ​​a triangle with sides 3,4,5 is', triangle_area(3, 4, 5))
print('The area of ​​a triangle with sides 5,12,13 is', triangle_area(5, 12, 13))
print('The area of ​​a triangle with sides 7,24,25 is', triangle_area(7, 24, 25))
