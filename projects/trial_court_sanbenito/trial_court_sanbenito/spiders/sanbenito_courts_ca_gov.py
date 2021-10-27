import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TrialCourtSanbenitoItem

class ImperialCourtsCaGovSpider(CrawlSpider):
    name = 'www.sanbenito.courts.ca.gov'
    allowed_domains = ['www.sanbenito.courts.ca.gov']
    start_urls = [
        'http://www.sanbenito.courts.ca.gov/'
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
        item = TrialCourtSanbenitoItem()
        item['url'] = response.url
        item['title'] = response.css('.hero .title::text').get().strip()
        item['body'] = response.css('.contentCenterWide').get().strip()
        item['parent'] = 'http://www.sanbenito.courts.ca.gov/' + response.css('.subMenu a:last-of-type::attr(href)').get().strip()
        yield item
