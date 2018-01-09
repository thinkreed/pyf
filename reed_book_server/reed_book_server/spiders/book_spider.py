from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from reed_book_server.items import ReedBookServerItem
from scrapy import Selector


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


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
        item['author_name'] = response.xpath("//span[@class='item item']//a/text()").extract()[0]
        item['book_sites'] = {}
        item['book_sites']['name'] = '笔趣阁'
        item['book_sites']['chapters'] = []
        i = 0
        for a_tag in [item for chunk in chunker(response.xpath("//div[@class='book_list']//ul//li//a").extract(), 4) for
                      item in chunk]:
            a_selector = Selector(text=a_tag)
            chapter = {}
            chapter['index'] = i
            chapter['url'] = response.url + a_selector.xpath("//a/@href").extract_first()
            chapter['title'] = a_selector.xpath("//a//text()").extract_first()
            item['book_sites']['chapters'].append(chapter)
            i += 1

        return item
