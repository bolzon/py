
money = 2000 # global var

def growMoney():
  # uncomment line below to make the code work properly
  global money # this is the secret!!
  money = money + 1

print 'Money before:', money
growMoney()
print 'Money after: ', money
