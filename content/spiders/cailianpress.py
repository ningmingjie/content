# -*- coding: utf-8 -*-
import scrapy


class CailianpressSpider(scrapy.Spider):
    name = 'cailianpress'
    allowed_domains = ['www.cailianpress.com']
    start_urls = ['http://www.cailianpress.com/']

    def parse(self, response):
        pass
