# The-story
爬取故事网
第一次上传自己的项目，练练手

项目说明：爬取http://www.xigushi.com上的所有故事
流程：首先获取一个故事，获取这个故事里的内容保存起来后，进行下一页的提取内容，存储到pymysql数据库中

一，创造项目：scrapy startproject gushi



二，创造爬虫：scrapy genspider gushi_spider xigushi.com



三，进入项目后：创造一个执行项目文件start.py



四，item编写 用来存储你说需要的内容


五，进行gushi_spider.py文件编写进行网页的解析


六、pipelines.py编写 进行异步存储到mysql数据库中，


七、settings.py编写 需要打开
ROBOTSTXT_OBEY = False
# 设置请求头
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}
# 打开pipeline
ITEM_PIPELINES = {
   'gushi.pipelines.GushiPipeline': 300,
}
# 设置数据库的一些参数
HOST = 'localhost'
USER = 'root'
PASSWORD = 'password'
DB = 'jianshu'
