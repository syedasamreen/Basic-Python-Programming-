
import cdsapi
import netCDF4
from netCDF4 import num2date
import numpy as np
import os
import pandas as pd
 
# Retrieve data and store as netCDF4 file
c = cdsapi.Client()
file_location = '/home/syedasamreen/Downloads/ncum_imdaa_reanl_HR_APCP-sfc_2001010100-2001123123.nc'
c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type':'reanalysis',
        'variable':'2m_temperature',  # 't2m'
        'year':'2019',
        'month':'06',
        'day':[
            '24','25'
        ],
        'time':[
            '00:00','06:00','12:00',
            '18:00'
        ],
        'format':'netcdf'
    },
    file_location)
 
# Open netCDF4 file
f = netCDF4.Dataset(file_location)
 
# Extract variable
t2m = f.variables['t2m']
 
# Get dimensions assuming 3D: time, latitude, longitude
time_dim, lat_dim, lon_dim = t2m.get_dims()
time_var = f.variables[time_dim.name]
times = num2date(time_var[:], time_var.units)
latitudes = f.variables[lat_dim.name][:]
longitudes = f.variables[lon_dim.name][:]
 
output_dir = './'




filename = os.path.join(output_dir, 'table.csv')
print(f'Writing data in tabular form to {filename} (this may take some time)...')
times_grid, latitudes_grid, longitudes_grid = [
    x.flatten() for x in np.meshgrid(times, latitudes, longitudes, indexing='ij')]
df = pd.DataFrame({
    'time': [t.isoformat() for t in times_grid],
    'latitude': latitudes_grid,
    'longitude': longitudes_grid,
    't2m': t2m[:].flatten()})
df.to_csv(filename, index=False)
print('Done')
