import subprocess

Debug = True
#command1 = 'ipmitool -I lanplus -H '+host+' -U '+user+' -P '+passw+' sdr list'
command1 = 'ipmitool -I lanplus -H 10.1.0.29 -U root -P IDRAC@v!gy@nlabs chassis status'

sensor_output1 = subprocess.getoutput(command1)


