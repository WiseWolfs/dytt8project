# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from dytt8project.items import Dytt8ProjectItem


class Dytt8CrawlerSpider(CrawlSpider):
    name = 'dytt8_crawler'
    allowed_domains = ['ygdy8.net']
    start_urls = ['http://www.ygdy8.net/html/gndy/dyzz/list_23_2.html']

    rules = (
        Rule(LinkExtractor(allow=r'list_23_[1-168].html')),
        Rule(LinkExtractor(allow=r'html/gndy/dyzz/*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
       # movies = response.xpath('//div[@class="co_area2"]')
        movies = response.xpath('//div[@id="Zoom"]')
        print "movies",movies
        for movie in movies:
            item = Dytt8ProjectItem()
        #    item['name'] = movie.xpath('div[@class="title_all"]/h1/font/text()')
            item['tname'] = movie.xpath('td/p[1]/text()[1]').extract() #翻译名
            item['oname'] = movie.xpath('td/p[1]/text()[2]').extract() #原名
            item['year'] = movie.xpath('td/p[1]/text()[3]').extract() #年代
            item['country'] = movie.xpath('td/p[1]/text()[4]').extract() #国家
            item['category'] = movie.xpath('td/p[1]/text()[5]').extract() #类别
            item['language'] = movie.xpath('td/p[1]/text()[6]').extract() #语言
            item['word'] = movie.xpath('td/p[1]/text()[7]').extract() #字幕
            item['idb'] = movie.xpath('td/p[1]/text()[8]').extract()
            item['url'] = movie.xpath('td/table/tbody/tr/td/a/text()').extract()

            print "item[cname]",item['tname']
            yield item
