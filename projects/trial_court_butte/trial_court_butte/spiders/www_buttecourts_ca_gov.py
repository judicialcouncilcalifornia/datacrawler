import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TrialCourtButteItem

class WwwwButtecourtsCaGovSpider(CrawlSpider):
    name = 'www.buttecourt.ca.gov'
    allowed_domains = ['www.buttecourt.ca.gov']
    start_urls = [
        'https://www.buttecourt.ca.gov/',
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
        item = TrialCourtButteItem()
        item['url'] = response.url
        item['title'] = response.xpath('(//p[contains(concat(" ", normalize-space(@class), " "), " w3-text-deep-purple ")])[1]/text()').get().strip()
        item['body'] = response.css('.w3-container:nth-last-child(n+3)').get().strip()
        yield item
