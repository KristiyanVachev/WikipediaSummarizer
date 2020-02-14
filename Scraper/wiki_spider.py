from scrapy import Spider
from scrapy.selector import Selector
import html2text

class WikiSpider(Spider):
    name = "wiki_spider"
    allowed_domains = ["www.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/koala"]

    def parse(self, response):
        hxs = Selector(response)
        sample = hxs.select("//div[@id='mw-content-text']/p[1]").extract()[0]

        converter = html2text.HTML2Text()
        converter.ignore_links = True
        print(converter.handle(sample)) #Python 3 print syntax
