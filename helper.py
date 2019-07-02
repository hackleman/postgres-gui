import connect as postgres
import os
import sys

config = []

def connectionTest(self):

    if (len(config) == 0):
        err = 'No connection string specified.  Please configure your connection'
        self.connectionstr.set(err)
        return False

    if (postgres.connect(config)):
        success = 'Connection Successful'
        self.connectionstr.set(success)
        return True
    else:
        fail = 'Connection failed.  Try configuring env variables'
        self.connectionstr.set(fail)
        return False

def setdefaultconfig(self):

    global config

    dbname = 'postgres'
    user = 'postgres'
    pwd = '1234'
    host = 'localhost'

    config = [host, dbname, user, pwd]

def getConfig(self):

    global config

    dbname = self.dbname.get('1.0', 'end-1c')
    user = self.user.get('1.0', 'end-1c')
    pwd = self.password.get('1.0', 'end-1c')
    host = self.host.get('1.0', 'end-1c')

    config = [host, dbname, user, pwd]
    connectionTest(self)

def getTable(self, textbox):
    
    table = textbox.get('1.0', 'end-1c')
    output = postgres.view(table)
    self.console.set(output)


def getName(textbox):

    table = textbox.get('1.0', 'end-1c')
    print(table)
