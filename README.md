# The-story
爬取故事网
项目说明：爬取http://www.xigushi.com上的所有故事
流程：首先获取一个故事，获取这个故事里的内容保存起来后，进行下一页的提取内容，存储到pymysql数据库中

一，创造项目：scrapy startproject gushi
二，创造爬虫：scrapy genspider gushi_spider xigushi.com
三，进入项目后：创造一个执行项目文件start.py
四，进行gushi_spider.py文件编写进行网页的解析
五，item
