import zipfile

zf = zipfile.ZipFile('evil.zip')
passFile = open('dictionary.txt', 'r')

for line in passFile.readlines():
  passwd = line.strip('\n')
  try:
    zf.extractall(pwd=passwd)
    print '[+] Password = ' + passwd + '\n'
    exit(0)
  except Exception, e:
    pass
