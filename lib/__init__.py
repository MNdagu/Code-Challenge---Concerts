import sqlite3

CONN = sqlite3.connect('concerts.db')
CURSOR = CONN.cursor()