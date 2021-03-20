# !/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import datetime
import pymysql
import pandas as pd

from sqlalchemy import create_engine
import pymysql
import pandas as pd
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import datetime

engine_jsMons = create_engine('mysql+pymysql://root:123456@localhost:3306/JS_Mons')
# 查询语句，选出employee表中的所有数据 "JS225_JS400"

sql_sp_LJ = 'select id,J7747,J7741,J7733,J7731,J7729,J7717,J7701,J4902,J4543,LastTime from  sp_LJ_400  ; '

ln = os.getcwd()


def savedt():

    df_js225 = pd.read_sql_query(sql_sp_LJ, engine_jsMons)

    excelFile3 = '{0}/{1}.xlsx'.format(ln, "Precision_mechanical_equipment")  # 处理了文件属于当前目录下！
    df_js225.to_excel(excelFile3)



if __name__ == '__main__':
    savedt()

