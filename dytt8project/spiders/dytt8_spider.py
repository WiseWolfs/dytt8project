from scrapy import Spider
from scrapy.selector import Selector
from dytt8project.items import Dytt8ProjectItem

class Dytt8Spider(Spider):
    name = "dytt8"
    allowed_domains = ["ygdy8.net"]
    start_urls = [
        "http://www.ygdy8.net/html/gndy/dyzz/list_23_2.html"
    ]
    def parse(self,response):
        movies = Selector(response).xpath('//table[@class="tbspan"]')
        print "movies: ",movies
        for movie in movies :
            item = Dytt8ProjectItem()
            item['name'] = movie.xpath('tr[2]/td[2]/b/a/text()').extract()[0]
            item['desc'] = movie.xpath('tr[4]/td/text()').extract()[0]
            yield item



