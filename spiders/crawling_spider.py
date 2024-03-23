from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = 'mycrawler'
    allowed_domains = ['leto.gg']
    start_urls = ['http://www.leto.gg/']

    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
    )

