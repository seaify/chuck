# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy import log
from scrapy.http import Request
from scrapy.exceptions import IgnoreRequest
from bs4 import BeautifulSoup
import re
import os
import json


class Filter(object):
    def process_request(self, request, spider):
        log.err('request.url = %s' % request.url);
        m = re.search(u'start=(\d+)', request.url);
        if m and int(m.group(1)) > 900:
            log.msg(m.group(1));
            return IgnoreRequest();

class douban_group_spider(CrawlSpider):
    
    name = 'douban_group'
    allow_domains = 'douban.com'
    allow_users = ['65813704']

    rules = (
        Rule(SgmlLinkExtractor(allow=("discussion\?start=\d+")), callback='get_topics', follow=True),
        )

    def start_requests(self):
        yield Request('http://www.douban.com/people/65813704/groups', callback=self.get_group_discussion)
    
    def get_group_discussion(self, response):
        
        links = SgmlLinkExtractor(allow=("group/[^/]+/$")).extract_links(response)
        for link in links:
            log.msg('group %s' % link.url)
            yield Request('%sdiscussion?start=0' % link.url)
    
    def get_topics(self, response):
        open('group.txt', 'a').write('%s\n' % response.url)
        
        soup = BeautifulSoup(response.body)
        trs = soup.find('table', class_='olt').find_all('tr')[1:]
        for tr in trs:
            es = tr.find_all('a')
            user = re.search('people/([^/]+)/', es[1]['href']).group(1)
            if user in self.allow_users:
                log.msg('%s %s\n' % (es[0]['title'].encode('utf8'), es[0]['href']))
            
            open('log.txt', 'a').write('%s %s %s\n' % (es[0]['title'].encode('utf8'), es[0]['href'], user))
