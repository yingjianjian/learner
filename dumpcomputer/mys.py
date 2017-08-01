#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import MySQLdb
import os
import getpass
os.system('clear')
class Database:
    def __init__(self):
            self.conn= MySQLdb.connect(
            host='127.0.0.1',
            port = 3306,
            user='root',
            passwd='root',
            db ='haha',
            charset='utf8',)
            self.user_list = []
	    self.user_login=[]
    def get_mysql_user(self):

        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM user")
            rows = cur.fetchall()
            dict_uid = dict()
            for row in rows:
		self.user_list.append((str(row['id']),row["ip"],row["hostname"],row["author"],row["name"],row["loginpass"]))
            return self.user_list

a= Database()
w=a.get_mysql_user()
c=1
d2=[]
while c<len(w):
	i=c-1
	d='\t'.join(w[i])
	d1=d.split()
	c+=1
	d2.append(d1)
while True:
	try:
		louser=raw_input("please login system's user:")
	except EOFError:
		print ''
		print 'exit success'
		sys.exit(0)
	p=0
	l=len(d2)
	try:
		while p<=l:
			if louser==d2[p][3]:
				loginpass= d2[p][5]
				break
			p=p+1
		break
	except IndexError:
		print 'input error'
		continue
lopass=getpass.getpass("please login %s's password:" %(louser))
if lopass==loginpass:
	c=1
	print '''\033[32;1mWelcome to the Connecting System!\033[0m
	Choose the Server to connect:
	'''
	print '='*87
	while c<len(w):
		i=c-1
		d='\t'.join(w[i])
		d1=d.split()
		c+=1
		print '%-20s%-20s%-20s%-20s%s'%(d1[0],d1[1],d1[2],d1[3],d1[4])
	print '='*87
	print ''
	try:
		choice = raw_input('Your choice:')
	except EOFError:
		print ''
		print 'exit success'
		sys.exit(0)
	p=0
	while p<=l:
		if choice==d2[p][0]:
			address=d2[p][1]
			hostname=d2[p][2]
		#	author=d2[p][3]
			break
		p=p+1
	try:
		conn = MySQLdb.connect(host = '127.0.0.1', user = 'root',passwd = 'root', db = 'haha', port = 3306)
        	cur = conn.cursor()
        	cur.execute("select * from loginuser where ip = '%s'" % address)
        	qur_result = cur.fetchall()
        	for record in qur_result:
			record=list(record)
                	if record[0] == address:
                        	username = record[1]
                        	password = record[2]
        	cur.close()
        	conn.close()
	except MySQLdb.Error,e:
        	print 'Mysql Error Msg:',e
	cmd = 'python /tmp/paramiko-1.7.7.1/demos1/demo.py %s %s %s %s' %(hostname,username,password,louser)
	os.system(cmd)
else:
	print 'user or pass is error'
