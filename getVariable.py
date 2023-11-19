import netCDF4 as nc
import numpy as np

# Open the NetCDF-4 file
file_path = 'data2/oco2_LtCO2_180905_B11014Ar_221102171836s.nc4'
nc_file = nc.Dataset(file_path, 'r')

# Get a list of variable names
variable_names = nc_file.variables.keys()
print("Variable names:", variable_names)


"""
data
lat
long
time
xco2
xco2_uncertainy"""