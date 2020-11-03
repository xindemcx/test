# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TianyanchaspiderItem(scrapy.Item):
    pass


class CompanyInfoItem(scrapy.Item):
    CompanyGUID = scrapy.Field()
    CompanyName = scrapy.Field()  #公司名称
    CompanyState = scrapy.Field() #经营状态
    ItemType = scrapy.Field()   #
    RegisteredCapital = scrapy.Field()   #注册资本
    EstablishDate =scrapy.Field()     #成立日期
    CommercialRegistrationNumber =scrapy.Field()   #工商注册号
    UnifiedSocialCreditCode =scrapy.Field()    #统一社会信用代码
    OrganizationCode =scrapy.Field()    #组织机构代码
    TaxpayerIdentificationNumber =scrapy.Field()   #纳税人识别号
    CompanyType =scrapy.Field()   #公司类型
    OperatingPeriod =scrapy.Field()    #营业期限
    ApprovalDate =scrapy.Field()      #核准日期
    ContributedCapital =scrapy.Field()      #实缴资本
    StaffSize =scrapy.Field()    #人员规模
    InsuredCount =scrapy.Field()    #参保人数
    RegisterOffice =scrapy.Field()    #登记机关
    OldName =scrapy.Field()    #曾用命
    RegisteredAddress =scrapy.Field()   #注册地址
    Telephone =scrapy.Field()    #电话
    Email =scrapy.Field()     #邮箱
    WebSite =scrapy.Field()    #网站
    Industry =scrapy.Field()    #行业
    Address =scrapy.Field()    #地址
    BusinessScope =scrapy.Field()   #经营范围
    CompanyDetailURL= scrapy.Field() #网站详情url



class PatentItem(scrapy.Item):
    ItemType = scrapy.Field()
    PatentID = scrapy.Field()
    CompanyGUID = scrapy.Field()
    AnnouncementDate = scrapy.Field()
    PatentName = scrapy.Field()
    ApplicationNumber = scrapy.Field()
    PublishedApplicationNumber = scrapy.Field()
    PatentType = scrapy.Field()



class SoftwareCopyrightItem(scrapy.Item):
    ItemType = scrapy.Field()
    SoftwareCopyrightID = scrapy.Field()
    CompanyGUID = scrapy.Field()
    ApprovedDate = scrapy.Field()
    SoftwareFullname = scrapy.Field()
    SoftwareShortname = scrapy.Field()
    RegisterNumber = scrapy.Field()
    ClassificationNumber = scrapy.Field()
    VersionNumber = scrapy.Field()


class MainPersonItem(scrapy.Field):
    ItemType = scrapy.Field()
    PersonID = scrapy.Field()
    CompanyGUID = scrapy.Field()
    PersonName = scrapy.Field()
    JobName = scrapy.Field()



class TaxCreditLevelItem(scrapy.Field):
    ItemType = scrapy.Field()
    TaxCreditLevelID = scrapy.Field()
    CompanyGUID = scrapy.Field()
    EvaluationDate = scrapy.Field()
    CreditLevel = scrapy.Field()
    CreditLevelType = scrapy.Field()
    TaxpayerIdentificationNumber = scrapy.Field()
    EvaluationDepartment = scrapy.Field()
    JobName = scrapy.Field()


class FinancingHistoryItem(scrapy.Field):
    FinancingHistoryID = scrapy.Field()
    CompanyGUID = scrapy.Field()
    DisclosureDate = scrapy.Field()
    FinancingRaund = scrapy.Field()
    TransactionAmount = scrapy.Field()
    Investor = scrapy.Field()

class BranchItem(scrapy.Field):
    BranchID = scrapy.Field()
    CompanyGUID = scrapy.Field()
    CorpName = scrapy.Field()
    CorpManager = scrapy.Field()
    EstablishDate = scrapy.Field()
    State = scrapy.Field()


class InvestItem(scrapy.Field):
    InvestID = scrapy.Field()
    CompanyGUID = scrapy.Field()
    InvestToCompany = scrapy.Field()
    InvestToCompanyManager = scrapy.Field()
    InvestPercent = scrapy.Field()
    RegisteredCapital = scrapy.Field()
    EstablishDate = scrapy.Field()

class ChangeLogItem(scrapy.Field):
    ChangeLogID = scrapy.Field()
    CompanyGUID = scrapy.Field()
    ChangeDate = scrapy.Field()
    ChangeContent = scrapy.Field()
    BeforeChange = scrapy.Field()
    AfterChange = scrapy.Field()


class CompetingProductItem(scrapy.Field):
    CompetingProductID = scrapy.Field()
    CompanyGUID = scrapy.Field()
    Product = scrapy.Field()
    CurrentFinancingRound = scrapy.Field()
    EstablishDate = scrapy.Field()
    Area = scrapy.Field()
    Business = scrapy.Field()
    Industry = scrapy.Field()


class InvestEventItem(scrapy.Field):
    InvestEventID = scrapy.Field()
    CompanyGUID = scrapy.Field()
    EventTime = scrapy.Field()
    InvestRound = scrapy.Field()
    InvestAmount = scrapy.Field()
    Investor = scrapy.Field()
    Production = scrapy.Field()
    Area = scrapy.Field()
    Industry = scrapy.Field()
    Business = scrapy.Field()