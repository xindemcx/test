
import logging
import datetime



def updateCompanyInfostTB(item,cursor,conn):
    CompanyGUID = str(item['CompanyGUID'])
    CompanyName = item['CompanyName']
    Address = item['Address']
    Email = item['Email']
    WebSite = item['WebSite']
    Telephone = item['Telephone']
    Industry = item['Industry']
    RegisteredCapital = item['RegisteredCapital']
    RegisteredAddress = item['RegisteredAddress']
    ApprovalDate = item['ApprovalDate']
    RegisterOffice = item['RegisterOffice']
    StaffSize = item['StaffSize']
    InsuredCount = item['InsuredCount']
    OldName = item['OldName']
    OperatingPeriod = item['OperatingPeriod']
    ContributedCapital = item['ContributedCapital']
    BusinessScope = item['BusinessScope']
    TaxpayerIdentificationNumber = item['TaxpayerIdentificationNumber']
    CommercialRegistrationNumber = item['CommercialRegistrationNumber']
    UnifiedSocialCreditCode = item['UnifiedSocialCreditCode']
    OrganizationCode = item['OrganizationCode']
    CompanyType = item['CompanyType']
    sel_sql = "SELECT * FROM tb_companyinfo WHERE CompanyGUID='" + CompanyGUID + "'"
    cursor.execute(sel_sql)  # 执行sql语句
    row = cursor.fetchone()  # 读取查询结果,
    if row:
        createDateTime = datetime.datetime.now()
        try:
            sql = """update tb_companyinfo set CompanyName =%s, Address =%s, Email=%s, WebSite=%s, Telephone=%s, Industry=%s, UnifiedSocialCreditCode=%s,OrganizationCode=%s,CompanyType=%s,
            RegisteredCapital=%s, RegisteredAddress=%s, ApprovalDate=%s, RegisterOffice=%s,CommercialRegistrationNumber=%s,
            StaffSize=%s, InsuredCount=%s, OldName=%s, OperatingPeriod=%s, ContributedCapital=%s, BusinessScope=%s,TaxpayerIdentificationNumber=%s where CompanyGUID=%s"""
            # 执行SQL语句
            cursor.execute(sql, (
                CompanyName, Address, Email, WebSite, Telephone, Industry, UnifiedSocialCreditCode, OrganizationCode, CompanyType,
                RegisteredCapital, RegisteredAddress, ApprovalDate, RegisterOffice, CommercialRegistrationNumber,
                StaffSize, InsuredCount, OldName, OperatingPeriod, ContributedCapital, BusinessScope, TaxpayerIdentificationNumber,
                CompanyGUID))
            # 提交到数据库执行
            conn.commit()
        except Exception as e:
            logging.info(e)
            # 发生错误时回滚
            conn.rollback()
    else:
        try:
            pass
        except Exception as e:
            logging.info(e)


def inputTouZiTB(item,cursor,conn):
    CompanyGUID = str(item['CompanyGUID'])
    EventTime = item['EventTime']
    InvestRound = item['InvestRound']
    InvestAmount = item['InvestAmount']
    Investor = item['Investor']
    Production = item['Production']
    Area = item['Area']
    Industry = item['Industry']
    Business = item['Business']
    sel_sql = "SELECT * FROM tb_investevent WHERE CompanyGUID='" + CompanyGUID + "' and EventTime = '"+ EventTime +"'"

    cursor.execute(sel_sql)  # 执行sql语句
    row = cursor.fetchone()  # 读取查询结果,
    if not row:
        createDateTime = datetime.datetime.now()
        try:
            # file_path 网络地址 ，filename 文件名
            cursor.execute("""INSERT INTO tb_investevent(CompanyGUID,EventTime,InvestRound,InvestAmount,Investor,Production, Area, Industry, Business)
                                                                                                               VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                           (
                               CompanyGUID,
                               EventTime,
                               InvestRound,
                               InvestAmount,
                               Investor,
                               Production,
                               Area,
                               Industry,
                               Business
                           ))
            conn.commit()
        except Exception as e:
            logging.info(e)
            # 发生错误时回滚
            conn.rollback()
    else:
        try:
            pass
        except Exception as e:
            logging.info(e)

def inputCompanyInfostTB(item,cursor,conn):
    CompanyGUID = str(item['CompanyGUID'])
    CompanyName = item['CompanyName']
    CompanyState = item['CompanyState']
    RegisteredCapital = item['RegisteredCapital']
    EstablishDate = item['EstablishDate']
    CompanyDetailURL = item['CompanyDetailURL']
    sel_sql = "SELECT * FROM tb_companyinfo WHERE CompanyName='" + CompanyName + "'"
    cursor.execute(sel_sql)  # 执行sql语句
    row = cursor.fetchone()  # 读取查询结果,
    if not row:
        createDateTime = datetime.datetime.now()
        try:
            # file_path 网络地址 ，filename 文件名
            cursor.execute("""INSERT INTO tb_companyinfo(CompanyGUID,CompanyName,CompanyState,RegisteredCapital,EstablishDate,CompanyDetailURL)
                                                                                                               VALUES (%s,%s,%s,%s,%s,%s)""",
                           (
                               CompanyGUID,
                               CompanyName,
                               CompanyState,
                               RegisteredCapital,
                               EstablishDate,
                               CompanyDetailURL
                           ))
            conn.commit()
        except Exception as e:
            logging.info(e)
            # 发生错误时回滚
            conn.rollback()
    else:
        try:
            pass
        except Exception as e:
            logging.info(e)


def inputPatenTB(item,cursor,conn):
    CompanyGUID = str(item['CompanyGUID'])
    AnnouncementDate = item['AnnouncementDate']
    PatentName = item['PatentName']
    ApplicationNumber = item['ApplicationNumber']
    PublishedApplicationNumber = item['PublishedApplicationNumber']
    PatentType = item['PatentType']
    sel_sql = "SELECT * FROM tb_patent WHERE ApplicationNumber='" + ApplicationNumber + "'"
    cursor.execute(sel_sql)  # 执行sql语句
    row = cursor.fetchone()  # 读取查询结果,
    if not row:
        createDateTime = datetime.datetime.now()
        try:
            # file_path 网络地址 ，filename 文件名
            cursor.execute("""INSERT INTO tb_patent(CompanyGUID,AnnouncementDate,PatentName,ApplicationNumber,PublishedApplicationNumber,PatentType)
                                                                                                               VALUES (%s,%s,%s,%s,%s,%s)""",
                           (
                               CompanyGUID,
                               AnnouncementDate,
                               PatentName,
                               ApplicationNumber,
                               PublishedApplicationNumber,
                               PatentType
                           ))
            conn.commit()
        except Exception as e:
            logging.info(e)
            # 发生错误时回滚
            conn.rollback()
    else:
        try:
            pass
        except Exception as e:
            logging.info(e)


def inputCopyrightTB(item,cursor,conn):
    CompanyGUID = str(item['CompanyGUID'])
    ApprovedDate = item['ApprovedDate']
    ClassificationNumber = item['ClassificationNumber']
    RegisterNumber = item['RegisterNumber']
    SoftwareFullname = item['SoftwareFullname']
    SoftwareShortname = item['SoftwareShortname']
    VersionNumber = item['VersionNumber']
    sel_sql = "SELECT * FROM tb_softwarecopyright WHERE RegisterNumber='" + RegisterNumber + "'"
    cursor.execute(sel_sql)  # 执行sql语句
    row = cursor.fetchone()  # 读取查询结果,
    if not row:
        createDateTime = datetime.datetime.now()
        try:
            # file_path 网络地址 ，filename 文件名
            cursor.execute("""INSERT INTO tb_softwarecopyright(CompanyGUID,ApprovedDate,SoftwareShortname,ClassificationNumber,RegisterNumber,SoftwareFullname,VersionNumber)
                                                                                                               VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                           (
                               CompanyGUID,
                               ApprovedDate,
                               SoftwareShortname,
                               ClassificationNumber,
                               RegisterNumber,
                               SoftwareFullname,
                               VersionNumber
                           ))
            conn.commit()
        except Exception as e:
            logging.info(e)
            # 发生错误时回滚
            conn.rollback()
    else:
        try:
            pass
        except Exception as e:
            logging.info(e)

def inputStaffTB(item,cursor,conn):
    CompanyGUID = str(item['CompanyGUID'])
    PersonName = item['PersonName']
    JobName = item['JobName']
    sel_sql = "SELECT * FROM tb_mainperson WHERE CompanyGUID='" + CompanyGUID + "' and PersonName='"+PersonName+"'"
    cursor.execute(sel_sql)  # 执行sql语句
    row = cursor.fetchone()  # 读取查询结果,
    if not row:
        createDateTime = datetime.datetime.now()
        try:
            # file_path 网络地址 ，filename 文件名
            cursor.execute("""INSERT INTO tb_mainperson(CompanyGUID,PersonName,JobName)
                                        VALUES (%s,%s,%s)""",
                           (
                               CompanyGUID,
                               PersonName,
                               JobName
                           ))
            conn.commit()
        except Exception as e:
            logging.info(e)
            # 发生错误时回滚
            conn.rollback()
    else:
        try:
            pass
        except Exception as e:
            logging.info(e)


def inputTaxcreditTB(item,cursor,conn):
    CompanyGUID = str(item['CompanyGUID'])
    EvaluationDate = item['EvaluationDate']
    CreditLevel = item['CreditLevel']
    CreditLevelType = item['CreditLevelType']
    TaxpayerIdentificationNumber = item['TaxpayerIdentificationNumber']
    EvaluationDepartment = item['EvaluationDepartment']
    sel_sql = "SELECT * FROM tb_taxcreditlevel WHERE EvaluationDate='" + EvaluationDate + "' and TaxpayerIdentificationNumber='"+TaxpayerIdentificationNumber+"'"
    cursor.execute(sel_sql)  # 执行sql语句
    row = cursor.fetchone()  # 读取查询结果,
    if not row:
        createDateTime = datetime.datetime.now()
        try:
            # file_path 网络地址 ，filename 文件名
            cursor.execute("""INSERT INTO tb_taxcreditlevel(CompanyGUID,EvaluationDate,CreditLevel,CreditLevelType,TaxpayerIdentificationNumber,EvaluationDepartment)
                                        VALUES (%s,%s,%s,%s,%s,%s)""",
                           (
                               CompanyGUID,
                               EvaluationDate,
                               CreditLevel,
                               CreditLevelType,
                               TaxpayerIdentificationNumber,
                               EvaluationDepartment
                           ))
            conn.commit()
        except Exception as e:
            logging.info(e)
            # 发生错误时回滚
            conn.rollback()




def inputChangeinfoTB(item,cursor,conn):
    CompanyGUID = str(item['CompanyGUID'])
    ChangeDate = item['ChangeDate']
    ChangeContent = item['ChangeContent']
    BeforeChange = item['BeforeChange']
    AfterChange = item['AfterChange']
    sel_sql = "SELECT * FROM tb_changelog WHERE CompanyGUID='" + CompanyGUID + "' and ChangeDate='"+ChangeDate+"' and ChangeContent='"+ChangeContent+"' and BeforeChange = '"+BeforeChange+"'"
    cursor.execute(sel_sql)  # 执行sql语句
    row = cursor.fetchone()  # 读取查询结果,
    if not row:
        createDateTime = datetime.datetime.now()
        try:
            # file_path 网络地址 ，filename 文件名
            cursor.execute("""INSERT INTO tb_changelog(CompanyGUID,ChangeDate,ChangeContent,BeforeChange,AfterChange)
                                        VALUES (%s,%s,%s,%s,%s)""",
                           (
                               CompanyGUID,
                               ChangeDate,
                               ChangeContent,
                               BeforeChange,
                               AfterChange
                           ))
            conn.commit()
        except Exception as e:
            logging.info(e)
            # 发生错误时回滚
            conn.rollback()
    else:
        try:
            pass
        except Exception as e:
            logging.info(e)

def inputJingPinTB(item,cursor,conn):
    CompanyGUID = str(item['CompanyGUID'])
    Product = item['Product']
    CurrentFinancingRound = item['CurrentFinancingRound']
    EstablishDate = item['EstablishDate']
    Area = item['Area']
    Business = item['Business']
    Industry = item['Industry']
    sel_sql = "SELECT * FROM tb_competingproduct WHERE CompanyGUID='" + CompanyGUID + "' and Product='"+Product+"'"
    cursor.execute(sel_sql)  # 执行sql语句
    row = cursor.fetchone()  # 读取查询结果,
    if not row:
        createDateTime = datetime.datetime.now()
        try:
            # file_path 网络地址 ，filename 文件名
            cursor.execute("""INSERT INTO tb_competingproduct(CompanyGUID,Product,CurrentFinancingRound,EstablishDate,Area,Business,Industry)
                                        VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                           (
                               CompanyGUID,
                               Product,
                               CurrentFinancingRound,
                               EstablishDate,
                               Area,
                               Business,
                               Industry
                           ))
            conn.commit()
        except Exception as e:
            logging.info(e)
            # 发生错误时回滚
            conn.rollback()
    else:
        try:
            pass
        except Exception as e:
            logging.info(e)



def inputBranchTB(item,cursor,conn):
    CompanyGUID = str(item['CompanyGUID'])
    CorpName = item['CorpName']
    CorpManager = item['CorpManager']
    EstablishDate = item['EstablishDate']
    State = item['State']
    sel_sql = "SELECT * FROM tb_branch WHERE CompanyGUID='" + CompanyGUID + "' and CorpName='"+CorpName+"'"
    cursor.execute(sel_sql)  # 执行sql语句
    row = cursor.fetchone()  # 读取查询结果,
    if not row:
        createDateTime = datetime.datetime.now()
        try:
            # file_path 网络地址 ，filename 文件名
            cursor.execute("""INSERT INTO tb_branch(CompanyGUID,CorpName,CorpManager,EstablishDate,State)
                                        VALUES (%s,%s,%s,%s,%s)""",
                           (
                               CompanyGUID,
                               CorpName,
                               CorpManager,
                               EstablishDate,
                               State,
                           ))
            conn.commit()
        except Exception as e:
            logging.info(e)
            # 发生错误时回滚
            conn.rollback()
    else:
        try:
            pass
        except Exception as e:
            logging.info(e)



def inputInvestTB(item,cursor,conn):
    CompanyGUID = str(item['CompanyGUID'])
    InvestToCompany = item['InvestToCompany']
    InvestToCompanyManager = item['InvestToCompanyManager']
    InvestPercent = item['InvestPercent']
    RegisteredCapital = item['RegisteredCapital']
    EstablishDate = item['EstablishDate']
    sel_sql = "SELECT * FROM tb_invest WHERE CompanyGUID='" + CompanyGUID + "' and InvestToCompany='"+InvestToCompany+"'"
    cursor.execute(sel_sql)  # 执行sql语句
    row = cursor.fetchone()  # 读取查询结果,
    if not row:
        createDateTime = datetime.datetime.now()
        try:
            cursor.execute("""INSERT INTO tb_invest(CompanyGUID,InvestToCompany,InvestToCompanyManager,InvestPercent,RegisteredCapital,EstablishDate)
                                        VALUES (%s,%s,%s,%s,%s,%s)""",
                           (
                               CompanyGUID,
                               InvestToCompany,
                               InvestToCompanyManager,
                               InvestPercent,
                               RegisteredCapital,
                               EstablishDate,
                           ))
            conn.commit()
        except Exception as e:
            logging.info(e)
            # 发生错误时回滚
            conn.rollback()
    else:
        try:
            pass
        except Exception as e:
            logging.info(e)


def inputRongZiTB(item,cursor,conn):
    CompanyGUID = str(item['CompanyGUID'])
    DisclosureDate = item['DisclosureDate']
    FinancingRaund = item['FinancingRaund']
    TransactionAmount = item['TransactionAmount']
    Investor = item['Investor']
    sel_sql = "SELECT * FROM tb_financinghistory WHERE CompanyGUID='" + CompanyGUID + "' and DisclosureDate='"+DisclosureDate+"'"
    cursor.execute(sel_sql)  # 执行sql语句
    row = cursor.fetchone()  # 读取查询结果,
    if not row:
        createDateTime = datetime.datetime.now()
        try:
            cursor.execute("""INSERT INTO tb_financinghistory(CompanyGUID,DisclosureDate,FinancingRaund,TransactionAmount,Investor)
                                        VALUES (%s,%s,%s,%s,%s)""",
                           (
                               CompanyGUID,
                               DisclosureDate,
                               FinancingRaund,
                               TransactionAmount,
                               Investor
                           ))
            conn.commit()
        except Exception as e:
            logging.info(e)
            # 发生错误时回滚
            conn.rollback()
    else:
        try:
            pass
        except Exception as e:
            logging.info(e)