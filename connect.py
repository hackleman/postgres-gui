import psycopg2
import os
import sys

def connect(config):

        try:
            conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (config[0], config[1], config[2], config[3]))
            return True

        except:
            return False

def view(table):

    try:
        # VIEW A TABLE
        conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=1234")
        cur = conn.cursor()
        cur.execute('SELECT * FROM '+ table)
        # all = cur.fetchall()
        output = f'Success.  Table "{table}" exists'
        return output

    except:
        err = 'Error.  Table or View does not exist.'
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
