import scrapy
from scrapy.http.request import Request

class IbrevSpider(scrapy.Spider):
    name = 'ibrev'
    allowed_domains = ['ibreviary.com']
    start_urls = ['http://www.ibreviary.com/m2/breviario.php']

    def parse(self,response):
         #lang=en&giorno=14&mese=3&anno=2022&ok=ok
         my_data = 'lang=en&giorno=15&mese=3&anno=2022&ok=ok'
         yield Request(self.start_urls[0],
                       method='POST', 
                       body=my_data, 
                       headers={'Content-Type': 'application/x-www-form-urlencoded'},
                       callback=self.parse_day)
         
    def parse_day(self, response):
        day_title_sel = "//div[@id='contenuto']/div[@class='inner']/p[2]"
        day_title = response.xpath(day_title_sel).get()
        yield {"Day Title": day_title}
        print(day_title)
        