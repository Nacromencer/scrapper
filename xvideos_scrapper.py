from bs4 import BeautifulSoup
import requests
import re
import csv
import time
dict_ = {}
for j in range(1,101):
    url = "http://www.xvideos.es/new/{}".format(j)
    print(url)
    data = requests.get(url)
    soup = BeautifulSoup(data.text)
    for i in soup.find_all("div",{"id":re.compile("video_[0-9]*")}):
        dict_[i.p.a.text] = {'img':i.find("img")['data-src'], 'link':"https://www.xvideos.es/embedframe/"+re.findall("video([0-9]+)/",i.a['href'])[0], "time":(i.find("span",{"class":"duration"}).text)}
    time.sleep(3)

d = []
for i in dict_:
    d.append([i, dict_[i]['link'], dict_[i]['img'], dict_[i]['time']])

s = []
for k in d:
    s.append([k[0].encode('utf8'), k[1].encode('utf8'), k[2].encode('utf8'), k[3].encode('utf8')])

with open("new.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(s)