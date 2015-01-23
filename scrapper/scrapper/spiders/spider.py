import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from scrapper.items import ScrapperItem, MuseumItem
'''
class Spider(scrapy.Spider):
    name = "museum_spider"
    allowed_domains = ["britishmuseum.org"]
    start_urls = [
        "http://www.britishmuseum.org/research/collection_online/search.aspx?searchText=drawing"
    ]
ls

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
	"http://www.britishmuseum.org/research/collection_online/search.aspx?from=ad&fromDate=1700&object=22909"
	]
	rules = (Rule (SgmlLinkExtractor(allow=("&partId=1&from=ad&fromDate=1700&object=22909&page=1",)), callback="parse_item", follow= True),)
#	rules = (Rule (SgmlLinkExtractor(allow=("&searchText=drawing&page=1","&searchText=drawing&page=2","&searchText=drawing&page=3",)), callback="parse_item", follow= True),)

	def parse_item(self, response):
		
		museumNumber = " "
		if response.css(".objectDetails").xpath("//li[h3='Museum number']/p/text()").extract():
			museumNumber = response.css(".objectDetails").xpath("//li[h3='Museum number']/p/text()").extract()[0]

		producerName = " "
		if response.css(".objectDetails").xpath("//li[h3='Producer name']/ul/li/a/text()").extract():
			producerName = response.css(".objectDetails").xpath("//li[h3='Producer name']/ul/li/a/text()").extract()[0]

		description = " "
		if response.css(".objectDetails").xpath("//li[h3='Description']/p/text()").extract():
			description = response.css(".objectDetails").xpath("//li[h3='Description']/p/text()").extract()[0]

		schoolOrStyle = " "
		if response.css(".objectDetails").xpath("//li[h3='School/Style']/ul/li/a/text()").extract():
			schoolOrStyle = response.css(".objectDetails").xpath("//li[h3='School/Style']/ul/li/a/text()").extract()[0]

		date = " "
		if response.css(".objectDetails").xpath("//li[h3='Date']/ul/li/text()").extract():
			date = response.css(".objectDetails").xpath("//li[h3='Date']/ul/li/text()").extract()[0]

		materials = " "
		if response.css(".objectDetails").xpath("//li[h3='Materials']/ul/li/a/text()").extract():
			materials = response.css(".objectDetails").xpath("//li[h3='Materials']/ul/li/a/text()").extract()[0]
		
		technique = " "
		if response.css(".objectDetails").xpath("//li[h3='Technique']/ul/li/a/text()").extract():
			technique = response.css(".objectDetails").xpath("//li[h3='Technique']/ul/li/a/text()").extract()[0]
		
		height = " "
		if response.css(".objectDetails").xpath("//li[h3='Dimensions']/ul/li[1]/text()").extract():
			height = response.css(".objectDetails").xpath("//li[h3='Dimensions']/ul/li[1]/text()").extract()[0]
		
		width = " "
		if response.css(".objectDetails").xpath("//li[h3='Dimensions']/ul/li[2]/text()").extract():
			width = response.css(".objectDetails").xpath("//li[h3='Dimensions']/ul/li[2]/text()").extract()[0]

		curatorsComments = " "
		if response.css(".objectDetails").xpath("//li[h3='Curator&apos;s comments']/p/text()").extract():
			curatorsComments = response.css(".objectDetails").xpath("//li[h3='Curator&apos;s comments']/p/text()").extract()[0]

		location = " "
		if response.css(".objectDetails").xpath("//li[h3='Location']/p/text()").extract():
			location = response.css(".objectDetails").xpath("//li[h3='Location']/p/text()").extract()[0]		
		
		acquisitionDate = " "
		if response.css(".objectDetails").xpath("//li[h3='Acquisition date']/p/text()").extract():
			acquisitionDate = response.css(".objectDetails").xpath("//li[h3='Acquisition date']/p/text()").extract()[0]

		department = " "
		if response.css(".objectDetails").xpath("//li[h3='Department']/p/text()").extract():
			department = response.css(".objectDetails").xpath("//li[h3='Department']/p/text()").extract()[0]

		registrationNumber = " "
		if response.css(".objectDetails").xpath("//li[h3='Registration number']/p/text()").extract():
			registrationNumber = response.css(".objectDetails").xpath("//li[h3='Registration number']/p/text()").extract()[0]

		item = MuseumItem()
		item['museumNumber'] = museumNumber
		item['producerName'] = producerName
		item['description'] = description
		item['schoolOrStyle'] = schoolOrStyle
		item['date'] = date
		item['materials'] = materials
		item['technique'] = technique
		item['height'] = height
		item['width'] = width
		item['curatorsComments'] = curatorsComments
		item['location'] = location
		item['acquisitionDate'] = acquisitionDate
		item['department'] = department
		item['registrationNumber'] = registrationNumber
		yield item

