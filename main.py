def findCircum(rad):
    return 2 * 3.14 * rad

print("Enter Radius of Circle: ", end="")
r = float(input())

c = findCircum(r)
print("\nCircumference = {:.2f}".format(c))