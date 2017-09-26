import urllib.request
import re
import time
import sys, getopt


def cleanhtml(raw_html):
  c = re.compile('<.*?>')
  ct = re.sub(c, '', raw_html)
  return ct

def main(argv):
    global w
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
            print("in xyz" + str(opt))
            n = int(arg)
        elif opt in ("-w", "--webpage"):
            w = arg

    if len(opts) == 0:
        print(len(opts))
        start_time = time.time()
        for i in range(1,10):
            x = urllib.request.urlopen('http://127.0.0.1:8080/web.html')
            print(cleanhtml(x.read().decode('utf-8')))
        print(" %s seconds " % (time.time() - start_time))



    elif len(opts) == 1:
        print("in if")
        for opt, arg in opts:
            print("in for" + str(opt))
            if opt in ("-n", "--number"):
                print("in -n if")
                start_time = time.time()
                for j in range(1,int(arg)):
                    x = urllib.request.urlopen('http://127.0.0.1:8080/helloworld.html')
                    print(cleanhtml(x.read().decode('utf-8')))
                print(" %s seconds " % (time.time() - start_time))
            elif opt in ("-w", "--webpage"):
                print("in -w if")
                start_time = time.time()
                for l in range(1,10):
                    x = urllib.request.urlopen('http://127.0.0.1:8080/' + str(arg))
                    print(cleanhtml(x.read().decode('utf-8')))
                print(" %s seconds " % (time.time() - start_time))
                sys.exit()

    elif len(opts) == 2:
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