# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags, replace_escape_chars

# defines the fields for the item and how the output should look like
class GetArticlesItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field(input_processor = MapCompose(remove_tags, replace_escape_chars), output_processor = TakeFirst())
    abstract = scrapy.Field(input_processor = MapCompose(remove_tags, replace_escape_chars))
    fulltext = scrapy.Field(input_processor = MapCompose(remove_tags, replace_escape_chars))