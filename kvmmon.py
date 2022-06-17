import libvirt
import sys

import libvirt
conn = libvirt.open('qemu:///system')
conn.getHostname()
conn.getMaxVcpus('qemu')
print(conn.getSysinfo())
conn.listDomainsID()
domainIDs = conn.listDomainsID()
for domainID in domainIDs:
    domain = conn.lookupByID()
    uuid = domain.UUIDString()
    print(uuid)
