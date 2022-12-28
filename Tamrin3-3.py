# Hamid HajiRahimi
# Tamrin: 3-2
# Solving 2nd Degree Equation:

############################################################

a,b,c = int(input("a : ")) , int(input("b : ")) , int(input("c : "))
delta = ((b**2) - 4*a*c)
print("")
print("Δ = {}".format(delta))

############################################################

if delta > 0:
    x1 = (-b+(delta**0.5))/(2*a)
    x2 = (-b-(delta**0.5))/(2*a)
    print ("Equation has 2 roots: \nx1 = {}".format(x1))
    print ("x2 = {}".format(x2))


elif delta == 0:
    x1 = (-b+(delta**0.5))/(2*a)
    print ("Equation has 1 root: \nx1 = {}".format(x1))

else:
    print("Error, We have no answer : Δ < 0")
    exit()