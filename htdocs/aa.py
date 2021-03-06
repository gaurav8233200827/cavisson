import urllib.request
import re
import time
import sys, getopt


def cleanhtml(raw_html):
  c = re.compile('<.*?>')
  ct = re.sub(c, '', raw_html)
  return ct

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hn:w:")
	except getopt.GetoptError:
		print ('t2.py -n number -w webpage name') #,["number=","webpage="]
		sys.exit()

	for opt, arg in opts:
		if opt == '-h':
			print ('t2.py -n number -w webpage name')
			sys.exit()
		elif opt in ("-n", "--number"):
			n = int(arg)
		elif opt in ("-w", "--webpage"):
			w = arg

	if len(opts) != 2:
		start_time = time.time()
		for i in range(1,10):
			x = urllib.request.urlopen('http://127.0.0.1:8080/web.html')
			print(cleanhtml(x.read().decode('utf-8')))
		print(" %s seconds " % (time.time() - start_time))
		sys.exit()

	start_time = time.time()
	for i in range(1,n):
		x = urllib.request.urlopen('http://127.0.0.1:8080/'+ w)
		# y = urllib.request.urlopen('http://127.0.0.1:8080/web3.php')
		print(cleanhtml(x.read().decode('utf-8')))
		# print(cleanhtml(y.read().decode('utf-8')))

	print(" %s seconds " % (time.time() - start_time))

if __name__ == "__main__":
   main(sys.argv[1:])









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