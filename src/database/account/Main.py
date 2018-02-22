#!python3
#encoding:utf-8
import sys
import subprocess
import shlex
import os.path
import getpass
import dataset
import database.TsvLoader
import setting.Setting

class Main:
    def __init__(self, db_path):
        self.__db_path = db_path
        self.__path_this_dir = os.path.abspath(os.path.dirname(__file__))
        #self.__setting = setting.Setting.Setting()

    def Run(self):
        self.__ConnectDb()
        # Create文
        for filename in ['Accounts','TwoFactors','AccessTokens','SshKeys']:
            path = os.path.join(self.__path_this_dir, 'res/sql/create/{0}.sh'.format(filename))
            self.__ExecuteSqlFile(path)
        # Insert文
        self.__Insert()
#        self.__Check() # Check.shで正常に文字列結合できずパスを作成できない。
 
    # 2018-02-20 dataset.database.query(SQL)で実行するよう改修（sqlite3コマンド不要化）
    def __Create(self):
        self.__CreateBlankFile()
        for filename in ['Accounts','TwoFactors','AccessTokens','SshKeys']:
            path = os.path.join(self.__path_this_dir, 'res/sql/create/{0}.sh'.format(filename))
            self.__ExecuteSqlFile(path)
            
    # DBファイルが無いなら空ファイル作成
    def __CreateBlankFile(self):
        if not os.path.isfile(self.__db_path):
            with open(self.__db_path, 'w') as f: pass

    def __ExecuteSqlFile(self, sql_path):
        with open(path, 'r') as f:
            sql = f.read()
            db = dataset.connect('sqlite:///' + self.__db_path)
            db.query(sql)

        # sqlite3 "${PATH_DB}" < ${PATH_SCRIPT}/Accounts.sql
#        if not os.path.isfile(os.path.join(self.__setting['Path']['DB'], )):
           
    # DBファイル生成＆接続
    def __ConnectDb(self):
        if not os.path.isfile(self.__db_path):
            with open(self.__db_path, 'w') as f: pass
        self.__db = dataset.connect('sqlite:///' + self.__db_path)

    # SQLファイル発行
    def __ExecuteSqlFile(self, sql_path):
        with open(sql_path, 'r') as f:
            sql = f.read()
            self.__db.query(sql)

    # 初期値の挿入
    def __Insert(self):
        tables = ['Accounts', 'TwoFactors', 'AccessTokens']
        for table in tables:
#            path_tsv = os.path.join(self.__path_this_dir, "res/tsv/{0}.tsv".format(table))
            path_tsv = os.path.join(self.__path_this_dir, "res/tsv/meta_{0}.tsv".format(table))
            loader = database.TsvLoader.TsvLoader()
            loader.ToSqlite3(path_tsv, self.__db_path, table)


    """
    def Run____(self):
        self.__Create()
        self.__Insert()
#        self.__Check() # Check.shで正常に文字列結合できずパスを作成できない。

    def Create(self):
        self.__Create()

    def __CreateSh(self):
        subprocess.call(shlex.split("bash \"{0}\" \"{1}\"".format(os.path.join(self.__path_this_dir, "CreateTable.sh"), self.__db_path)))

    def __InsertSh(self):
        tables = ['Accounts', 'TwoFactors', 'AccessTokens']
        for table in tables:
#            path_tsv = os.path.join(self.__path_this_dir, "res/tsv/{0}.tsv".format(table))
            path_tsv = os.path.join(self.__path_this_dir, "res/tsv/meta_{0}.tsv".format(table))
            loader = database.TsvLoader.TsvLoader()
            loader.ToSqlite3(path_tsv, self.__db_path, table)

    def __CheckSh(self):
        subprocess.call(shlex.split("bash \"{0}\" \"{1}\"".format(os.path.join(self.__path_this_dir, "Check.sh"), self.__db_path)))
    """

