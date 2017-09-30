#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-29 14:51:01
# @Author  : jaweyhuang (jaweyhuang@sina.com)
# @Link    : ${link}
# @Version : $Id$

import os

CSRF_ENABLED = True
SECRET_KEY = '123456s3cr3t'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]


basedir = os.path.abspath(os.path.dirname(__file__))
logfile = os.path.join(basedir, 'logs/flask.log')

#创建数据库连接,MySQLdb连接方式
#mysql_db = create_engine('mysql://用户名:密码@ip:port/dbname')
#创建数据库连接，使用mysql-connector-python连接方式
#mysql_db = create_engine("mysql+mysqlconnector://用户名:密码@ip:port/dbname")
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://hw:123456@127.0.0.1:3306/db_flask?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# pagination
POSTS_PER_PAGE = 3

WHOOSH_BASE = os.path.join(basedir, 'tmp/whoosh_index')
WHOOSH_ENABLE = True
MAX_SEARCH_RESULTS = 50
