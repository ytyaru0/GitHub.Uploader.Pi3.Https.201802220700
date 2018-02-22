#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import os.path
import setting.Setting

# 抽象クラス
class DbInitializer(metaclass=ABCMeta):
    def __init__(self):
        self.__path_dir_root = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
        self.__setting = setting.Setting.Setting()
        self.__path_dir_this = os.path.abspath(os.path.dirname(__file__))
#        self.__path_dir_db = self.__setting.DbPath
        self.__db = None

    def Initialize(self):
        db = None
        print(self.DbId)
        print(self.DbFileName)
#        if not os.path.isfile(self.__files[dbname]):
        if os.path.isfile(self.DbFilePath):
            db = dataset.connect('sqlite:///' + self.DbFilePath)
        else:
            # 空ファイル作成
            with open(self.DbFilePath, 'w') as f: pass
            # DB接続
            db = dataset.connect('sqlite:///' + self.DbFilePath)
            db.query('PRAGMA foreign_keys = false')
            # テーブル作成（CreateTable文）
            for path_sql in self.__GetCreateTableSqlFilePaths():
                self.__ExecuteSqlFile(dbname, path_sql)
            # 初期値の挿入（Insert文）
            for path_tsv in self.__GetInsertTsvFilePaths():
                table_name = os.path.splitext(table_name)[0]
                loader = database.TsvLoader.TsvLoader()
                loader.ToSqlite3(path_tsv, self.DbFilePath, table_name)
            db.query('PRAGMA foreign_keys = true')
        return db

    #@abstractmethod
    def CreateDb(self):
        if not os.path.isfile(self.DbFilePath):
            with open(self.DbFilePath, 'w') as f: pass

    def ConnectDb(self):
        self.__class__.Db = dataset.connect('sqlite:///' + self.DbFilePath)

    #@abstractmethod
    def CreateTable(self):
        db.query('PRAGMA foreign_keys = false')
        # テーブル作成（CreateTable文）
        for path_sql in self.__GetCreateTableSqlFilePaths():
            self.__ExecuteSqlFile(dbname, path_sql)

    #@abstractmethod
    def InsertInitData(self): pass
        # 初期値の挿入（Insert文）
        for path_tsv in self.__GetInsertTsvFilePaths():
            table_name = os.path.splitext(table_name)[0]
            loader = database.TsvLoader.TsvLoader()
            loader.ToSqlite3(path_tsv, self.DbFilePath, table_name)
        db.query('PRAGMA foreign_keys = true')


    
    @property
    def DbId(self): return self.__class__.__name__.replace(super().__thisclass__.__name__, '')
    @property
    def DbFileName(self): return 'GitHub.' + self.DbId + '.sqlite3'
    @property
    def DbFilePath(self): return os.path.join(self.__setting.DbPath, self.DbFileName)

    # パス取得（テーブル作成用SQLファイル）
    def __GetCreateTableSqlFilePaths(self):
        path = os.path.join(self.__path_dir_this, self.DbId, 'sql', 'create')
        for path_sql in glob.glob(os.path.join(path + '*.sql')): yield path_sql

    # パス取得（初期値挿入用TSVファイル）
    def __GetInsertTsvFilePaths(self, dbname):
        path = os.path.join(self.__path_dir_this, self.DbId, 'tsv')
        for path_tsv in glob.glob(os.path.join(path + '*.tsv')): yield path_tsv

    # SQLファイル発行
    def __ExecuteSqlFile(self, dbname, sql_path):
        with open(sql_path, 'r') as f:
            sql = f.read()
            self.__dbs[dbname].query(sql)
    """
    # パス取得（テーブル作成用SQLファイル）
    def __GetCreateTableSqlFilePaths(self, dbname):
        path = os.path.join(self.__path_dir_this, dbname, 'sql', 'create')
        for path_sql in glob.glob(os.path.join(path + '*.sql')): yield path_sql

    # パス取得（初期値挿入用TSVファイル）
    def __GetInsertTsvFilePaths(self, dbname):
        path = os.path.join(self.__path_dir_this, dbname, 'tsv')
        for path_tsv in glob.glob(os.path.join(path + '*.tsv')): yield path_tsv
        return self.__dbs[dbname]

    # SQLファイル発行
    def __ExecuteSqlFile(self, dbname, sql_path):
        with open(sql_path, 'r') as f:
            sql = f.read()
            self.__dbs[dbname].query(sql)
    """

