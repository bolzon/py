
try:
  f = open('notexistent.txt', 'r')
  print 'File content:', f.read()
except IOError, ex:
  print 'File could not be opened'
  print 'Error:', ex
#except ..:
  #..
else:
  print 'File was read successfully'
finally:
  print 'Exiting'
