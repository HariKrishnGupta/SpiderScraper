# -*- coding: utf-8 -*-

# Models for scraped items are defined here
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MuseumItem(scrapy.Item):
	museumNumber = scrapy.Field()
	producerName = scrapy.Field()
	description = scrapy.Field()
	schoolOrStyle = scrapy.Field()
	date = scrapy.Field()
	materials = scrapy.Field()
	technique = scrapy.Field()
	dimensions = scrapy.Field()
	curatorsComments = scrapy.Field()
	location = scrapy.Field()
	acquisitionDate = scrapy.Field()
	department = scrapy.Field()
	registrationNumber = scrapy.Field()
	imageLink = scrapy.Field()
	productionPlace = scrapy.Field()
	objectType = scrapy.Field()
	inscriptions = scrapy.Field()
	exhibitionHistory = scrapy.Field()
	associatedNames = scrapy.Field()
	acquisitionName = scrapy.Field()
	acquisitionNotes = scrapy.Field()
	bibliography = scrapy.Field()
	additonalIDs = scrapy.Field()
	subjects = scrapy.Field()
	findspot = scrapy.Field()
	cultureOrPeriod = scrapy.Field()



