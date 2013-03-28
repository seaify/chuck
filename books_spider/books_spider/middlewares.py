from scrapy import log


class InitRequest(object):
    idx = 0

    def process_request(self, request, spider):
        request.meta['proxy'] = spider.proxy_list[self.idx % len(spider.proxy_list)]
        log.msg(request.meta['proxy'])
        self.idx += 1
