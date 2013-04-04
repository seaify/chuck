from scrapy import log
from scrapy.http import Request
import random
import time


class InitRequest(object):

    def __init__(self, settings):
        self.proxy_dict={x.strip(): 100.0 for x in open('books_spider/proxy.list').readlines()}

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_request(self, request, spider):
        print('number of proxys is %d' % len(self.proxy_dict))
        proxys = sorted(self.proxy_dict.items(), key=lambda x: x[1])
        request.meta['proxy'] = random.choice(proxys[0:1])[0]
        print('current proxy is %s' % request.meta['proxy'])


    def process_response(self, request, response, spider):
        if response.status != 200:
            del self.proxy_dict[request.meta['proxy']]
            return Request(request.url)
        
        #print(response.status)
        #print(response.body[0:100])
        #print(time.time())
        print(request.meta.get('download_latency'))
        self.proxy_dict[request.meta['proxy']] = request.meta['download_latency']
        #print(response.meta.get('download_latency'))
        return response

    def process_exception(self, request, exception, spider):
        print('hello ' + str(exception))
        del self.proxy_dict[request.meta['proxy']]
