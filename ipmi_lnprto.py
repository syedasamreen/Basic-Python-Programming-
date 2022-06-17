f = open('/home/syedasamreen/Downloads/ipmidata.txt','r')
file = f.readlines()
parsed_data = [line.strip().split('|') for line in file]
line_proto = []
measurments = "IPMI_sensor"
for i in parsed_data:
    tag,value,status = i[0], i[1],i[2]
    line = measurments + ": " + "Tags="+ tag + "value=" + value + "status=" + status
    line_proto.append(line)

outfile = open("ipmisensor_dt.txt",'w')
for item in line_proto:
    outfile.write("%s\n" % item)

