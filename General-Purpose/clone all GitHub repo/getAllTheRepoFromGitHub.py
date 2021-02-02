from bs4 import BeautifulSoup
import requests
from time import sleep
import re
from os import system

gitWebsite, ext = "https://github.com/", ".git"
userName = input("Enter your username for GitHub: ")
r = None

while True:
    r = requests.get("%s%s%s" % (gitWebsite, userName, "?tab=repositories"))
    if r.status_code == 200:
        break
    sleep(1)

soup = BeautifulSoup(r.text, features = "lxml")
ls = soup.findAll('a', attrs={'href': re.compile("^/%s/" % (userName))})

links = [i.get('href') for i in ls]

for link in links:
    link = link.split('/')
    if len(link) == 3:
        link.pop(0)
        system("git clone %s%s%s" % (gitWebsite, "/".join(link), ext))