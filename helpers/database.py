import psycopg2
import guihelper as guihelper
import os
import sys

params = []

def connect(config):

        try:
            conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (config[0], config[1], config[2], config[3]))
            return True

        except:
            return False

def view(table):

    try:
        # VIEW A TABLE
        params = guihelper.getConfig()
        conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (params[0], params[1], params[2], params[3]))
        cur = conn.cursor()
        cur.execute('SELECT * FROM '+ table + ' FETCH FIRST 10 ROW ONLY')
        all = cur.fetchall()
        guihelper.setData(all)

        output = f'Success.  Table "{table}" exists'
        return output

    except:
        err = 'Error.  Table or View does not exist.'
        return err

def viewrange(table, pointer):

    try:
        # VIEW A TABLE
        params = guihelper.getConfig()

        conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (params[0], params[1], params[2], params[3]))
        cur = conn.cursor()
        cur.execute('SELECT * FROM '+ table + ' OFFSET ' + str(pointer) + ' FETCH FIRST 10 ROW ONLY')
        all = cur.fetchall()
        print(all)
        guihelper.setData(all)

    except:
        err = 'Error fetching query.'
        return err
# def delete(name, conn, cur):
#         try:
#                 # DELETE A TABLE 
#                 cur.execute('DROP TABLE ' + name)
#                 conn.commit()
#         except:
#                 print('Database Error: ')

# def createtable(name, conn, cur):
#         try:

#                 # CREATE A TABLE 
#                 cur.execute("""
#                 CREATE TABLE """ + name + """(
#                 TRIPID integer PRIMARY KEY,
#                 PICKUPTIME timestamp,
#                 DROPOFFTIME timestamp,
#                 PICKUPZONE smallint,
#                 DROPOFFZONE smallint)""")
#                 conn.commit()
#         except:
#                 print('Databse Error: ')

# def insert(file, conn, cur, header=True, tablename=''):
#         try:
#                         # INSERT CSV INTO Table
#                 with open(file, 'r') as f:            
#                         if header: next(f)
#                         cur.copy_from(f, tablename, sep = ',')
#                         conn.commit()
#         except:
#                 print('Database Error: ')
