# -*- coding: utf-8 -*-
import scrapy
from gushi.items import GushiItem

class GushiSpiderSpider(scrapy.Spider):
    name = 'gushi_spider'
    allowed_domains = ['xigushi.com']
    start_urls = ['http://www.xigushi.com/ymgs/14077.html']

    def parse(self, response):
        # print(response.text)
        names = response.xpath("//div[@class='index']")
        for name in names:
            title = response.xpath(".//div[@class='by']//dd/h1/text()").extract()[0]
            # pub_time = response.xpath('.//div[@class="by"]//dd/div/text()').extract()[0]
            text = response.xpath(".//div[@class='by']//dd/p").extract()
            item = GushiItem()
            item["title"] = title
            # item["pub_time"] = pub_time
            item["text"] = text
            yield item
        next = response.xpath("//div[@class='pages']//ul/li[2]/a/@href").extract()[0]
        url = response.urljoin(next)
        yield scrapy.Request(url=url,callback=self.parse)





