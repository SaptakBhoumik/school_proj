def quadratic_solver(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    return (root1, root2)
print("ax^2 + bx + c = 0")
a=float(input("Enter a:-"))
b=float(input("Enter b:-"))
c=float(input("Enter c:-"))
print("Roots:-",quadratic_solver(a,b,c))