import pandas as pd
from pdb import set_trace
from scipy import interpolate
df = pd.read_csv("MgO_hugonoit.csv",header = None)
f = interpolate.interp1d(df[1],df[0])
print (f(260),fill_value = 'extrapolate', bounds_error = False)
