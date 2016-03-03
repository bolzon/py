
import smtplib

sender = 'alexandre.bolzon@venturus.org.br'
receivers = [sender]
message = 'This is the test message'

try:
  so = smtplib.SMTP('brcpsex01')
  so.sendmail(sender, receivers, message)
  print 'Email successfully sent'
except Exception, ex:
  print 'Error:', ex
