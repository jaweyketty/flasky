#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from config import basedir
from config import logfile
from datetime import date,timedelta

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

lm = LoginManager()
lm.session_protection = "strong"
# Flask-Login 那个视图允许用户登录设置
lm.login_view = "login"
lm.login_message = u"请登录！"
lm.login_message_category = "info"
lm.remember_cookie_duration = timedelta(days=1)
lm.init_app(app)

from app import views, models

import logging
from logging.handlers import RotatingFileHandler
file_handler = RotatingFileHandler(logfile, 'a', 1 * 1024 * 1024, 10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
app.logger.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.info('blog startup')