# -*- coding: utf-8 -*-
import uuid
import scrapy
from tianyanchaSpider.items import CompanyInfoItem,PatentItem
from os import path
import os
import configparser
import logging
from tianyanchaSpider.para.parameter import Parameter
scrawl_urls, companies = Parameter().get_tianyan_para()
import tianyanchaSpider.tools.tools
class TianyanchaSpiderSpider(scrapy.Spider):
    config = configparser.ConfigParser()
    # 获取当前目录
    d = path.dirname(__file__)
    # 获取当前目录的父级目录
    parent_path = os.path.dirname(d)
    logs_path = os.path.dirname(parent_path)
    custom_settings = {
        'LOG_FILE': logs_path + '/logs/tianyancha_log.log',
    }
    name = 'tianyancha_spider'
    allowed_domains = ['tianyancha.com']

    def start_requests(self):
        headers = {
                "Host": "www.tianyancha.com",
                "Connection": "keep-alive",
                "Cache-Control": "max-age=0",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User":"?1",
                "Referer": "www.tianyancha.com/",
                "Upgrade-Insecure-Requests": "1",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            }
        strr = tianyanchaSpider.tools.tools.getCreateCookie()
        headers['Cookie'] = strr
        while scrawl_urls.__len__():
            try:
                url = scrawl_urls.pop()
                company_name = companies.pop()
                yield scrapy.Request(url=url, headers=headers,
                              meta={'headers':headers, 'url': url, 'company_name':company_name,'handle_httpstatus_list': [302,412, 404, 403, 407, 500, 502, 503, 504, 408, 416, 400]}, callback=self.parse,
                              dont_filter=True)
            except Exception as e:
                logging.info(e)



    def parse(self, response):
        url = response.meta['url']
        headers = eval(str(response.meta['headers']))
        if response.status == 200:
            company_infos= CompanyInfoItem();
            company_name = response.meta['company_name']
            company_url = response.xpath('//*[@id="web-content"]//div[@class="header"]//a/@href').extract_first()
            # 企业名称
            # 企业状态
            company_state= response.xpath("//*[@id='web-content']//div[@class='content']/div[@class='header']//div//text()").extract_first()
            companyElement = response.xpath('//*[@id="web-content"]//div[@class="info row text-ellipsis"]')
            # 法人代表
            frdb =companyElement.xpath('./div[@class="title -wider text-ellipsis"]/a/@title').extract_first()
            faren_url =companyElement.xpath('./div[@class="title -wider text-ellipsis"]/a/@href').extract_first()
            # 注册资金
            registeredCapital =companyElement.xpath("//div[@class='content']//div[text()='注册资本：']/span/text()").extract_first()
            # 注册时间
            register_date =companyElement.xpath("//div[@class='content']//div[text()='成立日期：']/span/text()").extract_first()
            # //div[@class='web-content]//div[text()='成立日期']/span
            company_infos['CompanyName'] = company_name
            company_infos['CompanyState'] = company_state
            company_infos['RegisteredCapital'] = registeredCapital
            company_infos['EstablishDate'] = register_date
            company_infos['CompanyDetailURL'] = company_url
            company_infos['CompanyGUID'] = uuid.uuid1()
            company_infos['ItemType'] = 'companyinfo'
            yield company_infos
        #出现验证码
        # if response.status == 302:
        #     # 重新获取cookie
        #     try:
        #         oldCookie = tianyanchaSpider.tools.tools.getCreateCookie()
        #         if oldCookie == headers['Cookie']:
        #             # newCookie = tianyanchaSpider.tools.tools.getCookieStr(url)
        #             crack = CrackGeetest()
        #             cookie_str = crack.crack()
        #             headers['Cookie'] = cookie_str
        #             tianyanchaSpider.tools.tools.setCreateCookie(cookie_str)
        #             # crack.close_browse()
        #             yield scrapy.Request(
        #                 url=url, headers=headers, meta={'header': headers, 'url': url}, callback=self.parse,
        #                 priority=0, dont_filter=True)
        #     except Exception as e:
        #         print(e)





