import sqlite3
import time
import datetime
def OnlineUserDatabase(data):
	conn = sqlite3.connect('302python.db')
	c = conn.cursor()
	clear = 'DELETE FROM OnlineUsers'
	c.execute(clear)
	for x in range(len(data)):
		username = data[str(x)]['username']
		ip = data[str(x)]['ip']
		port = data[str(x)]['port']
		location = data[str(x)]['location']
		lastLogin = datetime.datetime.fromtimestamp(
		int(data[str(x)]['lastLogin'])
		).strftime('%Y-%m-%d %H:%M:%S')
		c.execute('INSERT INTO OnlineUsers VALUES(?, ?, ?, ?, ?)',
		(username, ip, location, port, lastLogin))
	conn.commit()
	conn.close()

def MessageDatabase(currentTime, sender, message, receicer):
	conn = sqlite3.connect('302python.db')
	c = conn.cursor()
	c.execute('INSERT INTO Message VALUES(?, ?, ?, ?)',
	(currentTime, sender, message, receicer))
	conn.commit()
	conn.close()

def ReceiveFileDatabase(time, sender, filename, content_type):
	conn = sqlite3.connect('302python.db')
	c = conn.cursor()
	c.execute('INSERT INTO FileReceived VALUES(?, ?, ?, ?)',
	(time, sender, filename, content_type))
	conn.commit()
	conn.close()
	
	
def findIp(username):
	conn = sqlite3.connect('302python.db')
	c = conn.cursor()
	c.execute('SELECT ip FROM OnlineUsers WHERE username=?',(username,))
	ip=c.fetchone()
	return ip[0]
	
def findPort(username):
	conn = sqlite3.connect('302python.db')
	c = conn.cursor()
	c.execute('SELECT port FROM OnlineUsers WHERE username=?',(username,))
	port=c.fetchone()
	return port[0]