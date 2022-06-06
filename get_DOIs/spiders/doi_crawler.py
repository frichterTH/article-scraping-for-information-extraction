import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DoiCrawlerSpider(CrawlSpider):
    name = 'doi_crawler'
    allowed_domains = ['www.microbiologyresearch.org']
    start_urls = ['https://www.microbiologyresearch.org/content/journal/ijsem/browse']

    # stores all the links found in the xpath selectors mentioned below
    volume_links = LinkExtractor(restrict_xpaths="//h3[@class='h5']/a")
    issue_links = LinkExtractor(restrict_xpaths="//ul[@class='togglecontent list-unstyled volume-issue-list']/li[@class='issue']/a")
    page_links = LinkExtractor(restrict_xpaths="//div[@class='paginator pull-left']/a")

    # sets rules for how the saved links are used
    rules = (
        Rule(volume_links, follow=True),                            # these links are followed only
        Rule(issue_links, callback='parse_item', follow=True),      # for the other two Rules the links were followed
        Rule(page_links, callback='parse_item', follow=True)        # and then the function 'parse_item' called
    )

    # extracts all links found under defined the CSS selector.
    def parse_item(self, response):
        yield {
            'doi': response.css('div.articleSourceTag a::attr(href)').getall()
                }
