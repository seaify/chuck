class InitRequest(object):
    
    def process_request(self, request, spider):
        request.meta['proxy'] = 'http://localhost:8087/'
