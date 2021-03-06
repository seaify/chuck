# Scrapy settings for proxy_list project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22'

SPIDER_MODULES = ['proxy_list.spiders']
NEWSPIDER_MODULE = 'proxy_list.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'proxy_list (+http://www.yourdomain.com)'
DOWNLOADER_MIDDLEWARES = {
    'proxy_list.middlewares.InitRequest': 50,
    }
