import re
import requests
from bs4 import BeautifulSoup

class Chia:
    
    mainLinks = []
    episodeLinks = []
    linktmp = ""
    
    def __init__(self):
        self.getMainPage()

    
    def getMainPage(self):
        main = requests.get("http://www.chia-anime.me/index/")
        soup = BeautifulSoup(main.text.encode('utf-8'), 'html.parser')
        div = soup.find_all('li')
        
        for i in div:
            links = i.find_all('a')
            for link in links:
                if self.linktmp[:1].lower() != link.get_text()[:1].lower():
                    res = ("<a id=\"" + link.get_text()[:1] + "\"</a>")
                    self.mainLinks.append(res)
                    res = ("<br> <br>" + link.get_text()[:1] + "<br> <br>")
                    print(res)
                    self.mainLinks.append(res)

                res = (link['href'], link.get_text())
                self.linktmp = link.get_text()
                    # print(link['href'], link.get_text().encode('utf-8'))
                self.mainLinks.append(res)

    def getEpisodes(self, show):
        html = requests.get(show)
        soup = BeautifulSoup(html.text.encode('utf-8'), 'html.parser')
        div = soup.find_all('h3')
        res = []
        for i in div:
            links = i.find_all('a')
            for link in links:
                res.append((link['href'], link.get_text()))
        return res
        
    def getLink(self, episode):
        html = requests.get(episode)
        soup = BeautifulSoup(html.text.encode('utf-8'), 'html.parser')
        div = soup.find_all('div', {'class', 'play-video selected'})
        for link in div:
            video = re.findall(r'src="([^"]+)', str(link))
        return video            
    
#chia = Chia()
#print(chia.getLink("http://www.chia-anime.me/11eyes-episode-10-english-subbed/"))
