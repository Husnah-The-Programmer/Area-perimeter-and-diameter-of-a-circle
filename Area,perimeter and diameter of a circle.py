def area_of_circle(Radius):
    area = 3.14 * Radius ** 2
    return area
def perimeter_of_circle(Radius):
    perimeter = 2 * 3.14 * Radius
    return perimeter
def diameter_of_circle(Radius):
    diameter = 2 * Radius
    return diameter

Radius=int(input("Enter Radius:\n"))
print("The area of the circle is %0.2f" %area_of_circle(Radius))
#perimeter=int(input("Enter perimeter:\n"))
print("The perimeter of the circle is %0.2f" %perimeter_of_circle(Radius))
#diameter=int(input("Enter diameter:\n"))
print("The diameter of the circle is %0.2f" %diameter_of_circle(Radius))
