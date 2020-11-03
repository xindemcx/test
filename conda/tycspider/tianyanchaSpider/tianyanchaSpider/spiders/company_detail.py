import scrapy

from tianyanchaSpider.items import CompanyInfoItem
import tianyanchaSpider.tools
from tianyanchaSpider.para.parameter import Parameter
companyGUIDs, scrawl_urls = Parameter().get_tianyancha_detail()
import logging
class CompanyDetailSpider(scrapy.Spider):
    name = 'company_detail'
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
                companyGUID=companyGUIDs.pop()
                yield scrapy.Request(url=url, headers=headers,
                              meta={'headers':headers, 'url': url,'companyGUID':companyGUID,'handle_httpstatus_list': [302,412, 404, 403, 407, 500, 502, 503, 504, 408, 416, 400]}, callback=self.parse,
                              dont_filter=True)
            except Exception as e:
                logging.info(e)

    def parse(self, response):
        # print('---vvvv----')
        url = response.meta['url']
        headers = eval(str(response.meta['headers']))
        if response.status == 200:
            headers = eval(str(response.meta['headers']))
            CompanyGUID = str(response.meta['companyGUID'])
            CompanyName = response.xpath('//*[@id="web-content"]//div[@class="header"]//h1/text()').extract_first()
            companyele = response.xpath(
                            '//*[@id="nav-main-corpContactInfoCount"]//table[@class="table -striped-col -breakall"]')
                        # 公司联系
            contact_info = tianyanchaSpider.tools.tools.get_table(companyele)
            companyInfo = CompanyInfoItem()
            companyInfo = tianyanchaSpider.tools.tools.getContact_info(companyInfo, contact_info)
            #
            telephone = response.xpath('//*[@id="company_web_top"]/div[2]/div[3]/div[3]/div[1]/div[1]/span[2]/text()').extract_first()
            website= response.xpath('//*[@id="company_web_top"]/div[2]/div[3]/div[3]/div[2]/div[1]/a/@href').extract_first()
            address= response.xpath('//*[@id="company_web_top"]/div[2]/div[3]/div[3]/div[2]/div[2]/div/div/text()').extract_first()
            email = response.xpath('//*[@id="company_web_top"]/div[2]/div[3]/div[3]/div[1]/div[2]/span[2]/text()').extract_first()
            companyInfo['WebSite'] =website
            companyInfo['Telephone'] =telephone
            companyInfo['Address'] =address
            companyInfo['Email'] =email
            companyInfo['CompanyGUID'] = CompanyGUID
            companyInfo['CompanyName'] = CompanyName
            # 公司简介
            com_intr_ele = response.xpath('//*[@id="nav-main-stockNum"]//table[@class="table -striped-col"]')
            com_intr = tianyanchaSpider.tools.tools.get_table(com_intr_ele)
            companyInfo = tianyanchaSpider.tools.tools.getContact_info(companyInfo, com_intr)

            #基本信息
            basic_intr_ele = response.xpath('//div[@class="block-data"]//table[@class="table -striped-col -border-top-none -breakall"]')
            basic_intr = tianyanchaSpider.tools.tools.get_table(basic_intr_ele)
            companyInfo = tianyanchaSpider.tools.tools.getBasicData(companyInfo, basic_intr)
            companyInfo['ItemType']='basicType'
            #专利信息
            patent_intr_ele = response.xpath('//div[@id="_container_patent"]/table')
            patent_intr = tianyanchaSpider.tools.tools.get_table(patent_intr_ele)
            patentList= tianyanchaSpider.tools.tools.getPatenData(CompanyGUID, patent_intr)

            #软件著作权
            copyrightCountEle = response.xpath('//*[@id="_container_copyright"]/table')
            copyright_intr = tianyanchaSpider.tools.tools.get_table(copyrightCountEle)
            copyrightList = tianyanchaSpider.tools.tools.getCopyrightListData(CompanyGUID, copyright_intr)
            #主要人员
            #/div[@id = '']//table
            staffEle = response.xpath("//div[@id='_container_staff']/div[@class='clearfix']/table")
            staff_intro = tianyanchaSpider.tools.tools.get_table(staffEle)
            staffList = tianyanchaSpider.tools.tools.getStaffData(CompanyGUID, staff_intro)
            #
            #//div[@id='_container_taxcredit']/table
            taxcreditEle = response.xpath("//div[@id='_container_taxcredit']/table")
            taxcredit_intro = tianyanchaSpider.tools.tools.get_table(taxcreditEle)
            taxcreditList = tianyanchaSpider.tools.tools.getTaxcreditData(CompanyGUID, taxcredit_intro)
            #
            #变更记录
            changeinfoEle = response.xpath("//div[@id='_container_changeinfo']//table")
            changeinfo_intro = tianyanchaSpider.tools.tools.get_tableChange(changeinfoEle)
            changeinfoList = tianyanchaSpider.tools.tools.getChangeinfoData(CompanyGUID, changeinfo_intro)
            #
            # _container_jingpin  竞品信息
            jingpinEle = response.xpath("//*[@id='_container_jingpin']/div/table")
            jingpin_intro = tianyanchaSpider.tools.tools.get_table(jingpinEle)
            jingpinList = tianyanchaSpider.tools.tools.getJingPingData(CompanyGUID, jingpin_intro)
            #
            #分支机构.//div[@id='_container_branch']/table
            branchEle = response.xpath(".//div[@id='_container_branch']/table")
            branch_intro = tianyanchaSpider.tools.tools.get_table(branchEle)
            branchList = tianyanchaSpider.tools.tools.getBranchData(CompanyGUID, branch_intro)
            #
            # 对外投资
            investEle = response.xpath(".//div[@id='_container_invest']//table[@class='table -breakall']")
            invest_intro = tianyanchaSpider.tools.tools.get_table(investEle)
            investList = tianyanchaSpider.tools.tools.getInvestData(CompanyGUID, invest_intro)

            # _container_rongzi融资历程
            rongziEle = response.xpath(".//div[@id='_container_rongzi']/table")
            rongzi_intro = tianyanchaSpider.tools.tools.get_table(rongziEle)
            rongziList = tianyanchaSpider.tools.tools.getRongZiData(CompanyGUID, rongzi_intro) # _container_rongzi融资历程

            touziEle = response.xpath(".//div[@id='_container_touzi']/table")
            touzi_intro = tianyanchaSpider.tools.tools.get_table(touziEle)
            touziEleList = tianyanchaSpider.tools.tools.getTouyZiData(CompanyGUID, touzi_intro)
            yield companyInfo

            #
            for item in copyrightList:
                yield item
            for item in patentList:
                yield item
            for item in staffList:
                yield item
            for item in taxcreditList:
                yield item
            for item in changeinfoList:
                yield item
            for item in jingpinList:
                yield item
            for item in branchList:
                yield item
            for item in investList:
                yield item
            for item in rongziList:
                yield item
            for item in touziEleList:
                yield item
            # 出现验证码
        else:
            pass
            # # 重新获取cookie
            # try:
            #     oldCookie = tianyanchaSpider.tools.tools.getCreateCookie()
            #     if oldCookie == headers['Cookie']:
            #         # newCookie = tianyanchaSpider.tools.tools.getCookieStr(url)
            #         crack = CrackGeetest()
            #         cookie_str = crack.crack()
            #         headers['Cookie'] = cookie_str
            #         tianyanchaSpider.tools.tools.setCreateCookie(cookie_str)
            #         # crack.close_browse()
            #         yield scrapy.Request(
            #             url=url, headers=headers, meta={'headers': headers, 'url': url}, callback=self.parse,
            #             priority=0, dont_filter=True)
            # except Exception as e:
            #     print(e)
