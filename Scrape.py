from Hour import Breviary
from bs4 import BeautifulSoup
import requests
import psycopg2
from lxml import etree, html
import sys

class Breviary:
    DAYS = ["MON","TUE"]#,"WED","THU","FRI","SAT","SUN"]
    HOUR_ABBREVIATIONS = ["mp"]
class ScrapedElement:
    def __init__(self, name: str = "", xpath: str = "",split:str="",split_index:int=0,selector:str="",start:str="",end:str="",start_index:int=-1,end_index:int=-1):
        self.xpath = xpath
        self.value = ""
        self.name = name
        self.split=""
        self.split_index=split_index
        self.selector = selector
        self.start = start
        self.end = end
        self.start_index = start_index
        self.end_index = end_index

class Scrape:
    def __init__(self):
        self.conn = None

    def scrape_four_week(self):
        for self.week in range(1, 2):#5):  # weeks 1-4 inclusive
            for self.day in Breviary.DAYS:
                for self.hour in Breviary.HOUR_ABBREVIATIONS:
                    # http://www.liturgies.net/Liturgies/Catholic/loh/week5sundayor.htm
                    #url = "http://www.liturgies.net/Liturgies/Catholic/loh/week" + str(4 + self.week) + self.day.lower() + self.hour + ".htm"
                    url = "http://divineoffice.org/ord-w0"+str(self.week)+"-"+self.day.lower()+"-"+self.hour+"/?accessible=true"
                    print(url)
                    getattr(self, 'scrape_%s' % self.hour)(url)

    def scrape_or(self, url):

        elements = [#ScrapedElement(name="invitatory", xpath="/html/body/font/p[1]/text()[7]"),
                    ScrapedElement(name="antiphon_1",xpath="/html/body/font/p[6]/i/text()")]
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        dom = etree.HTML(str(soup))
        p=soup.find_all("b")
        #print(p.text())
        # thing = dom.xpath(e.xpath)[0]
        # if e.split:
        #     thing = thing.split(e.split)[e.split_index]
        # print("[" + str(self.week) + "," + self.day + "," + self.hour + "] (" + e.name + ") " + str( thing ))


    def scrape_mp_old(self, url):
        elements = [ScrapedElement(name="empty",selector = "//*[starts-with(.,'PSALMODY')]/following-sibling::*"),
                    ScrapedElement(name="antiphon_1",xpath="//p[contains(., 'Ant. 1')]/text()", selector = "//p[starts-with(.,'Ant. 1')]/following-sibling::p"),
                    ScrapedElement(name="psalm_1",xpath="//p[position()=3]/text()"),
                    ScrapedElement(name="antiphon_2",xpath="//p[contains(., 'Ant. 2') or contains(., 'Ant.2')]/text()"),
                    ScrapedElement(name="antiphon_3",xpath="//p[contains(., 'Ant. 3')]/text()")]
                    # //*[starts-with(.,'CANTICLE OF ZECHARIAH')]/following-sibling::p[starts-with(.,'Ant.') and position()=1]
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        cookies = {'iAmFromTheUSA': '1'}
        page = requests.get(url,headers=headers)
        #print(page.content)
        #soup = BeautifulSoup(page.content, 'html.parser')
        dom = html.fromstring(page.content)
        #dom = etree.HTML(str(soup))
        for e in elements:
            if e.xpath:
                print(dom.xpath(e.xpath))
            if e.selector != "":
                print(dom)
                dom = dom.xpath(e.selector)[0]
                print("\n\nAFTER")
                print(dom)
                
    def scrape_mp(self, url):
        elements = [ScrapedElement(name="empty",selector = "//*[starts-with(.,'PSALMODY')]/following-sibling::*"),
                    ScrapedElement(name="antiphon_1",xpath="//p[contains(., 'Ant. 1')]/text()", selector = "//p[starts-with(.,'Ant. 1')]/following-sibling::p"),
                    ScrapedElement(name="psalm_1",xpath="//p[position()=3]/text()"),
                    ScrapedElement(name="antiphon_2",xpath="//p[contains(., 'Ant. 2') or contains(., 'Ant.2')]/text()"),
                    ScrapedElement(name="antiphon_3",xpath="//p[contains(., 'Ant. 3')]/text()")]
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        cookies = {'iAmFromTheUSA': '1'}
        page = requests.get(url,headers=headers)
        #print(page.content)
        #soup = BeautifulSoup(page.content, 'html.parser')
        dom = html.fromstring(page.content)
        #dom = etree.HTML(str(soup))
        pieces = [ScrapedElement(name="ANT1",start_index=0,end_index = 1),
                  ScrapedElement(name="PS1",start_index=0,end = "Glory to the Father"),
                  ScrapedElement(name = "PS2",start_index=1, end = "Glory to the Father"),
                  ScrapedElement(name = "PS3",start_index=0, end = "Glory to the Father"),
                  ScrapedElement(name = "Reading_verse",start_index=3, end_index = 1),
                  ScrapedElement(name = "Reading",start_index=0, end_index = 1),
                  ScrapedElement(name = "RSP_1",start_index=2, end_index = 1),
                  ScrapedElement(name = "RSP_2",start_index=0, end_index = 1),
                  ScrapedElement(name = "RSP_3",start_index=0, end_index = 1),
                  ScrapedElement(name = "RSP_3",start_index=0, end_index = 1),
                  ScrapedElement(name = "INT_first",start_index=11, end_index=1),
                  ScrapedElement(name = "INT",start_index=0, end = "Our Father"),
                  ScrapedElement(name = "Prayer",start_index=1, end = "May the Lord")
                  ]
        current_piece = 0
        piece_index=0
        growing = False
        growing_piece = ""
        print(html.tostring(dom.xpath("//p[starts-with(.,'PSALMODY')]/following-sibling::p[28]")[0], with_tail=True))
        for index,e in enumerate(dom.xpath("//p[starts-with(.,'PSALMODY')]/following-sibling::p")):
            utf_string = html.tostring(e, with_tail=True).decode("utf-8")
            # print(utf_string+"\n\n")
            if(utf_string):
                if(not growing and (piece_index == pieces[current_piece].start_index or (pieces[current_piece].start in utf_string and pieces[current_piece].start != ""))): #second part of for failing b/c null condition is "" which is everywhere
                    growing_piece = growing_piece+ utf_string
                    growing = 1
                    piece_index = 1
                if (growing and (piece_index == pieces[current_piece].end_index or (pieces[current_piece].end in utf_string and pieces[current_piece].end != ""))):
                    #done
                    pieces[current_piece].value = growing_piece
                    print(pieces[current_piece].name,"  ",pieces[current_piece].value)
                    growing_piece=""
                    piece_index=0
                    growing = 0
                    current_piece = current_piece +1
                    
                    if current_piece == len(pieces):
                        return
                        
                elif growing and growing_piece != utf_string :
                    growing_piece = growing_piece + utf_string
                    piece_index = piece_index+1
                else:
                    piece_index = piece_index+1
                
            #print(index," ",html.tostring(e, with_tail=True))  
        
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
                password="Pa88w0rd")


        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


if __name__ == "__main__":
    s = Scrape()
    s.scrape_four_week()
