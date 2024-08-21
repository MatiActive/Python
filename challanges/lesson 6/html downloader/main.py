import os, sys
import urllib.parse
import validators # pip install validators
import requests
from datetime import datetime
print("number of arguments: ", len(sys.argv))
print("Arguments list: ", sys.argv)

url= "https://duckduckgo.com"
if len(sys.argv) > 1:
    url=sys.argv[1]

print("website to download: ", url)

scriptDir= os.path.dirname(__file__)
os.chdir(scriptDir)
print("current working dir", os.getcwd())

if not os.path.exists("./websites"):
    os.mkdir("websites")

parsedUrl = urllib.parse.urlparse(url)
print(parsedUrl)

validFlag = validators.url(url)
if validFlag:
    print("url:", url, "is valid")
else:
    print("url:", url, "is invalid")
    raise Exception("bad URL")

response = requests.get(url, allow_redirects=True)
if response.ok == True:
    print("response ok form server ", url)
    now = datetime.now()
    dateString = now.strftime("%d.%m.%Y  %H:%M:%S")
    print(dateString)

    fileName = "./websites/" + parsedUrl.netloc + " " + dateString + ".html"
    print(fileName)
    fh = open(fileName, "wb")
    fh.write(response.content)
    fh.close()