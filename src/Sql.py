#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Copyright (C) 2010 by Will Kamp <manimaul!gmail.com>

import sqlite3 as sql
import time

def CreateEmptyDiveDB(filename):
    conn = sql.connect(filename)
    curs = conn.cursor()
    
    sqlfile = open('DiveRT_Template.sql', 'r')
    sqldat = sqlfile.read()
    sqlfile.close()
                
    curs.executescript(sqldat)
    conn.commit()
    
    curs.close()

class DataStore:
    def __init__(self, filename):
        #print 'sql opening datastore: ', filename
        self.conn = sql.connect(filename)
        self.curs = self.conn.cursor()
        
    def GetLastCleanupRound(self):
        self.curs.execute('select max(cleanupNumber) from dives')
        r = self.curs.fetchall()[0][0]
        if r is None:
            r = 1
        return int(r)
        
    def GetCleanupSQLData(self, num):
        num = str(num)
        t = (num,)
        self.curs.execute('select * from dives where cleanupNumber=?', t)
        lst = self.curs.fetchall()
        r = []
        for each in lst:
            r.append(each)
        return r
    
    def GetDiverDateSQLData(self, diver, date, cleanupNumber):
        val = (diver, date, cleanupNumber)
        sql = 'select * from dives where diverName=\'%s\' and diveDate=\'%s\' and cleanupNumber=\'%s\'' % val
        self.curs.execute(sql)
        lst = self.curs.fetchall()
        return lst
    
    def GetDive(self, id):
        #recordid, cleanupNumber, diveDate, diverName, start, stop, latitude, longitude, bearing, notes, tenderName
        id = str(id)
        t = (id,)
        self.curs.execute('select * from dives where rowid=?', t)
        return self.curs.fetchone()
    
    def GetDateList(self, lst):
        uniquedates = []
        for row in lst:
            try:
                uniquedates.index(row[2])
            except ValueError:
                uniquedates.append(row[2])
        return uniquedates
    
    def GetBasicCleanupList(self):
        self.curs.execute('select distinct cleanupNumber from dives')
        #print self.curs.fetchall()
        lst = []
        for each in self.curs.fetchall():
            print str(each)
            lst.append(str(each[0]))
        if lst.__len__() is 0:
            lst.append('1')
        return lst        
    
    def GetCleanupList(self):
        self.curs.execute('select cleanupNumber from dives')
        lst = self.curs.fetchall()
        unique = []
        strlst = []
        for row in lst:
            try:
                unique.index(row[0])
            except ValueError:
                unique.append(row[0])
        for each in unique:
            self.curs.execute('select * from dives where cleanupNumber=?', str(each))
            lst = self.curs.fetchall()
            datelst = self.GetDateList(lst)
            epochlst = []
            for date in datelst:
                epochlst.append(time.mktime(time.strptime(date, '%b %d %Y')))
            firstday = time.strftime('%b-%d-%y', time.localtime(min(epochlst)))
            lastday = time.strftime('%b-%d-%y', time.localtime(max(epochlst)))
            if each == self.GetLastCleanupRound():
                strlst.append(str(each) + ': ' + firstday + ' to ...')
            else:
                strlst.append(str(each) + ': ' + firstday + ' to ' + lastday)
        return strlst
        
    def GetDiverList(self, cleanupNumber=1):
        #gets list of divers in dive data not personnel
        lst = self.GetCleanupSQLData(cleanupNumber)
        uniquedivers = []
        for row in lst:
            try:
                uniquedivers.index(row[3])
            except ValueError:
                uniquedivers.append(row[3])
        return uniquedivers
    
    def GetCrewList(self):
        self.curs.execute('select * from crew')
        return self.curs.fetchall()
    
    def GetBasicDiverList(self):
        self.curs.execute('select name from crew where duty = \'Diver and Tender\'')
        divers = self.curs.fetchall()
        lst = []
        for each in divers:
            lst.append(each[0])
        return lst
    
    def GetBasicTenderList(self):
        self.curs.execute('select name from crew where duty = \'Diver and Tender\'')
        divers = self.curs.fetchall()
        self.curs.execute('select name from crew where duty = \'Tender\'')
        tenders = self.curs.fetchall()
        lst = []
        for each in tenders:
            lst.append(each[0])
        for each in divers:
            lst.append(each[0])
        return lst
    
    def GetGPSSettings(self):
        self.curs.execute('select value from settings where setting = \'gpscom\' ')
        try:
            com = self.curs.fetchall()[0][0]
        except IndexError:
            com = None
        self.curs.execute('select value from settings where setting = \'gpsbaud\' ')
        try:
            baud = int(self.curs.fetchall()[0][0])
        except IndexError:
            baud = None
        return (com, baud)
    
    def SetGPSSettings(self, com, baud):
        self.curs.execute('delete from settings where setting = \'gpscom\' ')
        self.curs.execute('delete from settings where setting = \'gpsbaud\' ')
        self.conn.commit()
        t = ('gpscom', str(com))
        self.curs.execute("""insert into settings values (?,?)""",t)
        self.conn.commit()
        t = ('gpsbaud', str(baud))
        self.curs.execute("""insert into settings values (?,?)""",t)
        self.conn.commit()
        
    def DropCrewData(self):
        self.curs.execute('delete from crew')
        self.conn.commit()
        
    def AddCrew(self, name, duty, diverate, tendrate):
        name = name.strip()
        t = (name, duty, diverate, tendrate)
        self.curs.execute("""insert into crew values (NULL,?,?,?,?)""",t)
        self.conn.commit()
    
    def SecondsToHMString(self, seconds):
        minutes = seconds/60
        hours = int(minutes/60)
        minutes = int(minutes-hours*60)
        return str(hours) + 'hrs ' + str(minutes) + 'min'
    
    def GetDiveString(self, lst, date, diver):
        divestr = ''
        seconds = 0
        for row in lst:
            if row[2] == date and row[3] == diver:
                start = time.mktime(time.strptime(row[4] +' 1970', "%I:%M %p %Y"))
                stop = time.mktime(time.strptime(row[5] +' 1970', "%I:%M %p %Y"))
                seconds += stop - start
                divestr += '\n%s to %s' %(row[4], row[5])
                first = False
        if divestr == '':
            divestr = '\n**No Dives**'   
        return self.SecondsToHMString(seconds) + divestr
    
    def GetDiveTuple(self, lst, date, diver):
        divestr = ''
        for row in lst:
            if row[2] == date and row[3] == diver:
                start = time.mktime(time.strptime(row[4] +' 1970', "%I:%M %p %Y"))
                stop = time.mktime(time.strptime(row[5] +' 1970', "%I:%M %p %Y"))
                seconds = stop-start
                divestr += '%s to %s' %(row[4], row[5])
        if divestr == '':
            divestr = '0hrs 0min\n**No Dives**'   
        return (divestr, seconds)
    
    def GetDataTable(self, cleanupNumber=1):
        lst = self.GetCleanupSQLData(cleanupNumber)
        table = []
        diverlist = []
        for date in self.GetDateList(lst):
            row = []
            row.append(date)
            diverlist = self.GetDiverList(cleanupNumber)
            for diver in diverlist:
                total = 0
                diveString = self.GetDiveString(lst, date, diver)
                row.append(diveString)
            seconds = 0
            for dive in row[1:row.__len__()]:
                seconds += 3600 * int(dive[0:dive.index('hrs')])
                seconds += 60 * int(dive[dive.index(' ')+1:dive.index('min')])
            row.append(self.SecondsToHMString(seconds)) 
            table.append(row)
        
        #grand total
        seconds = 0
        for row in table:
            hm = row[-1]
            seconds += 3600 * int(hm[0:hm.index('hrs')])
            seconds += 60 * int(hm[hm.index(' ')+1:hm.index('min')])
        grandT = self.SecondsToHMString(seconds)
            
        #final row
        row = ['Totals']
        num = diverlist.__len__()+1
        for index in range(num):
            if index > 0 and index < num:
                seconds = 0
                for rows in table:
                    dive = rows[index]
                    seconds += 3600 * int(dive[0:dive.index('hrs')])
                    seconds += 60 * int(dive[dive.index(' ')+1:dive.index('min')])
                row.append(self.SecondsToHMString(seconds))
        row.append(grandT)
        table.append(row)       
        return table
    
    def AppendDive(self, cleanup, date, diver, start, stop, lat, long, bearing, notes, tender):
        print 'sql inserting record into dives'
        #recordID, cleanupNumber, diveDate, diverName, start, stop, latitude, longitude, heading
        t = (cleanup, date, diver, start, stop, lat, long, bearing, notes, tender)
        self.curs.execute("""insert into dives values(NULL,?,?,?,?,?,?,?,?,?,?)""", t)
        self.conn.commit()
        return self.curs.lastrowid
    
    def DeleteDive(self, id):
        print 'sql deleting from dives rowid: ', id
        t = (str(id),)
        self.curs.execute("""delete from dives where rowid=?""", t)
        self.conn.commit()
        
    def UpdateDive(self, id, cleanup, date, diver, start, stop, lat, long, bearing, notes, tender):
        print 'sql updating record in dives rowid: ', id
        val = (str(cleanup), str(date), diver, start, stop, lat, long, str(bearing), notes, tender, str(id))
        sql = """update dives set 
                 cleanupNumber='%s', 
                 diveDate='%s', 
                 diverName='%s', 
                 start='%s', 
                 stop='%s', 
                 latitude='%s', 
                 longitude='%s', 
                 bearing='%s', 
                 notes='%s' ,
                 tenderName='%s' 
                 where ROWID='%s'""" % val
        self.curs.execute(sql) 
        self.conn.commit()
        
    def UpdateDive2(self, id, cleanup, diver):
        print 'sql updating record in dives rowid: ', id
        val = (str(cleanup), diver, str(id))
        sql = """update dives set cleanupNumber='%s', 
                 diverName='%s' 
                 where ROWID='%s'""" % val
        self.curs.execute(sql) 
        self.conn.commit()
        
    def Close(self):
        #print 'sql closing datastore'
        self.curs.close()
        
if __name__=='__main__':
    DiveRTdbFile = 'C:\ProgramData\DiveRT\DiveRT.db'
    ds = DataStore(DiveRTdbFile)
    print ds.GetBasicCleanupList()

    ds.Close()
        