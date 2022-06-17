import pandas as pd
from influxdb import DataFrameClient
dbhost = 'localhost'
dbport = 8086
dbuser = ' '
# dbpasswd = ' '
dbname = 'HVAC_Temp'
protocol = 'line'

# fields from csv
Fields = ['Time','Return_Air_Temperature','Rack1_Exhaust_Temperature','HVAC_New.Return_Humidity']

#Tag Fields
datatags = ['Return_Air_Temperature','Rack1_Exhaust_Temperature','HVAC_New.Return_Humidity']


# Read csv 
df = pd.read_csv('/home/syedasamreen/Documents/HVAC RACK/data/Historical Temperature Data.csv',
                 index_col=False, parse_dates = ['Time'])
# set index
df.set_index('Time',inplace = True)
print(df.head())

client = DataFrameClient(dbhost, dbport, dbname)
client.create_database(dbname)
#client.get_list_database()
client.switch_database(dbname)
client.write_points(df,"Tempdata",tags=None,tag_columns=datatags,protocol=protocol)
result = client.query('select * from Tempdata;')
#print(result)
