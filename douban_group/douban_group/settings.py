# Scrapy settings for douban_group project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'douban_group'

SPIDER_MODULES = ['douban_group.spiders']
NEWSPIDER_MODULE = 'douban_group.spiders'

DOWNLOADER_MIDDLEWARES = {'douban_group.spiders.group.Filter': 100};

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'douban_group (+http://www.yourdomain.com)'
