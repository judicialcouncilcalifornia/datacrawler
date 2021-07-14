import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TrialCourtFresnoItem


class WwwFresnoCourtsCaGovSpider(CrawlSpider):
    name = 'www.fresno.courts.ca.gov'
    allowed_domains = ['www.fresno.courts.ca.gov']
    start_urls = [
        'http://www.fresno.courts.ca.gov/',
        'http://www.fresno.courts.ca.gov/case_info/'
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
        item = TrialCourtFresnoItem()
        item['url'] = response.url
        item['title'] = response.css('h1::text').get().strip()
        item['body'] = '<table><tr>' + response.xpath("/html/body/table/tr/td[2]/table[4]/tr[3]/td[2]").get().strip() + '</tr></table>'
        item['parent'] = 'http://www.fresno.courts.ca.gov' + response.css('a.breadcrumb:nth-last-child(2)::attr(href)').get().strip()
        yield item
