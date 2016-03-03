
# parent class

class Parent:
  'Parent sample class'
  __parentAttr = 10

  def __init__(self):
    print 'Calling parent constructor'

  def parentMethod(self):
    print 'Calling parent method'

  def setAttr(self, attr):
    Parent.__parentAttr = attr

  def getAttr(self):
    return Parent.__parentAttr

# child class

class Child(Parent):
  'Child sample class'

  def __init__(self):
    print 'Calling child constructor'

  def childMethod(self):
    print 'Calling child method'

# testing class inheritance

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(20)
print c.getAttr()
