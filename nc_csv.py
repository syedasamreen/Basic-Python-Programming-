import xarray as xr
import os
local_storage_directory = '/home/syedasamreen/Downloads/'
netcdf_dir = local_storage_directory + 'ncn/'
csv_dir = local_storage_directory + 'csv/
files_to_convert = local_storage_directory + 'ncn/'
for filename in os.listdir(files_to_convert):
    ds = xr.open_dataset(files_to_convert + filename)
    df = ds.to_dataframe()
    df.to_csv(csv_dir + filename[:-3] + '.csv')
    print(filename + ' has been processed to .csv')

