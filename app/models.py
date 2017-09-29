#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-29 16:20:44
# @Author  : jaweyhuang (jaweyhuang@sina.com)
# @Link    : ${link}
# @Version : $Id$

from app import db
from hashlib import md5

followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


class Post(db.Model):
    id        = db.Column(db.Integer, primary_key = True)
    body      = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id   = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)

class User(db.Model):
    id        = db.Column(db.Integer, primary_key = True)
    nickname  = db.Column(db.String(64), unique = True)
    email     = db.Column(db.String(120), unique = True)
    posts     = db.relationship('Post', backref = 'author', lazy = 'dynamic')
    about_me  = db.Column(db.String(512))
    last_seen = db.Column(db.DateTime)
    followed = db.relationship('User', 
        secondary = followers, 
        primaryjoin = (followers.c.follower_id == id), 
        secondaryjoin = (followers.c.followed_id == id), 
        backref = db.backref('followers', lazy = 'dynamic'), 
        lazy = 'dynamic')

    # 只返回 True，除非表示用户的对象因为某些原因不允许被认证
    def is_authenticated(self):
        return True

    # 返回 True，除非是用户是无效的，比如因为他们的账号是被禁止。
    def is_active(self):
        return True

    # 返回 True，除非是伪造的用户不允许登录系统
    def is_anonymous(self):
        return False

    # 返回一个用户唯一的标识符，以 unicode 格式。使用数据库生成的唯一的 id
    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/' + md5(self.email).hexdigest() + '?d=mm&s=' + str(size)

    @staticmethod
    def make_unique_nickname(nickname):
        if User.query.filter_by(nickname = nickname).first() == None:
            return nickname
        version = 2
        while True:
            new_nickname = nickname + str(version)
            if User.query.filter_by(nickname = new_nickname).first() == None:
                break
            version += 1
        return new_nickname

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
            return self

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)
            return self

    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        return Post.query.join(followers, (followers.c.followed_id == Post.user_id)).filter(followers.c.follower_id == self.id).order_by(Post.timestamp.desc())

    def __repr__(self):
        return '<User %r>' % (self.nickname)
