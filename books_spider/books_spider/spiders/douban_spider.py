from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy import log
import re


class douban_spider(CrawlSpider):

    name = "douban"
    
    start_urls = ["http://book.douban.com/tag/"]

    allow_domain = "book.douban.com"

    rules = (
        Rule(SgmlLinkExtractor(allow=("/tag"))),
        Rule(SgmlLinkExtractor(allow=("subject/\d+/$")), callback='parse_page'),
        )

    def get_url_id(self, response):
        
        m = re.search("subject/(\d+)$", response.url)
        if m:
            return m.group(1)
        return None


    def parse_page(self, response):

        url_id = self.get_url_id(response)
        if url_id:
            open(os.path.join('douban/', url_id), 'w').write(response.body)
        
