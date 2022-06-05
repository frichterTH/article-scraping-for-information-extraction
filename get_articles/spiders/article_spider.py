import scrapy
from scrapy_requests import HtmlRequest
from get_articles.items import GetArticlesItem
from scrapy.loader import ItemLoader
import pandas as pd


class ArticleSpiderSpider(scrapy.Spider):
    name = 'article_spider'

    # reads the CSV file with the DOIs and converts it to a list
    df = pd.read_csv('D:/TH_Koeln/WS21-22/Bachelorarbeit/python_scripts/venv_scrapy-requests/cleaned_article_DOIs.csv')
    doi_list = df['doi'].tolist()

    start_urls = doi_list
    '''
    each DOI from the list, which is also a URL, is requested and waited for one second,
    before the 'parse_content' function is called, so that the JavaScript elements have time to load.
    '''
    def parse(self, response):
        yield HtmlRequest(url=response.url, callback=self.parse_content, render=True, options={'sleep': 1})

    # all found contents of the xpath selectors defined below are passed to the ItemLoader
    def parse_content(self, response):
        loader = ItemLoader(item = GetArticlesItem(), selector=response)

        loader.add_value('url', response.url)

        loader.add_xpath('title', "//h1[@class='item-meta-data__item-title']")

        # extracts abstracts from HTML documents of different structure
        loader.add_xpath('abstract', "//div[@class='articleSection article-abstract']/p")
        loader.add_xpath('abstract', "//div[@class='articleabstract']/div/div[@class='description']/p")

        loader.add_xpath('fulltext', "//div[@class='articleSection']/p")

        # extracts texts with multiple headings and paragraphs in full text
        loader.add_xpath('fulltext', "//div[@class='articleSection']/div/p") 
        
        yield loader.load_item()