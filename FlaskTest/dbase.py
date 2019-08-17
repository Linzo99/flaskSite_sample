import sqlite3

def dbconnector():
	base = sqlite3.connect('users.db')
	cur = base.cursor()

	return cur, base