# Gets data by taking in lat and long, and returns projection
import re
import os
import netCDF4 as nc
import numpy as np

def find_file_by_date(folder_path, target_date):
    # Get a list of all files in the specified folder
    files = os.listdir(folder_path)

    # Iterate through the files to find a match
    for filename in files:
        # Extract the date from the filename
        # Search for the pattern in the filename
        # Define a regular expression pattern to match the date
        # pattern = re.compile(r'\d{6}')
        pattern = re.compile(r'\d{6}')
        match = re.search(pattern, filename)
        if match:
            # print(match.group())
            if match.group() == str(target_date):
                return filename

    # Return None if no matching file is found
    return None

def getData(lat, long, time):
    file = find_file_by_date('data2',time)
    print(file)
    if file == None:
        return None
    nc_file = nc.Dataset("data2/" + file, 'r')
    xco2 = nc_file.variables['xco2'][:].data
    # print(xco2)
    lati = nc_file.variables['latitude'][:].data
    longt = nc_file.variables['longitude'][:].data
    time = nc_file.variables['time'][:].data
    two_d_list = np.transpose(np.array([lati,longt,xco2,time]))
    # print(type(two_d_list))
    two_d_list[two_d_list[:, 0].argsort()]
    for x in two_d_list:
        print(f"{round(x[0],1)} \n {round(x[1],1)}")
        if round(x[0],1) == round(lat,1) and round(x[1],1) == round(long,1):
            return x[3]
            
    # for x in two_d_list:
    #     if x[0] == lat and x[1] == long:
    #         return 


print(getData(-2.1,-157.6,180918))
        
    


    



