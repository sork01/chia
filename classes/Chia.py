import re
import requests
from bs4 import BeautifulSoup

class Chia:
    
    mainLinks = []
    episodeLinks = []
    linktmp = ""
    
    def __init__(self):
        self.getMainPage()

    def getLatest(self):
        latest = requests.get("http://www.chia-anime.me")
        episodes = re.findall(r'(box2-top.+\n.+\n.+\n.+\n.+\n.+\n.+)', latest.text)
        lastrel = []
        for episode in episodes:
            show = []
            url = re.findall(r'a href="([^"]+)', episode)
            title = re.findall(r'title="([^"]+)', episode)
            pic = re.findall(r'src="([^"]+)', episode)
            if len(url) != 0:
                show.append(url[0])
            if len(title) != 0:
                show.append(title[0])
            if len(pic) != 0:
                show.append(pic[0])
            else:
                show.append("")
            lastrel.append(show)
        return lastrel
        

    
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
