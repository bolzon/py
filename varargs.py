
# variable number of arguments

def varargs(arg1, *vargs):
  print 'arg1 is', arg1
  for arg in range(len(vargs)):
    print ('arg%d' % (arg + 2)), 'is', vargs[arg]
  print ''

varargs(10)
varargs(20, 30, 40)
varargs(50, 60, 70, 80, 90)
