#!/usr/bin/python -tt

#
# nw-ipmi-stats.py - 2014-05-29
# Developed using Python 2.7
#

#*/1 * * * * /usr/bin/ipmitool sdr list -v > /tmp/tmpsdrsensors.out; mv -f /tmp/tmpsdrsensors.out /tmp/sdrsensors.out
#*/1 * * * * /usr/bin/ipmitool chassis status -v > /tmp/tmpchassisstatus.out; mv -f /tmp/tmpchassisstatus.out /tmp/chassisstatus.out
#*/1 * * * * /usr/bin/ipmitool sdr type "Power Supply" > /tmp/tmppsustats.out; mv -f /tmp/tmppsustats.out /tmp/psustats.out

#pass_persist .1.3.6.1.4.1.36807.5 /etc/snmp/nw-ipmi-stats.py

#snmpwalk -v2c -c netwitness localhost .1.3.6.1.4.1.36807.5.1.1
#snmptable -CB -v2c -c netwitness localhost ipmiFanTable

#snmpwalk -v2c -c netwitness localhost .1.3.6.1.4.1.36807.5.1.2
#snmptable -CB -v2c -c netwitness localhost ipmiChassisTable

#snmpwalk -v2c -c netwitness localhost .1.3.6.1.4.1.36807.5.1.3
#snmptable -CB -v2c -c netwitness localhost ipmiPsuTable

#snmpwalk -v2c -c netwitness localhost .1.3.6.1.4.1.36807.5.1.4
#snmptable -CB -v2c -c netwitness localhost ipmiTemperatureTable

import sys
import os
import subprocess
import re
import pprint
import logging
import logging.handlers
from nwsnmp import nwsnmp
from nwsnmp import AutoVivification

ipmitool = "/usr/bin/ipmitool"
nwIpmiOID = '.1.3.6.1.4.1.36807.5'
ipmiStatsOID = nwIpmiOID + '.1'

ipmiFanOID = ipmiStatsOID + '.1'
ipmiChassisOID = ipmiStatsOID + '.2'
ipmiPsuOID = ipmiStatsOID + '.3'
ipmiTempOID = ipmiStatsOID + '.4'

#if not os.access(ipmitool, os.X_OK):
# print raidUtil + " not found"
# sys.exit(1)

def readFile(file):
  try:
    f = open(file).readlines()
  except:
    print "Couldn't open file %s" % (f)
  return f

def runCmd(cmd,args):
  p = subprocess.Popen([cmd + " " + args],stdout=subprocess.PIPE,shell=True)
  (out,err) = p.communicate()
  p_status=p.wait()
  return out.split("\n")

def grokSdr(list):
  tmpSensors = AutoVivification()
  for l in list:
    if re.match(r'^\s*$',l): continue
    l = l.rstrip('\r\n')
    vals = l.split(':')
    if len(vals) > 1:
      (k,v) = vals
    else:
      k = vals[0]
      v = ''
    #print "k: %s, v: %s" % (k,v)
    if re.match(r'^\S',k):
      sensor = v.lstrip().rstrip()
    else:
      tmpSensors[sensor][k.lstrip().rstrip()] = v.lstrip().rstrip()
  return tmpSensors

def grokChassis(list):
  tmpStats = AutoVivification()
  for l in list:
    if re.match(r'^\s*$',l): continue
    l = l.rstrip('\r\n')
    #print l
    (k,v) = re.split(r'\s*\:\s+',l)[:2]
    tmpStats[k.lstrip().rstrip()] = v.lstrip().rstrip()
  return tmpStats

def grokPsu(list):
  tmpSensors = AutoVivification()
  for l in list:
    if re.match(r'^\s*$',l): continue
    l = l.rstrip('\r\n')
    (k,address,status, entityId, assertion) = re.split(r'\s*\|\s*',l)[:5]
    k = k.lstrip().rstrip() + ' ' + address.lstrip().rstrip()
    tmpSensors[k]['Status'] = status.lstrip().rstrip()
    tmpSensors[k]['Entity ID'] = entityId.lstrip().rstrip()
    tmpSensors[k]['Assertion'] = assertion.lstrip().rstrip()
    #pprint.pprint(tmpSensors)
  return tmpSensors

def addFanStats(snmp):
  inFile = "/tmp/sdrsensors.out"
  #sdrOutput = runCmd(ipmitool,"sdr list -v")
  sdrOutput = readFile(inFile)
  sensors = grokSdr(sdrOutput)

  sensorsL = []
  entityIdL = []
  valueL = []
  unitL = []
  statusL = []

  #pprint.pprint(sensors)
  for k in sensors.keys():  #counting num of fan sensors
    if sensors[k]['Sensor Type (Analog)'] == 'Fan':
      sensorsL.append(k)
      entityIdL.append(sensors[k]['Entity ID'])
      res = re.match(r'^(\d+) \(.*?\) (\S+)$',sensors[k]['Sensor Reading'])
      (speed,unit) = res.groups()[:2]
      valueL.append(speed)
      unitL.append(unit)
      statusL.append(sensors[k]['Status'])

  snmp.addTable(ipmiFanOID)
  snmp.addColumn(sensorsL,'string')
  snmp.addColumn(entityIdL,'string')
  snmp.addColumn(valueL,'integer')
  snmp.addColumn(unitL,'string')
  snmp.addColumn(statusL,'string')

def addChassisStats(snmp):
  inFile = "/tmp/chassisstatus.out"
   #sdrOutput = runCmd(ipmitool,"chassis status")
  chassisOutput = readFile(inFile)
  sensors = grokChassis(chassisOutput)
  #pprint.pprint(sensors)
  sensorsL = []
  valueL = []

  for k in sensors.keys():  #counting num of sensors
    sensorsL.append(k)
    valueL.append(sensors[k])

  snmp.addTable(ipmiChassisOID)
  snmp.addColumn(sensorsL,'string')
  snmp.addColumn(valueL,'string')

def addPsuStats(snmp):
  inFile = "/tmp/psustats.out"
  #sdrOutput = runCmd(ipmitool, 'sdr type "Power Supply"'
  psuOutput = readFile(inFile)
  sensors = grokPsu(psuOutput)
  #pprint.pprint(sensors)
  sensorsL = []
  entityIdL = []
  assertionL = []
  statusL = []
  for k in sensors.keys():  #counting num of sensors
    sensorsL.append(k)
    entityIdL.append(sensors[k]['Entity ID'])
    statusL.append(sensors[k]['Status'])
    assertionL.append(sensors[k]['Assertion'])
  snmp.addTable(ipmiPsuOID)
  snmp.addColumn(sensorsL,'string')
  snmp.addColumn(entityIdL,'string')
  snmp.addColumn(statusL,'string')
  snmp.addColumn(assertionL,'string')


def addTempStats(snmp):
  inFile = "/tmp/sdrsensors.out"
  #sdrOutput = runCmd(ipmitool,"sdr list -v")
  sdrOutput = readFile(inFile)
  sensors = grokSdr(sdrOutput)
  #pprint.pprint(sensors)

  sensorsL = []
  entityIdL = []
  valueL = []
  unitL = []
  statusL = []

  for k in sensors.keys():  #counting num of sensors
    if sensors[k]['Sensor Type (Analog)'] == 'Temperature' and sensors[k]['Sensor Reading'] != 'Disabled':
      #print "SENSOR: " + k
      #print "SENSOR READING: " + sensors[k]['Sensor Reading']
      #pprint.pprint(sensors[k])
      sensorsL.append(k)
      entityIdL.append(sensors[k]['Entity ID'])
      res = re.match(r'^(-?\d+) \(.*?\) (.*)$',sensors[k]['Sensor Reading'])
      (temp,unit) = res.groups()[:2]
      valueL.append(temp)
      unitL.append(unit)
      statusL.append(sensors[k]['Status'])
  snmp.addTable(ipmiTempOID)
  snmp.addColumn(sensorsL,'string')
  snmp.addColumn(entityIdL,'string')
  snmp.addColumn(valueL,'integer')
  snmp.addColumn(unitL,'string')
  snmp.addColumn(statusL,'string')


def main():
  global logger
  #set up logging
  logger = logging.getLogger(__name__)
  logger.setLevel(logging.INFO)
  #uncomment next two lines to log to syslog
  handler = logging.handlers.SysLogHandler(address = '/dev/log')
  logger.addHandler(handler)
  logger.info("Starting nwipmi-stats pass_persist agent")

  #create SNMP handler object
  snmp = nwsnmp(nwIpmiOID)
  snmp.addOID(ipmiStatsOID)

  addFanStats(snmp)
  addChassisStats(snmp)
  addPsuStats(snmp)
  addTempStats(snmp)

  #snmp.printOids()
  #snmp.printTree()

  snmp.listen()

main()
