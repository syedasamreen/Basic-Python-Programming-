###Get the aggregate CPU statistics
import sys
import libvirt

domName = 'Centos7.9_test'

conn = None
try:
    conn = libvirt.open("qemu+SSH://root@10.1.0.162:22/system")
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

dom = conn.lookupByID(127)
if dom == None:
    print('Failed to find the domain '+domName,file=sys.stderr)
    exit(1)
    
stats = dom.getCPUStats(True)
print('cpu_time:    '+str(stats[0]['cpu_time']))
print('system_time: '+str(stats[0]['system_time']))
print('user_time:   '+str(stats[0]['user_time']))

conn.close()
exit(0)
