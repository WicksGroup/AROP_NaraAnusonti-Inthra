import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
df_hyades = pd.read_csv("quartz hugoniot.csv")
df_russian = pd.read_csv("quartz_hugoniot_russian.csv")
plt.plot(df_hyades.pressure, df_hyades.density, label = "hyades", c = "red", ls = ':')
plt.plot(df_russian.pressure, df_russian.density, label = "russian", c = "green", ls = '--')
plt.legend()
plt.xlabel("pressure (GPa)")
plt.ylabel("density (g/cc)")
plt.title("quartz")
plt.show()