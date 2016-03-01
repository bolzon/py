#!/usr/bin/python
import time
import calendar

localtime = time.asctime( time.localtime(time.time()) )
print 'Local time is:', localtime, '\n'

cal = calendar.month(2015, 4)
print 'Here is the worst calendar ever:\n'
print cal
