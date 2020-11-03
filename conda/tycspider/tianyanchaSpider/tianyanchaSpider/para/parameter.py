from os import path
import os
import configparser
import tianyanchaSpider.tools.tools
from urllib.parse import quote
config = configparser.ConfigParser()
    # 获取当前目录
d = path.dirname(__file__)
    # 获取当前目录的父级目录
parent_path = os.path.dirname(d)
logs_path = os.path.dirname(parent_path)
import pymysql
config = configparser.ConfigParser()
        # 获取当前目录
d = path.dirname(__file__)
config.read(d + "/../config/config.ini")
        # 初始化数据库连接
db_host = config.get("db", "host")
db_port = config.get("db", "port")
db_user = config.get("db", "user")
db_password = config.get("db", "password")
db_name = config.get("db", "dbname")
class Parameter():
    def __init__(self):
        pass

    def get_tianyan_para(self):
        companies = tianyanchaSpider.tools.tools.getExecleData(d + "/../gaoqimingdan.xlsx")
        url = "https://www.tianyancha.com/search?key="
        new_urls=[]
        #数据库查询书否存在
        conn = pymysql.connect(user=db_user, passwd=db_password, db=db_name, host=db_host, port=int(db_port),
                               charset="utf8", use_unicode=True)
        cursor = conn.cursor()
        sel_sql = "SELECT CompanyName FROM tb_companyinfo"
        cursor.execute(sel_sql)  # 执行sql语句
        result = cursor.fetchall()
        for row in result:
            cn = row[0]
            if cn in companies:
                companies.remove(cn)
        for company_name in companies:
            cname = quote(company_name)
            new_url = str(url + (cname))
            new_urls.append(new_url)
        return new_urls,companies


    def get_tianyancha_detail(self):
        conn = pymysql.connect(user=db_user, passwd=db_password, db=db_name, host=db_host, port=int(db_port),
                               charset="utf8", use_unicode=True)
        cursor = conn.cursor()
        sel_sql = "SELECT * FROM tb_companyinfo"
        cursor.execute(sel_sql)  # 执行sql语句
        result = cursor.fetchall()
        companyGUIDs =[]
        companyDetailURLs = []
        for row in result:
            if not row[5]:
                companyGUIDs.append(row[0])
                companyDetailURLs.append(row[24])

        cursor.close()
        conn.close()
        return companyGUIDs,companyDetailURLs




