from Hour import Breviary
from bs4 import BeautifulSoup
import requests
import psycopg2
from lxml import etree
import sys


class ScrapedElement:
    def __init__(self, name: str = "", xpath: str = "",split:str="",split_index:int=0):
        self.xpath = xpath
        self.value = ""
        self.name = name
        self.split=""
        self.split_index=split_index

class Scrape:
    def __init__(self):
        self.conn = None

    def scrape_four_week(self):
        for self.week in range(1, 5):  # weeks 1-4 inclusive
            for self.day in Breviary.DAYS:
                for self.hour in Breviary.HOUR_ABBREVIATIONS:
                    # http://www.liturgies.net/Liturgies/Catholic/loh/week5sundayor.htm
                    url = "http://www.liturgies.net/Liturgies/Catholic/loh/week" + str(
                        4 + self.week) + self.day.lower() + self.hour + ".htm"

                    getattr(self, 'scrape_%s' % self.hour)(url)

    def scrape_or(self, url):

        elements = [#ScrapedElement(name="invitatory", xpath="/html/body/font/p[1]/text()[7]"),
                    ScrapedElement(name="antiphon_1",xpath="/html/body/font/p[6]/i/text()")]
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        dom = etree.HTML(str(soup))
        p=soup.find_all("b")
        print(p.text())
        # thing = dom.xpath(e.xpath)[0]
        # if e.split:
        #     thing = thing.split(e.split)[e.split_index]
        # print("[" + str(self.week) + "," + self.day + "," + self.hour + "] (" + e.name + ") " + str( thing ))

    def scrape_mp(self, url):
        pass

    def scrape_dp(self, url):
        pass

    def scrape_ep(self, url):
        pass

    def scrape_np(self, url):
        pass

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host="localhost",
                database="postgres",
                user="postgres",
                password="postgres")


        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


if __name__ == "__main__":
    s = Scrape()
    s.scrape_four_week()
