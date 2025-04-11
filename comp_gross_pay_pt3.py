hrs = input("Enter Hours:")
rte = input("Enter Rate:")

h = float(hrs)
r = float(rte)


def computepay(h, r):
    if h > 40:
        gross = (r*1.5) * (h-40) + 40*r

    if h <= 40:
        gross = h * r
    
    return gross

p = computepay(h, r)

print("Pay", p)
