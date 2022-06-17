import sys
import libvirt

conn = None
try:
    conn = libvirt.open("qemu+SSH://root@203.129.243.197:22/system")
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

pools = conn.listAllStoragePools(0)
if pools == None:
    print('Failed to locate any StoragePool objects.', file=sys.stderr)
    exit(1)

for pool in pools:
    print('Pool: '+pool.name())

conn.close()
exit(0)
