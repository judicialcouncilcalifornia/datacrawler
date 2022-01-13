# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, Identity
from w3lib.html import remove_tags
from .utils.processors import Text, Number, Price, Date, Url, Image


class TrialCourtMercedItem(scrapy.Item):
    url = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    body = scrapy.Field()
    parent = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
