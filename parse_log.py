#!/usr/bin/env python
import re , sys
#open the file for reading
try:
  handle = open('test-sample.log','r')
except IOError as e:
  print e
  sys.exit()
#parse and match the required pattern
for line in handle:
    line = line.rstrip()
    id=re.findall('\[\d{5}\]', line)
    subject=re.findall('\s[T][=].*', line)
    if subject:
      print "Message id is : ", id[0].lstrip('[').rstrip(']') , " and subject is : ", subject[0].split('=')[1]
