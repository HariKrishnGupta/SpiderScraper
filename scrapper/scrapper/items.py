# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapperItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()l
	link = scrapy.Field()

class MuseumItem(scrapy.Item):
	museumNumber = scrapy.Field()
	producerName = scrapy.Field()
	description = scrapy.Field()
	schoolOrStyle = scrapy.Field()
	date = scrapy.Field()
	materials = scrapy.Field()
	technique = scrapy.Field()
	height = scrapy.Field()
	width = scrapy.Field()
	curatorsComments = scrapy.Field()
	location = scrapy.Field()
	acquisitionDate = scrapy.Field()
	department = scrapy.Field()
	registrationNumber = scrapy.Field()
