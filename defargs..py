
# default function argument

def printfoo(name, age = 31):
  print 'Your name is', name.capitalize() + ', age', age
  return # this is optional

printfoo('alexandre')
printfoo('valks', 34)
