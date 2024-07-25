from scipy.io import netcdf_file
import pandas as pd
file = netcdf_file("combined_simulation_quartz.cdf")
pressure = file.variables["Pres"].data.T[0]*10**-10
density = file.variables["Rho"].data.T[0]
df_pres = pd.DataFrame({"pressure":pressure,"density":density})
df_pres.to_csv("quartz hugoniot.csv", index = False)
