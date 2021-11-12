import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TrialCourtRiversideItem

class ImperialCourtsCaGovSpider(CrawlSpider):
    name = 'www.riverside.courts.ca.gov'
    allowed_domains = ['www.riverside.courts.ca.gov']
    start_urls = [
        'http://www.riverside.courts.ca.gov/'
    ]

    rules = [
        Rule(
            LinkExtractor(
                allow=('.*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]

    def parse_item(self, response):
        item = TrialCourtRiversideItem()
        item['url'] = response.url
        item['title'] = response.css('.page-heading::text').get().strip()
        item['body'] = response.css('.basic-page').get().strip()
        item['parent'] = 'http://www.riverside.courts.ca.gov/' + response.css('.nav-link a:last-of-type::attr(href)').get().strip()
        yield item
