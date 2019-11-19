# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class GushiItem(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 时间
    pub_time = scrapy.Field()
    # 内容
    text = scrapy.Field()