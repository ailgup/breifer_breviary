import scrapy
from scrapy.http.request import Request
from datetime import datetime

class IbrevSpider(scrapy.Spider):
    name = 'ibrev'
    allowed_domains = ['ibreviary.com']
    start_urls = ['http://www.ibreviary.com/m2/breviario.php']
    date_object = datetime.strptime("03/14/2022", "%m/%d/%Y")
    
    def parse(self,response):
         #lang=en&giorno=14&mese=3&anno=2022&ok=ok
         
         my_data = self.date_object.strftime('lang=en&giorno=%d&mese=%m&anno=%Y&ok=ok')
         yield Request(self.start_urls[0],
                       method='POST', 
                       body=my_data, 
                       headers={'Content-Type': 'application/x-www-form-urlencoded'},
                       callback=self.parse_day)
         
    def parse_hour(self, hour):
        """
        parse_day gets basic info of day.

        :param hour: 0=OoR, 1=MP, 2=DP, 3=EP, 4=NP
        :return: describe what it returns
        """
        print("FF")
        hours_url_string = ["s=ufficio_delle_letture","s=lodi","s=ora_media","s=vespri","s=compieta"]
        hour_functions = ["parse_office","parse_lauds","parse_midday","parse_vespers","parse_compline"]
        self.date_object.strftime('lang=en&giorno=%d&mese=%m&anno=%Y&ok=ok')
        yield Request(self.start_urls[0]+hours_url_string[hour],
                       method='POST', 
                       body=my_data, 
                       headers={'Content-Type': 'application/x-www-form-urlencoded'},
                       callback=eval("self."+hour_functions[hour])
                       )

    def parse_office(self, response):
        print("PO")
        ant_one_sel = "//*[@id='contenuto']/div/p[5]/text()[1]"
        ant_two_sel = "//*[@id='contenuto']/div/p[5]/text()[49]"
        ant_three_sel = "//*[@id='contenuto']/div/p[5]/text()[73]"
        
        rand = "//*[@id='contenuto']/div/p[2]/span[1]"
        print(response.xpath(rand).get())
        print(response.xpath(ant_one_sel).get())
        print(response.xpath(ant_two_sel).get())
        print(response.xpath(ant_three_sel).get())
        
    def parse_day(self, response):
        """
        parse_day gets basic info of day.

        :return: describe what it returns
        """
        # Tuesday, 15 March 2022
        day_title_sel = "//*[@id='contenuto']/div/p[1]/text()"
        
        # Tuesday of the Second Week of Lent
        day_liturgical_title_sel = "//*[@id='contenuto']/div/p[2]/text()"
        
        # Tipo: Feriale - Tempo: Quaresima
        season_sel = "//*[@id='contenuto']/div/p[3]/text()"

        # ["Tipo: Feriale","Tempo: Quaresima"]
        day_type_season_delimiator = " - "
        
        # ["Tipo","Feriale"]
        type_text_delimiator = ": "
        
        day_types_it = ["Feriale","Festivo"]
        day_types_en = ["Of the Day","Feast"]
        
        season_it = ["Ordinario","Quaresima","Natale","Avvento","Pasqua"]
        season_en = ["Ordinary Time", "Lent", "Christmas", "Advent", "Easter"]
        
        day_title = response.xpath(day_title_sel).get()
        
        day_liturgical_title = response.xpath(day_liturgical_title_sel).get()
        
        unsplit_season = response.xpath(season_sel).get()
        
        season = unsplit_season.split(day_type_season_delimiator)[1]
        season = season.split(type_text_delimiator)[1]
        
        day_type = unsplit_season.split(day_type_season_delimiator)[0]
        day_type = day_type.split(type_text_delimiator)[1]
        
        
        print(day_title)
        print(day_liturgical_title)
        print(season + " ["+season_en[season_it.index(season)]+"]")
        print(day_type + " ["+day_types_en[day_types_it.index(day_type)]+"]")
         
        self.parse_hour(0)
        
        yield {"Day Title": day_title}
       
        