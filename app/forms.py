#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-29 14:52:36
# @Author  : jaweyhuang (jaweyhuang@sina.com)
# @Link    : ${link}
# @Version : $Id$

from flask_wtf import FlaskForm as Form
from wtforms import StringField, BooleanField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from app.models import User

class LoginForm(Form):
    username    = StringField(u'用户名', validators=[DataRequired()])
    password    = PasswordField(u'密码', validators=[DataRequired(), Length(6, 18, message=u'密码长度在6到18位')])
    submit      = SubmitField(u'登录')
    remember    = BooleanField(u'记住我', default=False)

    def validate(self):
        """Validator for check the account information."""
        check_validata = super(LoginForm, self).validate()

        # If validator no pass
        if not check_validata:
            return False

        # Check the user whether exist.
        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            self.username.errors.append(u'无效的用户名或密码错误.')
            return False

        # Check the password whether right.
        if not user.check_password(self.password.data):
            self.password.errors.append(u'无效的用户名或密码错误.')
            return False

        return True


class EditForm(Form):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])

    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not Form.validate(self):
            return False

        if self.nickname.data == self.original_nickname:
            return True

        user = User.query.filter_by(nickname=self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True

class PostForm(Form):
    post = StringField('post', validators=[DataRequired()])

class SearchForm(Form):
    search = StringField('search', validators=[DataRequired()])