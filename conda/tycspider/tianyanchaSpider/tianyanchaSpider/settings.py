# -*- coding: utf-8 -*-

# Scrapy settings for tianyanchaSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tianyanchaSpider'

SPIDER_MODULES = ['tianyanchaSpider.spiders']
NEWSPIDER_MODULE = 'tianyanchaSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tianyanchaSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
# DOWNLOAD_DELAY = 1
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False
HTTPERROR_ALLOWED_CODES = [302, 404]
# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'tianyanchaSpider.middlewares.TianyanchaspiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'tianyanchaSpider.middlewares.my_proxy': 540,
   # 'tianyanchaSpider.middlewares.RandomUserAgentMiddlware': 543,
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
   'tianyanchaSpider.middlewares.TianyanchaspiderDownloaderMiddleware': 543,
}
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}
# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'tianyanchaSpider.pipelines.TianyanchaspiderPipeline': 300,
}
COMMANDS_MODULE = 'tianyanchaSpider.commands'
LOG_LEVEL = 'INFO'
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False
COOKIES_ENABLED = False
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10
AUTOTHROTTLE_TARGET_CONCURRENCY = 1000 #同一时间的请求量（并发量）
AUTOTHROTTLE_DEBUG = False # 调试时设为True
#CONCURRENT_REQUESTS_PER_DOMAIN = 100 #同一域名的并发量
#CONCURRENT_REQUESTS_PER_IP = 50
DOWNLOAD_DELAY = 1 #自动节流器会把delay控制在DOWNLOAD_DELAY与AUTOTHROTTLE_MAX_DELAY之间的最优值
