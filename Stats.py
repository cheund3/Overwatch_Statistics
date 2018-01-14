# Dylan Cheung
from bs4 import BeautifulSoup
import requests
from Player import Player


class Stats:

    def __init__(self):
        self.data = []


    def printInfo(self):
        sorted = self.data
        sorted.sort(key=lambda x: x.sr , reverse=True)
        count = 1
        for i in sorted:
            if count == 1:
                print ("=" * 50)
            print ("#"+str(count))
            print i
            print ("=" * 50)
            count += 1


    def add(self, username, ConsoleXbox):
        url = "overwatchtracker.com/profile/" + ConsoleXbox + "/global/" + username
        r = requests.get("http://" + url)
        data = r.text
        soup = BeautifulSoup(data)

        info = []
        for div in soup.find_all('div', class_="player-info"):
            for div2 in div.find_all('span', class_="name"):
                info.append(div2.string)
        for div in soup.find_all('div', class_="infobox-container"):
            for div2 in div.find_all('div', class_="infobox"):
                for div3 in div2.find_all('span', class_="value"):
                    if div3.string is not None:
                        info.append(div3.string)
        self.data.append(Player(info[0], info[1], info[2], info[3], info[4]))
