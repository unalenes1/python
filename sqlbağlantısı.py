# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 14:45:54 2019

@author: Casper
"""
#import edilmesi gereken kütüphaneler
import mysql.connector
import sqlite3

#sql bağlantısı 
mydb = mysql.connector.connect(
        host= 'localhost',
        database= 'betik',
        user= 'enes',
        password= 'asd002'
    )
mycursor= mydb.cursor()
mycursor.execute('SELECT * FROM kullanici')
kullanici = mycursor.fetchall()
for i in kullanici:
    print("Kullanıcı Adı : "+i[1]+" === "+" Kullanıcı Puanı : "+str(i[3]))