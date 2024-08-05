import pandas as pd
from pdb import set_trace
from scipy import interpolate
import matplotlib.pyplot as plt
input_pressure = input("What pressure? ")
df = pd.read_csv("FoIII_pressure-volume.csv")
f = interpolate.interp1d(df.pressure,df.volume, fill_value = 'extrapolate')
print(f(input_pressure))
