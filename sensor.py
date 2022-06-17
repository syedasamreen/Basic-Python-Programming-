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
