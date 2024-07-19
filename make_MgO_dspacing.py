import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import math

pressure = 260
reflections = ["110","111","002","211"]
points = {"35":[2.461,0.001],"37":[2.351, 0.001],"42":[2.059,0.002],"50":[1.743,0.001],"60":[1.491,0.001],"72":[1.249,0.001],"76":[1.205,0.0002]}
def dspacing(rho,x):
    h = x[0]
    k = x[1]
    l = x[2]
    return math.sqrt((6*40.304/rho)**(2/3)/(eval(h)**2+eval(k)**2+eval(l)**2))
df = pd.read_csv("MgO_hugonoit.csv")
for x in reflections:
    plt.plot(df.pressure, df.density.apply(dspacing, args = (x,)), label = x)
for key in points.keys():
    mypoints = points[key]
    plt.scatter(pressure,mypoints[0],label = f"point at {key} 2-theta", c = (np.random.random(), np.random.random(), np.random.random()), marker = "d")
    plt.errorbar(pressure, mypoints[0], yerr = mypoints[1], ecolor = "black")
plt.legend()
plt.title("d-spacing MgO B1")
plt.xlabel("pressure (GPa)")
plt.ylabel("d-spacing(a)")
plt.savefig("MgO_B1_dspacing.png")
plt.show()
