friends = [ 'john', 'paty', 'gary', 'michael' ]
for i, name in enumerate(friends):
  print 'iteration {0} is {1}'.format(i, name)
  print '-- iteration {iteration} is {name}'.format(iteration=i, name=name)
