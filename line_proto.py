f1 =open('/home/syedasamreen/Downloads/ipmidata.txt','r')
l =  f1.readlines()
f1.close()
measuremnt = "IPMI_sensor"
for l1 in l:
    l1 = l1.strip().split('|')#;print(l1[2])
    l2 = l1[0].strip().split(' ')#;print(l2[0])
    l2 = '_'.join(l2)#;print(l2)
    l3 = l1[1].strip().split()#;print(l3[0])
    l33 = l3[1:]
    l4 = '_'.join(l33)#;print(l4)
    l5 = l1[2]#;print(l5)
    l6 = measuremnt+','+"Tags="+l2+' '+"Value="+l3[0]+','+"Unit="+l4+','+"Status="+l5
    print(l6)


