# -*- coding: utf-8 -*-
# MySQLdbのインポート
import MySQLdb
import os
import subprocess
 

class ConnectDB():

  def __init__(self):
    self.connection = MySQLdb.connect(
        host='localhost',
        user='root',
        db='sudokunet_development')
    self.cursor = self.connection.cursor()
 
  def execute(self,sql_command):
    print(sql_command)
    self.cursor.execute(sql_command)
    self.rows = self.cursor.fetchall()
    self.connection.commit()
    

  def get_data(self):
    return self.rows

  def display(self):
    print("a")
    for row in self.rows:
      print (row)

  def close(self):
    self.connection.close()
