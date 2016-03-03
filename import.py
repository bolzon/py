
# it's possible to import the whole module
import glob

# or just some functions of it
from math import asin

print 'asin(1) =', asin(1) # prints the result
print 'acos(1) =', acos(1) # gives an error (acos was not imported)
