# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class Dytt8ProjectItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tname = Field() #翻译名称
    oname = Field() #原名
    year = Field() #年代
    country = Field() #国家
    category = Field() #类别
    language = Field() # 语言
    word = Field() #字幕
    url = Field()#下载地址
    idb = Field() #豆瓣评分

    



