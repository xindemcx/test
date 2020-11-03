from scrapy import cmdline


from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

crawler = CrawlerProcess(settings)
from tianyanchaSpider.spiders import tianyancha_spider
import json
if __name__ == '__main__':
    # settings = get_project_settings()
    #
    cmdline.execute("scrapy crawlall".split())
    # crawler = CrawlerProcess(settings)
    # crawler.crawl('tianyancha_spider')
    # crawler.crawl('company_detail')


    # # pass
    # cmdline.execute("scrapy crawl tianyancha_spider".split())
    # cmdline.execute("scrapy crawl company_detail".split())


#{"GET":{"scheme":"https","host":"api.geetest.com","filename":"/ajax.php","query":{"gt":"f5c10f395211c77e386566112c6abf21","challenge":"5bd8f2d326e0f5b99b1b94145b49024f6j","w":"Y1yvo27dub8DrBZoys8KUpR5jdetgrp6pJ)7r7fVcgkrYGjp99sByaio6lNK)Q4m2XuDVVfqy7GvZPYuVZYn8PR(Ch5jhVO3UwSPnVeH44jEdLoit(DfznVbQGx(q25asT5ZC9ig414Nm0o(rlN(fSqlOLJoIE4xn)Fe2b8TdZR6rs(i1NmY6dKpF573MtO85obTv35oefsGtgkZ8DNMXTnkbSR5DHHZ0Amo4gbvOMo08j8VcWB72GiI6c5NyMHDmHNzKOeiO7vAC04QWG7aRhGt4P4iC)mwYgqmQ056T9bighrrocjDtESpU5ejKXJT3geqvlsbDSIohW9uvQ8gunGvkW3p2ivv6f6QeYUPays.1d0f926efcac65c3b67e64415bbf90ff76327f9df9e8c1fa38814c2bb6f71468356c9ca18d23fa34c5ec43f17da2617ba13907710dcd939125ca331e9671edd7892be4e7043c5705812da46a0ab9f69ce4bd2670d6cebe6615a9871fdffb3a9b285f4847762b4a6e82dbd38aebe24b766678e2edc5ae04dc6143d5d2184cbbf3","callback":"geetest_1598279256776"},"remote":{"地址":"203.107.32.16:443"}}}



