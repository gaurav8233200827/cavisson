import urllib.request

link = "http://www.google.com"
f = urllib.request(link)

print (f.text)