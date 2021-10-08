import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TrialCourtPlacerItem

class ImperialCourtsCaGovSpider(CrawlSpider):
    name = 'www.placer.courts.ca.gov'
    allowed_domains = ['www.placer.courts.ca.gov']
    start_urls = [
        'http://www.placer.courts.ca.gov/'
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
        item = TrialCourtPlacerItem()
        item['url'] = response.url
        item['title'] = response.css('.hero .title::text').get().strip()
        item['body'] = response.css('.contentCenterWide').get().strip()
        item['parent'] = 'http://www.placer.courts.ca.gov/' + response.css('.subMenu a:last-of-type::attr(href)').get().strip()
        yield item
