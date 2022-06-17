f = open('/home/syedasamreen/Downloads/ipmidata.txt','r')
lines = f.readlines()
measurments = "CPU_metrics
tag1,tag2,value,unit,status = [],[],[],[],[]

for line in lines:
    line1 = line.replace(" | ", '')
    line2 = line1.strip().split()
    tag1.append(line2[0])
    tag2.append(line2[1])
    value.append(line2[2])
    unit.append(line2[3])
    status.append(line2[4])
f.close()   
