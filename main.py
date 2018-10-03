from pydispatch import dispatcher
from scrapy import signals
from scrapy.crawler import CrawlerProcess

from poodlebot.spiders import pudelek_spider

items = []


def add_item(item):
	items.append(item)


dispatcher.connect(add_item, signal=signals.item_passed)

process = CrawlerProcess({
	'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(pudelek_spider.PudelekSpider)
process.start()
print("Found ", len(items), "items ")
