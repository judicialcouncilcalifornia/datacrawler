import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TrialCourtMercedItem

class MercedCourtsCaGovSpider(CrawlSpider):
    name = 'www.mercedcourt.org'
    allowed_domains = ['www.mercedcourt.org']
    start_urls = [
        'https://www.mercedcourt.org/'
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
        item = TrialCourtMercedItem()
        item['url'] = response.url
        item['title'] = response.css('.hero .title::text').get().strip()
        item['body'] = response.css('.contentCenterWide').get().strip()
        item['parent'] = 'https://www.mercedcourt.org/' + response.css('.subMenu a:last-of-type::attr(href)').get().strip()
        yield item
