from tianyanchaSpider.items import PatentItem, SoftwareCopyrightItem, MainPersonItem, TaxCreditLevelItem,\
    ChangeLogItem, CompetingProductItem, BranchItem, InvestItem,FinancingHistoryItem, InvestEventItem
def get_table(table_ele):
    """
    获取table数据
    :param table_ele:
    :return:
    """
    tr_lst = table_ele.xpath(".//tr")
    # 第一行后面都是数据
    data = get_data(tr_lst)

    return data

# def get_tableTest(table_ele):
#     """
#     获取table数据
#     :param table_ele:
#     :return:
#     """
#     tr_lst = table_ele.xpath(".//tr")
#     # 第一行后面都是数据
#     data = get_data1(tr_lst)
#
#     return data
#
#
# def get_data1(tr_lst):
#     """
#     获取数据
#     :param tr_lst:
#     :return:
#     """
#     datas = []
#     for tr in tr_lst:
#         tr_data = get_tr_data_by_tag1(tr, 'td')
#         # print(tr_data)
#         datas.append(tr_data)
#
#     return datas
#
#
# def get_tr_data_by_tag1(tr, tag):
#     """
#     获取一行数据
#     :param tr:
#     :param tag:
#     :return:
#     """
#     nodes = tr.xpath(".//{tag}".format(tag=tag))
#     result ={}
#     key = []
#     value = []
#     for index, node in enumerate(nodes):
#         text = ','.join(node.xpath('.//text()').extract())
#         print(text)
#         if text is None and text:
#             text = node.xpath('./div/@title').extract_first()
#             if text is None:
#                 text=node.xpath('./span/text()').extract_first()
#             if text is None:
#                 text = node.xpath('./a/@title').extract_first()
#         if index % 2 == 0:
#             if text:
#                 key.append(text)
#         elif text:
#             if text:
#                 value.append(text)
#     if len(key) > len(value):
#         value.append('-')
#     for k, v in zip(key, value):
#         if k in result:
#             result[k+"_"] = v;
#         else:
#             result[k] = v;
#
#     return result





def get_tableChange(table_ele):
    """
    获取table数据
    :param table_ele:
    :return:
    """
    tr_lst = table_ele.xpath(".//tr")
    # 第一行后面都是数据
    data = get_data_change(tr_lst)

    return data

def get_data_change(tr_lst):
    """
    获取数据
    :param tr_lst:
    :return:
    """
    datas = []
    for tr in tr_lst:
        tr_data = get_tr_data_by_tag_change(tr, 'td')
        datas.append(tr_data)

    return datas


def get_tr_data_by_tag_change(tr, tag):
    """
    获取一行数据
    :param tr:
    :param tag:
    :return:
    """
    nodes = tr.xpath(".//{tag}".format(tag=tag))
    result ={}
    for index, node in enumerate(nodes):
        text = ','.join(node.xpath('.//text()').extract())
        if text is None and text:
            text = node.xpath('./div/@title').extract_first()
            if text is None:
                text=node.xpath('./span/text()').extract_first()
            if text is None:
                text = node.xpath('./a/@title').extract_first()
        if index==0:
            result['Serial'] = text
        if index==1:
            result['ChangeDate'] = text
        if index==2:
            result['ChangeContent'] = text
        if index==3:
            result['BeforeChange'] = text
        if index==4:
            result['AfterChange'] = text
    return result


def get_data(tr_lst):
    """
    获取数据
    :param tr_lst:
    :return:
    """
    datas = []
    for tr in tr_lst:
        tr_data = get_tr_data_by_tag(tr, 'td')
        datas.append(tr_data)

    return datas


def get_tr_data_by_tag(tr, tag):
    """
    获取一行数据
    :param tr:
    :param tag:
    :return:
    """
    nodes = tr.xpath(".//{tag}".format(tag=tag))
    result ={}
    key=[]
    value=[]
    for index, node in enumerate(nodes):
        text = node.xpath('.//text()').extract_first()
        if text is None and text:
            text = node.xpath('./div/@title').extract_first()
            if text is None:
                text=node.xpath('./span/text()').extract_first()
            if text is None:
                text = node.xpath('./a/@title').extract_first()

        if index%2==0:
            if text:
                key.append(text)
        elif text:
            if text:
                value.append(text)
    if len(key)>len(value):
        value.append('-')
    for k, v in zip(key, value):
        if k in result:
            result[k + "_"] = v;
        else:
            result[k] = v;


        # datas.append(text)


    return result



def getContact_info(item,contact_info):
    item['RegisteredAddress'] = '-'
    for ci in contact_info:
        for key,value in ci.items():
            if "传真" in key:
                pass
            if "区域" in key:
                pass
            if "邮政编码" in key:
                pass
    return item


def getCom_intr(item,com_intr):
    item['OldName'] = '-'
    item['OrganizationCode'] = '-'
    item['CompanyType'] = '-'
    for ci in com_intr:
        for key, value in ci.items():
            if "上市曾用名" in key:
                item['OldName'] = value
            if "工商登记" in key:
                item['OrganizationCode'] = value
            if "所属行业" in key:
                item['CompanyType'] = value

    return item

#企业基本信息
def getBasicData(item,basicdata):
    for ci in basicdata:
        for key, value in ci.items():
            if "曾用名" in key:
                item['OldName'] = value
            if "工商登记" in key:
                item['OrganizationCode'] = value
            if "公司类型" in key:
                item['CompanyType'] = value
            if "行业" in key:
                item['Industry'] = value
            if "注册地址" in key:
                item['RegisteredAddress'] = value
            if "注册资本" in key:
                item['RegisteredCapital'] = value
            if "工商注册号" in key:
                item['CommercialRegistrationNumber'] = value
            if "组织机构代码" in key:
                item['OrganizationCode'] = value
            if "公司类型" in key:
                item['CompanyType'] = value
            if "统一社会信用代码" in key:
                item['UnifiedSocialCreditCode'] = value
            if "核准日期" in key:
                item['ApprovalDate'] = value
            if "登记机关" in key:
                item['RegisterOffice'] = value
            if "人员规模" in key:
                item['StaffSize'] = value
            if "参保人数" in key:
                item['InsuredCount'] = value
            if "曾用名" in key:
                item['OldName'] = value
            if "营业期限" in key:
                item['OperatingPeriod'] = value
            if "实缴资本" in key:
                item['ContributedCapital'] = value
            if "经营范围" in key:
                item['BusinessScope'] = value
            if "纳税人识别号" in key:
                item['TaxpayerIdentificationNumber'] = value
                # 核准日期
                # 公司类型 人员规模
    return item


def getPatenData(CompanyGUID,patendata):
    patens=[]
    for ci in patendata:
        index =0
        item = PatentItem()
        item['CompanyGUID']= CompanyGUID
        for key, value in ci.items():
            if index ==0:
                item['AnnouncementDate']=value
            if index ==1:
                item['PatentName']=key
                item['ApplicationNumber'] = value
            if index ==2:
                item['PublishedApplicationNumber']=key
                item['PatentType']=value
            item['ItemType'] = 'patenType'
            index+=1
        patens.append(item)
    return patens

#软件著作权
def getCopyrightListData(CompanyGUID,copyrightData):
    copyrights=[]
    for ci in copyrightData:
        index =0
        item = SoftwareCopyrightItem()
        item['CompanyGUID']= CompanyGUID
        for key, value in ci.items():
            if index ==0:
                item['ApprovedDate']=value
            if index ==1:
                item['SoftwareFullname']=key
                item['SoftwareShortname'] = value
            if index ==2:
                item['RegisterNumber']=key
                item['ClassificationNumber']=value
            if index == 3:
                item['VersionNumber'] = key
            item['ItemType'] = 'copyrightType'
            index+=1
        copyrights.append(item)
    return copyrights

#主要人员
def getStaffData(CompanyGUID,staffData):
    staffDatas=[]

    for staff in staffData:
        index = 0
        if len(staff) > 2:
            item = MainPersonItem()
            item['CompanyGUID'] = CompanyGUID
            for key, value in staff.items():
                if index == 1:
                    item['PersonName'] = value
                if index == 2:
                    item['JobName'] = value
                item['ItemType'] = 'staffType'
                index += 1
            staffDatas.append(item)
    return staffDatas


def getTaxcreditData(CompanyGUID,staffData):
    taxcreditDatas=[]
    for sd in staffData:
        index =0
        item = TaxCreditLevelItem()
        item['CompanyGUID'] = CompanyGUID
        for key, value in sd.items():
            if index == 0:
                item['EvaluationDate'] = value
            if index == 1:
                item['CreditLevel'] = key
                item['CreditLevelType'] = value
            if index == 2:
                item['TaxpayerIdentificationNumber'] = key
                item['EvaluationDepartment'] = value
            item['ItemType'] = 'taxcredit'
            index += 1
        taxcreditDatas.append(item)
    return taxcreditDatas


def getChangeinfoData(CompanyGUID,ChangeinfoData):
    Changeinfos = []
    for cinfo in ChangeinfoData:
        if cinfo:
            item = ChangeLogItem()
            item['CompanyGUID'] = CompanyGUID
            item['ChangeDate'] = cinfo['ChangeDate']
            item['ChangeContent']=cinfo['ChangeContent']
            item['BeforeChange']=cinfo['BeforeChange']
            item['AfterChange']=cinfo['AfterChange']
            item['ItemType'] = 'changeinfo'
            Changeinfos.append(item)
    return Changeinfos

def getJingPingData(CompanyGUID,JingPinData):
    JingPings = []
    # CompetingProductID = scrapy.Field()
    # CompanyGUID = scrapy.Field()
    # Product = scrapy.Field()
    # CurrentFinancingRound = scrapy.Field()
    # EstablishDate = scrapy.Field()
    # Area = scrapy.Field()
    # Business = scrapy.Field()
    # Industry = scrapy.Field()
    for jPing in JingPinData:
        index = 0
        if len(jPing)>3:
            item = CompetingProductItem()
            item['CompanyGUID'] = CompanyGUID
            for key, value in jPing.items():
                if index == 0:
                        item['Product'] = value
                if index == 2:
                    item['CurrentFinancingRound'] = key
                if index == 3:
                    item['EstablishDate'] = key
                    item['Industry'] = value

                if index == 4:
                    item['Area'] = key
                    item['Business'] = value
                    # EstablishDate
                item['ItemType'] = 'jingpin'
                index += 1
            JingPings.append(item)
    return JingPings



def getBranchData(CompanyGUID,branchData):
    branchs = []
    for branch in branchData:
        index = 0
        item = BranchItem()
        item['CompanyGUID'] = CompanyGUID
        if len(branch)==5:
            for key, value in branch.items():
                if index == 1:
                    item['CorpName'] = value
                if index == 3:
                    item['CorpManager'] = key
                if index == 4:
                    item['EstablishDate'] = key
                    item['State'] = value

                item['ItemType'] = 'branch'
                index += 1
            branchs.append(item)
        if len(branch)==4:
            for key, value in branch.items():
                if index == 1:
                    item['CorpName'] = value
                if index == 2:
                    item['CorpManager'] = key
                    item['EstablishDate'] = value
                if index == 3:
                    item['State'] = key

                item['ItemType'] = 'branch'
                index += 1
            branchs.append(item)
    return branchs


def getInvestData(CompanyGUID,investData):
    invests = []
    for invest in investData:
        index = 0
        item = InvestItem()
        item['CompanyGUID'] = CompanyGUID
        if len(invest)>3:
            for key, value in invest.items():
                if index == 1:
                    item['InvestToCompany'] = value
                if index == 3:
                    item['InvestToCompanyManager'] = key
                    item['EstablishDate'] = value
                if index == 4:
                    item['RegisteredCapital'] = key
                    item['InvestPercent'] = value

                item['ItemType'] = 'invest'
                index += 1
            invests.append(item)
    return invests


def getRongZiData(CompanyGUID,rongziData):
    rongzis = []
    for rongzi in rongziData:
        index = 0
        item = FinancingHistoryItem()
        item['CompanyGUID'] = CompanyGUID
        for key, value in rongzi.items():
            if index == 0:
                item['DisclosureDate'] = value
            if index == 1:
                item['TransactionAmount'] = key
                item['FinancingRaund'] = value
            if index == 3:
                item['Investor'] = key

            item['ItemType'] = 'rongzi'
            index += 1
            rongzis.append(item)
    return rongzis


def getTouyZiData(CompanyGUID,touziData):
    touzis = []
    for touzi in touziData:
        index = 0
        item = InvestEventItem()
        item['CompanyGUID'] = CompanyGUID
        if len(touzi)>3:
            for key, value in touzi.items():
                if index == 0:
                    item['EventTime'] = value
                if index == 1:
                    item['InvestRound'] = key
                    item['Investor'] = value
                if index == 2:
                    item['InvestAmount'] = key
                if index == 3:
                    item['Production'] = value
                if index == 4:
                    item['Industry'] = key
                    item['Area'] = value
                if index == 5:
                    item['Business'] = key

                item['ItemType'] = 'touzi'
                index += 1
                touzis.append(item)
    return touzis

import xlrd
def getExecleData(path):
    data = xlrd.open_workbook(path)
    table = data.sheet_by_name(u'Sheet1')
    nrows = table.nrows
    ncols = table.ncols
    companies=[]
    for i in range(1,nrows):
        for j in range(ncols):
            content = table.cell(i,j).value
            companies.append(content)
    return companies


# 写cookie到文件当中
import configparser
from os import path
def setCreateCookie(cookiestr):
    config = configparser.RawConfigParser()
    # 获取当前目录
    d = path.dirname(__file__)
    config.read(d + "/../config/cookie.ini")
    if "ck" not in config.sections():
        config.add_section("ck")
    config.set("ck", "cookiestr", str(cookiestr))
    with open(d + "/../config/cookie.ini", "w+") as f:
        config.write(f)


### 文件当中取cookie
def getCreateCookie():
    config = configparser.RawConfigParser()
    # 获取当前目录
    d = path.dirname(__file__)
    config.read(d + "/../config/cookie.ini")
    creattime = config.get("ck","cookiestr")
    return creattime



from selenium import webdriver
def getCookieStr(url):
    browser = webdriver.Firefox()
    browser.implicitly_wait(4)
    browser.get(url)
    Cookiese = browser.get_cookies()



    strr = ''
    for c in Cookiese:
        strr += c['name']
        strr += '='
        strr += c['value']
        strr += ';'
    return strr


# 写cookie到文件当中
