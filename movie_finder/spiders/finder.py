# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from movie_finder.items import MovieFinderItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join

import datetime
import socket


class FinderSpider(CrawlSpider):
    name = 'finder'
    allowed_domains = ['yts.ag']
    start_urls = ['https://yts.ag/browse-movies/0/1080p/biography/8/latest']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=
            '//*[@class="tsc_pagination tsc_paginationA tsc_paginationA06"]//li//a'),follow=True),
        Rule(LinkExtractor(restrict_xpaths='//*[@class="browse-movie-link"]'),
            callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # Create a loader using the response
        l = ItemLoader(item = MovieFinderItem(), response = response)

        # load fields using Xpath expression
        # Get the movie name
        l.add_xpath('name', '//*[@class="hidden-xs"]//h1/text()')
        m_year = response.xpath('//*[@class="hidden-xs"]//h2/text()')
        # Movie release year, index 0 to take only movie name
        l.add_value('year', m_year[0].extract())
        l.add_xpath('likes', '//*[@class="bottom-info"]//div[1]//span//text()')
        rt1 = response.xpath('//*[@class="bottom-info"]//div[2]//span//text()')
        # Rotten Tomatoyes Critics rating
        l.add_value('rottenTomatoes_critics', rt1[0].extract())
        rt2 = response.xpath('//*[@class="bottom-info"]//div[3]//span//text()')
        # Rotten Tomatoyes Audience rating
        l.add_value('rottenTomatoes_audience', rt2[0].extract())
        im = response.xpath('//*[@class="bottom-info"]//div[4]//span//text()')
        # IMDB rating
        l.add_value('imdb', im[0].extract())
        # Get a list of download link of different quality
        lt = response.xpath('//*[@class="hidden-xs hidden-sm"]//a//@href')
        if len(lt) is 3:
            l.add_value('download_link_3d', lt[0].extract())
            l.add_value('download_link_720p', lt[1].extract())
            l.add_value('download_link_1080p', lt[2].extract())
        else:
            l.add_value('download_link_720p', lt[0].extract())
            l.add_value('download_link_1080p', lt[1].extract())
        return l.load_item()
