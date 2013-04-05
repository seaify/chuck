from scrapy.dupefilter import RFPDupeFilter
from scrapy.utils.request import request_fingerprint
import os

class BooksDupeFilter(RFPDupeFilter):
    """for resume douban spider"""

    def request_seen(self, request):
        fp = request_fingerprint(request)
        if fp in self.fingerprints:
            return True
        self.fingerprints.add(fp)
        if 'not_write_file' in request.meta and request.meta['not_write_file']:
            return
        if self.file:
            self.file.write(fp + os.linesep)
