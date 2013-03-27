# Scrapy settings for books_spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'books_spider'

SPIDER_MODULES = ['books_spider.spiders']
NEWSPIDER_MODULE = 'books_spider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'books_spider (+http://www.yourdomain.com)'

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_DEBUG = True

DOWNLOADER_MIDDLEWARES = {
    'books_spider.middlewares.InitRequest': 50,
    }
