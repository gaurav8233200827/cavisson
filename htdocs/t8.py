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






# import urllib
# # for x in range(1,10):
# url = "http://127.0.0.1/index.html"
# f = urllib.urlopen(url)
# print (f.read())


# txt = "C:\Apache24\htdocs\web1.html"
# txt_opn = open(txt)
# # print txt_opn.read()
# from urllib import urlopen

# url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"    
# html = urlopen(url).read()    
# raw = nltk.clean_html(html)

# f = open('web1.html')
# lines = f.readlines() 
# f.close()