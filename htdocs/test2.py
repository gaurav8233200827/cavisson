#!C:\Users\Gaurav\AppData\Local\Programs\Python\Python36/python.exe
print ('Content-type: text/html\n\n')
import urllib.request
import re
import time

def cleanhtml(raw_html):
  c = re.compile('<.*?>')
  ct = re.sub(c, '', raw_html)
  return ct
  
start_time = time.time()
for i in range(1,10000):
	# x = urllib.request.urlopen('http://127.0.0.1/web.html')
	y = urllib.request.urlopen('http://127.0.0.1:8080/web3.php')
	# print(cleanhtml(x.read().decode('utf-8')))
	print(cleanhtml(y.read().decode('utf-8')))

print(" %s seconds " % (time.time() - start_time))