# -*- coding: utf-8 -*-
# !D:/Code/python
# -*- coding: utf-8 -*-
# @Time : 2020/6/13 17:58
# @Author : Wilson
# @Site :
# @File : pipelines.py
# @Software: PyCharm
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import configparser
import logging
import datetime
import tianyanchaSpider.tools.dbUtils
from os import path

config = configparser.ConfigParser()
# 获取当前目录
d = path.dirname(__file__)
config.read(d + "/config/config.ini")
# 初始化数据库连接
db_host = config.get("db", "host")
db_port = config.get("db", "port")
db_user = config.get("db", "user")
db_password = config.get("db", "password")
db_name = config.get("db", "dbname")


class TianyanchaspiderPipeline(object):
    def process_item(self, item, spider):
        try:
            conn = pymysql.connect(user=db_user, passwd=db_password, db=db_name, host=db_host, port=int(db_port),
                                 charset="utf8", use_unicode=True)
            # conn = pymssql.connect(host=db_host, port=db_port, user=db_user, password=db_password, database=db_name,
            #                        charset='utf8', autocommit=True)
            cursor = conn.cursor()
            ItemType = '-'
            if len(item)>2:
                ItemType =item['ItemType']

            # basicType 公司基本信息
            if "basicType"== ItemType:
                tianyanchaSpider.tools.dbUtils.updateCompanyInfostTB(item, cursor, conn)

            if "companyinfo"== ItemType:
                tianyanchaSpider.tools.dbUtils.inputCompanyInfostTB(item, cursor, conn)
            if "copyrightType"== ItemType:
                tianyanchaSpider.tools.dbUtils.inputCopyrightTB(item, cursor, conn)
            if "patenType"== ItemType:
                tianyanchaSpider.tools.dbUtils.inputPatenTB(item, cursor, conn)
            if "staffType"== ItemType:
                tianyanchaSpider.tools.dbUtils.inputStaffTB(item, cursor, conn)

            if "taxcredit"== ItemType:
                tianyanchaSpider.tools.dbUtils.inputTaxcreditTB(item, cursor, conn)
            if "changeinfo"== ItemType:
                tianyanchaSpider.tools.dbUtils.inputChangeinfoTB(item, cursor, conn)
                # print('changeinfo---',item)
            if "jingpin"== ItemType:
                tianyanchaSpider.tools.dbUtils.inputJingPinTB(item, cursor, conn)

            if "branch"== ItemType:
                tianyanchaSpider.tools.dbUtils.inputBranchTB(item, cursor, conn)

            if "invest"== ItemType:
                tianyanchaSpider.tools.dbUtils.inputInvestTB(item, cursor, conn)

            if "touzi"== ItemType:
                tianyanchaSpider.tools.dbUtils.inputTouZiTB(item, cursor, conn)
            # 融资
            if "rongzi"== ItemType:
                tianyanchaSpider.tools.dbUtils.inputRongZiTB(item, cursor, conn)
        except Exception as e:
            logging.info(e)

        return item
