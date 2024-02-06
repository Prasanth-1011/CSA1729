def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def Can_Measure(x, y, z):
    if z > x + y or z % gcd(x, y) != 0:
        return ["Can't Measure Desired Amount"]
    S = []
    i, j = 0, 0
    S.append((i, j))  # Initial state
    while i != z and j != z:
        if i == 0:
            i = x
        elif j == y:
            j = 0
        else:
            Pour = min(j1, y - j2)
            i -= Pour
            j += Pour
        S.append((i, j))
    return S

x, y, z = 3, 5, 4
Steps = Can_Measure(x, y, z)
for i in Steps:
    print(i)
print("Reached Target Capacity of", z, "Litres")
