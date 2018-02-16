import requests
import urllib.request
from bs4 import BeautifulSoup

#URL = "http://www.espncricinfo.com/"
#URL = "http://www.espncricinfo.com/series/18065/game/1122277/ind-in-sa-2017-18/"
URL = "http://www.cricbuzz.com/"
page  = requests.get(URL)
soup = BeautifulSoup(page.content,'html.parser')
#print(soup.find('a',class_="contentItem__header__wrapper"))
print(soup.prettify())
urllib.request.urlretrieve("https://wallpapercave.com/wp/SmJpcB0.jpg", "local-filename.jpg")
