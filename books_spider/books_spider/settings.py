# Scrapy settings for books_spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22'


SPIDER_MODULES = ['books_spider.spiders']
NEWSPIDER_MODULE = 'books_spider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'books_spider (+http://www.yourdomain.com)'

#AUTOTHROTTLE_ENABLED = True
#AUTOTHROTTLE_DEBUG = True
COOKIES_ENABLED = False
RETRY_TIMES = 0

DOWNLOADER_MIDDLEWARES = {
    'books_spider.middlewares.InitRequest': 50,
    }
