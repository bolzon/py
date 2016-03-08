
from sys import argv

argslen = len(argv) - 1
print 'Number of args:', argslen

script = argv[0]
print 'The script is "%s"' % script

if argslen >= 3:
  # disconsider the first argument,
  # that's the script name
  first, second, third = argv[1:]
  print 'First: ', first
  print 'Second:', second
  print 'Third: ', third
else:
  print 'Must be 3 or more'
