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
        print ('filename.py -n number -w webpage name')
        sys.exit()

    for opt, arg in opts:
        if opt == '-h':
            print ('t2.py -n number -w webpage name')
            sys.exit()
        elif opt in ("-n", "--number"):
            n = int(arg)
            if len(opts) == 1:
                if len(sys.argv) > 3:
                    print("wrong Arguments for -n")
                else:
                    start_time = time.time()
                    for j in range(1,n):
                        x = urllib.request.urlopen('http://127.0.0.1:8080/helloworld.html')
                        print(cleanhtml(x.read().decode('utf-8')))
                    print(" %s seconds " % (time.time() - start_time))
                sys.exit()
        elif opt in ("-w", "--webpage"):
            w = arg
            if len(opts) == 1:
                if len(sys.argv) > 3:
                    print("wrong Arguments for -w")
                else:
                    start_time = time.time()
                    for l in range(1,10):
                        x = urllib.request.urlopen('http://127.0.0.1:8080/' + w)
                        print(cleanhtml(x.read().decode('utf-8')))
                    print(" %s seconds " % (time.time() - start_time))
                sys.exit()
    if len(sys.argv) == 5 or len(sys.argv) == 1:
        if len(opts) == 0:
                start_time = time.time()
                for i in range(1,10):
                    x = urllib.request.urlopen('http://127.0.0.1:8080/web.html')
                    print(cleanhtml(x.read().decode('utf-8')))
                print(" %s seconds " % (time.time() - start_time))                

        elif len(opts) == 2 :
            start_time = time.time()
            for i in range(1,n):
                x = urllib.request.urlopen('http://127.0.0.1:8080/'+ w)
                print(cleanhtml(x.read().decode('utf-8')))
            print(" %s seconds " % (time.time() - start_time))

    else:
        print("Wrong Arguments")

if __name__ == "__main__":
   main(sys.argv[1:])
   # print(len(sys.argv))









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