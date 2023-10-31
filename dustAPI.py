from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import requests
import serial

url = 'https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'
queryParams = '?' + urlencode({quote_plus('serviceKey'):
'jNlGZq2anntgVGZKB/yVuuRSy+YMGBO54dwkZf2W//oz/Q/gQpDYONMWsFgyDV7RSyBmlSKKS6ClXa6Uco2k+Q=='
                               ,quote_plus('returnType'): 'xml'
                               ,quote_plus('numOfRows'): '10'
                               ,quote_plus('pageNo'): '1'
                               ,quote_plus('stationName'): '주안'
                               ,quote_plus('dataTerm'): 'DAILY'
                               ,quote_plus('ver'):'1.0'})

res = requests.get(url+queryParams)
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.find_all('item')
print(data)

for item in data:
    datatime = item.find('datatime')
    pm25value = item.find('pm25value')
    print(datatime.get_text())
    print(pm25value.get_text())

port = '/dev/ttyACM0'
brate = 9600

seri = serial.Serial(port, baudrate = brate, timeout = None)
print(seri.name)

seri.write(b'\x0101')

a=1
while a:
    if seri.in_waiting != 0 :
        content = seri.readline()
        print(content.decode())
        a=0

if float(content.decode()) < float(pm25value.get_text()):
        print("close door")
else:
        print("open door")
