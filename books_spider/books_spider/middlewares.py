class InitRequest(object):
    
    def process_request(self, request, spider):
        request.meta['proxy'] = 'http://123.134.95.131:80/'
        #request.meta['proxy'] = 'http://localhost:8087/'
