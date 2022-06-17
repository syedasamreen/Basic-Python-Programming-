import os
from influx_line_protocol import Metric
f1 =open('/home/syedasamreen/Downloads/ipmidata.txt','r')
l =  f1.readlines()
f1.close()
data = 'IPMI_Sensor.txt'
f2 = open(data,'a+')
for l1 in l:
    l1 = l1.strip().split('|')#;print(l1[2])
    l2 = l1[0].strip().split(' ')#;print(l2[0])
    l2 = '_'.join(l2)#;print(l2)
    l3 = l1[1].strip().split()#;print(l3[0])
    l33 = l3[1:]
    l4 = '_'.join(l33)#;print(l4)
    l5 = l1[2]#;print(l5)
    # l6 = measuremnt+','+"Tags="+l2+' '+"Value="+l3[0]+','+"Unit="+l4+','+"Status="+l5
    metric = Metric("IPMI_sensor")
    metric.with_timestamp(16478669490000)
    metric.add_tag("Tag",l2)
    metric.add_value("value",l3[0])
    metric.add_value("unit",l4)
    metric.add_value("status",l5)
    f2.write("%s\n" % metric)
f2.close()
command = "curl -i -XPOST 'http://localhost:8086/write?db=IPMIsensor_data' --data-binary @"+data
os.system(command)





