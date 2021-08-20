import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TrialCourtImperialItem

class ImperialCourtsCaGovSpider(CrawlSpider):
    name = 'imperial.courts.ca.gov'
    allowed_domains = ['imperial.courts.ca.gov']
    start_urls = [
        'https://imperial.courts.ca.gov/',
        'https://imperial.courts.ca.gov/ContactUsV4/ContactUs',
        'https://imperial.courts.ca.gov/ReservationSystem/',
        'https://imperial.courts.ca.gov',
        'https://imperial.courts.ca.gov/AccessCenter/DownloadForms.aspx',
        'https://imperial.courts.ca.gov/Interim/TemporaryJudge.html',
        'http://www.imperial.courts.ca.gov/CourtCalendars/',
        'https://imperial.courts.ca.gov/Traffic.htm',
        'https://imperial.courts.ca.gov/Covid19GeneralOrders.htm',
        'https://imperial.courts.ca.gov/',
        'https://imperial.courts.ca.gov/ADA.htm',
        'https://imperial.courts.ca.gov/CourtCalendars/',
        'https://imperial.courts.ca.gov/LawLibrary/',
        'https://imperial.courts.ca.gov/Court-Holidays.htm',
        'https://imperial.courts.ca.gov/PressRelease.htm',
        'https://imperial.courts.ca.gov/Judicial-Officers.htm',
        'https://imperial.courts.ca.gov/ProbateDocs/ProbateNotes4.aspx',
        'https://imperial.courts.ca.gov/AccessCenter.htm',
        'https://imperial.courts.ca.gov/AccessCenter/FLWorkshop.aspx',
        'https://imperial.courts.ca.gov/RestoreCourtServices.htm',
        'https://imperial.courts.ca.gov/CourtDocumentsVB/SCourtDocuments.aspx',
        'https://imperial.courts.ca.gov/Covid19LocalRules.htm',
        'https://imperial.courts.ca.gov/Index.htm',
        'https://imperial.courts.ca.gov/ACHotDocs.htm',
        'https://imperial.courts.ca.gov/Juror.htm',
        'https://imperial.courts.ca.gov/WebCaseAlert/Registration.aspx',
        'https://imperial.courts.ca.gov/iJuror/login.asp',
        'https://imperial.courts.ca.gov/Hr.htm'
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
        item = TrialCourtImperialItem()
        item['url'] = response.url
        item['title'] = response.css('header span::text').get().strip()
        item['body'] = response.css('article > *').get().strip()
        yield item
