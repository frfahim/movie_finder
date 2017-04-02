# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class MovieFinderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    year = Field()
    likes = Field()
    rottenTomatoes_critics = Field()
    rottenTomatoes_audience = Field()
    imdb = Field()
    download_link_3d = Field()
    download_link_720p = Field()
    download_link_1080p = Field()
