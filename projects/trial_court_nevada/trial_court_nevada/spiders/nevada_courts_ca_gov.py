import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TrialCourtNevadaItem

class NevadaCourtsCaGovSpider(CrawlSpider):
    name = 'nccourt.net'
    allowed_domains = ['nccourt.net']
    start_urls = [
        'http://nccourt.net/'
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
        item = TrialCourtNevadaItem()
        item['url'] = response.url
        item['title'] = response.css('.hero .title::text, .hero4 .title::text').get().strip()
        item['body'] = response.css('.contentCenterWide,.contentCenterWrap .contentCenter,.contentCenterWrap .contentColumn').get().strip()
        item['parent'] = 'http://nccourt.net/' + response.css('.subMenu a:last-of-type::attr(href)').get().strip()
        yield item
