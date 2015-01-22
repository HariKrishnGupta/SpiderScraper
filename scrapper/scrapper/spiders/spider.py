import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from scrapper.items import ScrapperItem
'''
class Spider(scrapy.Spider):
    name = "museum_spider"
    allowed_domains = ["britishmuseum.org"]
    start_urls = [
        "http://www.britishmuseum.org/research/collection_online/search.aspx?searchText=drawing"
    ]

    def parse(self, response):
	links = response.css('a::attr(href)').extract()
        for link in links:
		item = ScrapperItem()
		item['link'] = link
		yield item
'''
class Spider(CrawlSpider):
	name = "museum_spider"
	allowed_domains = ["britishmuseum.org"]
	start_urls = [
	"http://www.britishmuseum.org/research/collection_online/search.aspx?searchText=drawing"
	]
	rules = (Rule (SgmlLinkExtractor(allow=("&searchText=drawing&page=1",)), callback="parse_item", follow= True),)
#	rules = (Rule (SgmlLinkExtractor(allow=("&searchText=drawing&page=1","&searchText=drawing&page=2","&searchText=drawing&page=3",)), callback="parse_item", follow= True),)

	def parse_item(self, response):
		links = response.css('a::attr(href)').extract()
		for link in links:
			item = ScrapperItem()
			item['link'] = link
			yield item
