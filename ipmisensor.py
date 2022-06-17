import subprocess
import requests
import re

import handlers as func

def fanTempMeasure(ipmiHost,valueInsertList,timeStamp):
	measurements = []

	hostname = ipmiHost.hostname
	username = ipmiHost.username
	password = ipmiHost.password

	output = func.ipmiTool(hostname,username,password)

	for line in output:
		line = line.split("|")
		for idx,value in enumerate(line):
			# print(value.strip())
			value = re.findall(r'^(\d*\.?\d*) ',value.strip())
			if value:
				device = line[idx-1].strip()
				value = value[0]
				measurements.append((device,value))
				pass

	for device,value in measurements:
		print(device,value)
		device = device.replace(" ", "")
		value = value.replace(" ", "")
		if "fan" in device.lower():
			item = "fan_rpm"
		else:
			item = "temperature"

		data_fanTemp = [hostname,device,item,value]
		valueInsertList.append(func.getPostData(data_fanTemp,timeStamp))
	pass
	return valueInsertList
	
	
	
	
	
	
##################################################################	

    def ____run(self, command):
        procs = {}
        for node in self.nodes:
            ip = node['ip']
            user = node['user']
            password = node['password']
            cmd = f'ipmitool -H {ip} -U {user} -P {password} {command}'
            procs[ip] = subprocess.Popen(cmd,
                                         shell=True,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT,
                                         universal_newlines=True)
        while procs:
            for ip, proc in procs.items():
                if proc.poll() is not None:  # command finished
                    del procs[ip]
                    if proc.returncode == 0:
                        print(f"{ip}\t: SUCCESS ")
                    else:
                        print(f"{ip}\t: FAIL ({proc.stdout})")
                    break
                    
                    
                    
##################################################################################################
import sys
import subprocess
import time
import csv

duration = sys.argv[1]
file_name = sys.argv[2]
sensors = sys.argv[3:]
time_begin = time.time()

with open(file_name + '.csv', 'w') as file_out:
    write = csv.writer(file_out)
    first_row = ['Sensor_ID', 'Entity_ID', 'Sensor_Type_Threshold_',
                 'Sensor_Reading', 'Status',
                 'Lower_Non_Recoverable', 'Lower_Critical',
                 'Lower_Non_Critical', 'Upper_Non_Critical', 'Upper_Critical',
                 'Upper_Non_Recoverable', 'Positive_Hysteresis',
                 'Negative_Hysteresis', 'Assertion_Events',
                 'Assertions_Enabled', 'Deassertions_Enabled', 'Time_elapsed']
    write.writerow(first_row)
    end = time.time() + float(duration)
    while end > time.time():
        for sens in sensors:
            command = ['sudo', 'ipmitool', 'sensor', 'get', sens]
            process = subprocess.run(
                    command,
                    stdout=subprocess.PIPE,
                    universal_newlines=True)
            output = process.stdout
            output = output.split('\n')[2:-2]
            current_row = []
            current_row.append(sens)
            for i in range(len(output)):
                output[i] = output[i].split(':')
                output[i][0] = output[i][0].replace(' ', '')
                for j in range(1,len(output[i])):
                    output[i][j] = output[i][j].split()
                    if len(output[i][j]) > 0:
                        current_row.append(output[i][j][0])
                    else:
                        current_row.append('')
            current_row.append("{:.5f}".format(time.time() - time_begin))
            write.writerow(current_row)	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
