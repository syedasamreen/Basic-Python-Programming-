import subprocess


host = '10.1.0.29'
user = 'root'
passw = 'IDRAC@v!gy@nlabs'
command1 = 'ipmitool -I lanplus -H '+host+' -U '+user+' -P '+passw+' sdr list'
#print(command1)
sensor_output = subprocess.getoutput(command1)
print(sensor_output)

