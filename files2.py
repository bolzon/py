
from os import remove

# creates a new file
print 'Creating new file'
newFile = open('test.txt', 'w')

# prints the file info
print 'File info:'
print '\tname:', newFile.name
print '\tis closed:', newFile.closed
print '\topening mode:', newFile.mode
print '\tsoftspace flag:', newFile.softspace

# writes to the file and saves it
newFile.write('Hello world!')
newFile.close()

# opens the file for reading
f = open('test.txt', 'r')
print 'File "%s" is open and its content is:' % f.name
print f.read()
f.close()

# removes the test file
print 'Removing file'
remove('test.txt')
