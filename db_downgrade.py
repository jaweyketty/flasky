#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-29 16:53:27
# @Author  : jaweyhuang (jaweyhuang@sina.com)
# @Link    : ${link}
# @Version : $Id$

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, v - 1)
print 'Current database version: ' + str(api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO))
