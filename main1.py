import netCDF4 as nc
import numpy as np

# Open the NetCDF-4 file
file_path = 'data2/oco2_LtCO2_180918_B11014Ar_221102172618s.nc4'
nc_file = nc.Dataset(file_path, 'r')

# Get a list of variable names
variable_names = nc_file.variables.keys()
# print("Variable names:", variable_names)

# Access a specific variable
variable_name = 'your_variable'
xco2 = nc_file.variables['xco2'][:]
lat = nc_file.variables['latitude'][:]
long = nc_file.variables['longitude'][:]
time = nc_file.variables['time'][:]


# work with the variable data

# print(f"xco2 {xco2}\n lat {lat} \n long{long}\n time {time}")
print(f"{xco2.mask} {xco2.data}")

# for x in lat.data:
#     print(x)

for x in long.data:
    print(x)
# close the file when you're done
nc_file.close()


"""
User input:
lat
long
start time
end time
output:
projection


TODO
with given error range:
    check within radius, return first checked lat long
"""