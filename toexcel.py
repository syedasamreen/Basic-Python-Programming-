local_storage = '/home/syedasamreen/'
netcdf_dir = local_storage 
import xarray as xr
import os

netcdf_flname = '/home/syedasamreen/Downloads/ncum_imdaa_reanl_HR_APCP-sfc_2015010100-2015123123.nc'
# netcdf_flin = netcdf_dir + netcdf_flname
csv_flout = netcdf_dir  + '.csv'
ds = xr.open_dataset(netcdf_flname)
df = ds.to_dataframe()
#df.to_csv(csv_flout)
#print(df)
df.to_excel('ntcd1.xlsx',engine='xlsxwriter')
