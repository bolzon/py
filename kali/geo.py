import pygeoip

gi = pygeoip.GeoIP('Geo.dat')

gi.org_by_name('dell.com')
