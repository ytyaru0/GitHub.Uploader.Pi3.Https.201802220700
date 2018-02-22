#!python3
#encoding:utf-8
import os.path
import configparser
import shlex
import subprocess
import dataset
from web.service.github.api.v3.authentication.BasicAuthentication import BasicAuthentication
from web.service.github.api.v3.authentication.TwoFactorAuthentication import TwoFactorAuthentication
from web.service.github.api.v3.authentication.OAuthAuthentication import OAuthAuthentication
import web.service.github.api.v3.Client
"""
import database.language.Main
import database.api.Main
import database.gnu_license.create.Main
import database.gnu_license.Main
import database.license.Main
import database.account.Main
import database.repo.insert.command.repositories.Inserter
"""
import web.log.Log
import setting.Setting
import glob

import database.init.DbInitializer import DbInitializer
import database.init.ApisDbInitializer import ApisDbInitializer
import database.init.GnuLicensesDbInitializer import GnuLicensesDbInitializer

class DatabaseMeta(type):
    def __new__(cls, name, bases, attrs):
        for initer in [ApisDbInitializer(), GnuLicensesDbInitializer()]
            initer.CreateDb()
            initer.ConnectDb()
            initer.CreateTable()
            initer.InsertInitData()
            attrs[initer.DbId] = property(lambda : initer)
            #self[initer.DbId] = initer # プロパティにしたいが方法不明。これは属性値になってしまう
            #self.__dbs[initer.DbId] = initer # Db, DbFilePathなどが得られる
            # https://www.python-izm.com/advanced/property/
            #property(get_url, set_url, del_url, 'url Property')
            #property(lambda self x: x+1)
        return type.__new__(cls, name, bases, attrs)

