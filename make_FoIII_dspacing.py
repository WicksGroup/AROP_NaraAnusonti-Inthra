import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import math

pressure = 260
a0 = 2.640
b0 = 8.596
c0 = 9.04
v0 = a0*b0*c0
m = 140.666
reflections = ["011","002","020","012","031","100","040"]
points = {"35":[2.461,0.001],"37":[2.351, 0.001],"42":[2.059,0.002],"50":[1.743,0.001],"60":[1.491,0.001],"72":[1.249,0.001],"76":[1.205,0.0002]}
def dspacing(rho,x):
    h = x[0]
    k = x[1]
    l = x[2]
    v = m/rho
    p0 = v0/v
    p = p0**(1/3)
    a = a0/p
    b = b0/p
    c = c0/p
    return 1/math.sqrt(eval(h)**2/a**2+eval(k)**2/b**2+eval(l)**2/c**2)
df = pd.read_csv("Forsterite hugonoit.csv")
for x in reflections:
    plt.plot(df.pressure, df.density.apply(dspacing, args = (x,)), label = x)
for key in points.keys():
    mypoints = points[key]
    plt.scatter(pressure,mypoints[0],label = f"point at {key} 2-theta", c = (np.random.random(), np.random.random(), np.random.random()), marker = "d")
    plt.errorbar(pressure, mypoints[0], yerr = mypoints[1], ecolor = "black")
plt.legend()
plt.title("d-spacing FoIII")
plt.xlabel("pressure (GPa)")
plt.ylabel("d-spacing(a)")
plt.savefig("FoIII_dspacing.png")
plt.show()

