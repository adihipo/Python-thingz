# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['greenfoxacademy.com/']
    start_urls = ['https://www.greenfoxacademy.com/']

    def parse(self, response):
        quotes = response.xpath("//p").extract()
        yield {'quotes': quotes}