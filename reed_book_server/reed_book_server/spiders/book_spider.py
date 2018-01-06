from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from reed_book_server.items import ReedBookServerItem


class BookSpider(CrawlSpider):
    name = "biqu.la"
    start_urls = ['https://www.biqu.la/book/']

    rules = (
        Rule(LinkExtractor(allow=('/book/0-default'))),
        Rule(LinkExtractor(allow=('/book/[A-Z]'), deny=('/author')), callback='parse_item'),
    )

    def parse_item(self, response):
        item = ReedBookServerItem()
        item['book_name'] = response.xpath("//div[@id='info']//h1/text()").extract()[0]
        item['book_sites'] = {}
        item['book_sites']['笔趣阁'] = response.url
        return item
