# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy import log
from bs4 import BeautifulSoup
import re
import os
import json


class douban_spider(CrawlSpider):

    name = "douban"
    start_urls = ["http://book.douban.com/tag/"]

    allow_domain = "book.douban.com"

    proxy_list = []

    rules = (
        Rule(SgmlLinkExtractor(allow=("/tag"))),
        Rule(SgmlLinkExtractor(allow=("subject/\d+/$")),
            callback='parse_page'),
        )

    def __init__(self):
        
        CrawlSpider.__init__(self)
        self.proxy_list = [x.strip() for x in open('books_spider/proxy.list').readlines()]

    def get_url_id(self, response):
        m = re.search("subject/(\d+)/$", response.url)
        if m:
            return m.group(1)
        return None

    def generate_item(self, response):
        
        item = {}
        item['ref_ids'] = response.url

        soup = BeautifulSoup(response.body)
        item['name'] = soup.find('title').get_text().replace(u' (豆瓣)', '')

        info = list(soup.find('div', id="info").stripped_strings)

        last_text = ''
        for text in info:
            print last_text
            if last_text == u"原作名:":
                item['original_title'] = text
            elif last_text == u'出版社:':
                item['press'] = text
            elif last_text == u'页数:':
                item['page_nums'] = text
            elif last_text == u'定价:':
                item['price'] = text
            elif last_text == u'出版年:':
                item['publication'] = text
            elif last_text == u'ISBN:':
                item['isbn'] = text
            last_text = text

        
        try:
            item['authors'] = [x.get_text() for x in soup.find('span', class_='pl', text=re.compile(u'作者')).parent.find_all('a')]
            item['translator'] = [x.get_text() for x in soup.find('span', class_='pl', text=re.compile(u'译者: ')).parent.find_all('a')]
        except:
            pass


        try:
            item['score'] = soup.find('strong', property="v:average").get_text().strip()
            item['votes_num'] = soup.find('span', property="v:votes").get_text().strip()
        except:
            pass
        
        sections = list(soup.find('div', id="db-tags-section").find('div', class_="indent").stripped_strings)
        print(sections)
        if len(sections):
            item['tags'] = {}
            for i in range(0, len(sections), 2):
                item['tags'][sections[i]] = re.search('\((\d+)\)', sections[i + 1]).group(1)
        return item


    def parse_page(self, response):
        url_id = self.get_url_id(response)
        if not url_id:
            return 
        open(os.path.join('douban/', url_id), 'w').write(response.body)

        item = self.generate_item(response)
        print(item)
        open('info.txt', 'a').write('%s\n' % json.dumps(item, ensure_ascii=False).encode('utf8'))
