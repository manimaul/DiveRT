#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Copyright (C) 2010 by Will Kamp <manimaul!gmail.com>

import sqlite3 as sql
import time, Kml

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
        t = (cleanupNumber,)
        self.curs.execute('select distinct diverName from dives where cleanupNumber=?', t)
        lst = []
        for each in self.curs.fetchall():
            lst.append( each[0] )
        return lst
    
    def GetOperatorDiverList(self, cleanupNumber=1):
        self.curs.execute('select name from crew where duty == \'Operator Diver\'')
        lst = []
        for each in self.curs.fetchall():
            lst.append( each[0] )
        return list(set(lst).intersection(self.GetDiverList(cleanupNumber)))
    
    def GetExtraDiverList(self, cleanupNumber=1):
        self.curs.execute('select name from crew where duty == \'Extra Diver\'')
        lst = []
        for each in self.curs.fetchall():
            lst.append( each[0] )
        return list(set(lst).intersection(self.GetDiverList(cleanupNumber)))
    
    def GetTenderList(self, cleanupNumber=1):
        t = (cleanupNumber,cleanupNumber)
        #self.curs.execute('select distinct diverName, tenderName from dives where cleanupNumber=?', t)
        self.curs.execute('select distinct(ans) from (select diverName as ans from dives where cleanupNumber=? union select tenderName as ans from dives where cleanupNumber=?)', t)
        lst = []
        for each in self.curs.fetchall():
            lst.append( each[0] )
        return lst
    
    def GetTendingHours(self, cleanupNumber, tenderName):
        t = (cleanupNumber, tenderName)
        self.curs.execute('select start, stop from dives where cleanupNumber=? and tenderName=?', t)
        seconds = 0
        for startstop in self.curs.fetchall():
            start = time.mktime( time.strptime( startstop[0] +' 1970', "%I:%M %p %Y" ) )
            stop = time.mktime( time.strptime( startstop[1] +' 1970', "%I:%M %p %Y" ) )
            seconds += stop - start
            if seconds < 0:
                    seconds += 86400 #add 24hours if dive was overnight
        tending = seconds / 60 / 60
        
        t = (cleanupNumber, tenderName)
        self.curs.execute('select start, stop from dives where cleanupNumber=? and diverName=?', t)
        seconds = 0
        for startstop in self.curs.fetchall():
            start = time.mktime( time.strptime( startstop[0] +' 1970', "%I:%M %p %Y" ) )
            stop = time.mktime( time.strptime( startstop[1] +' 1970', "%I:%M %p %Y" ) )
            seconds += stop - start
            if seconds < 0:
                    seconds += 86400 #add 24hours if dive was overnight
        diving = seconds / 60 / 60
        
        result = tending - diving
        
        return round( result, 2 )
    
    def GetTenderRate(self, tenderName):
        defaultRate = 20
        self.curs.execute('select tendrate from crew where name=?', (tenderName,) )
        rate = self.curs.fetchone()
        if rate is not None:
            return float(rate[0])
        else:
            return defaultRate
    
    def GetDiverRates(self, diverlist):
        lst = []
        for each in diverlist:
            self.curs.execute( 'select diverate from crew where name=?', (each,) )
            lst.append( (each,self.curs.fetchone()[0]) )
        directory = dict( lst )
        return directory
    
    def GetKMLData(self):
        #[(round, ozperhr), [(date, name, hrs, color, bearing, icon, note, lat, long), ] ]
        lst = []
        
        icons = Kml.iconList()
        #colors = ( 'ffc183', 'ff0000', 'ff1ab8', '837200', '72607b', '8ca77b', '9e4f46')
        #badcolors = ( '00ff00', '72f6ff',  'f61160', '00ffc1','005700', '9ec1ff', 'ffd300', '0000ff',)
        i = 0
        for number in self.GetBasicCleanupList(): #list of all rounds from dives
            folder = ( number, self.GetOzPerHour(number))
            #print folder
            self.curs.execute('select * from dives where cleanupNumber=?', (number))
            fetch = self.curs.fetchall()
            #print fetch
            placemarks = []
            if fetch is not None:
                for each in fetch:
                    #date = each[2]
                    str_strptime = time.strptime(each[2], '%b %d %Y')
                    month = str( int( time.strftime('%m', str_strptime) ) )
                    day = str( int( time.strftime('%d', str_strptime) ) )
                    year = time.strftime('%y', str_strptime)
                    date = month +'-'+ day #+'-'+ year
                    name = each[3]
                    title = date + ' ' + name[0] #add initial to placemark title
                    title = title + number #add round
                    seconds = time.mktime(time.strptime(each[5] +' 1970', "%I:%M %p %Y")) - time.mktime(time.strptime(each[4] +' 1970', "%I:%M %p %Y"))
                    if seconds < 0:
                        seconds += 86400 #add 24hours if dive was overnight
                    hrs = str( round(seconds / 60 / 60, 2) )
                    lat = each[6]
                    latitude = lat.split('*')[0]
                    if lat.split('*')[1] == 'S':
                        latitude = '-' + latitude
                    lon = each[7]
                    longitude = lon.split('*')[0]
                    if lon.split('*')[1] == 'W':
                        longitude = '-' + longitude
                    bearing = each[8]
                    if bearing == 'None':
                        icon = 'circle' + icons[i]
                        bearing = '0.0'
                    elif ( float( bearing.split( '*' )[0] ) == 0.0):
                        icon = 'circle' + icons[i]
                        bearing = '0.0'
                    else:
                        icon = 'arrow' + icons[i]
                        bearing = bearing.split('*')[0]
                    note = each[9]
                    if (float(latitude)!= 0.0) or (float(longitude)!= 0.0):
                        placemarks.append( (title, name, hrs, bearing, icon, note, longitude, latitude) )
            if i == icons.__len__() - 1:
                i = 0
            else:
                i += 1
            lst.append( (folder, placemarks) )
        return lst
    
    def GetOzPerHour(self, cleanupNumber):
        self.curs.execute('select grams from cleanups where number=?', (cleanupNumber,) )
        fetch = self.curs.fetchone()
        grams = 0.0
        if fetch is not None:
            if fetch[0] != '':
                grams = float( fetch[0] )
        troyOz = grams / 31.1034768
        hours = float( self.GetTotalHours(cleanupNumber) )
        if hours == 0.0:
            ozPerHr = '0.0'
        else:
            ozPerHr = str( round(troyOz / hours, 2) )
        return ozPerHr
        
    def GetCrewList(self):
        self.curs.execute('select * from crew')
        return self.curs.fetchall()
    
    def GetBasicDiverList(self):
        self.curs.execute('select name from crew where duty != \'Tender\'')
        divers = self.curs.fetchall()
        lst = []
        for each in divers:
            lst.append(each[0])
        return lst
        
    def GetBasicTenderList(self):
        self.curs.execute('select name from crew')
        tenders = self.curs.fetchall()
        lst = []
        for each in tenders:
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
        
    def SaveReportTotals(self, cleanupNumber, grams, spot, loss):
        #remove any old report first
        t = ( str(cleanupNumber), )
        self.curs.execute( """delete from cleanups where number=?""", t )
        self.curs.execute( """delete from cleanupsub where number=?""", t )
        
        #save new report
        t = ( int(cleanupNumber), str(grams), str(spot), str(loss) )
        self.curs.execute("""insert into cleanups values (?,?,?,?)""",t)
        self.conn.commit()
        
    def GetReportTotals(self, cleanupNumber):
        t = ( str(cleanupNumber) )
        self.curs.execute( """select * from cleanups where number=?""", t )
        return self.curs.fetchone()
    
    def SaveReportDiverDetails(self, cleanupNumber, name, rate):
        t = ( int(cleanupNumber), str(name), str(rate))
        self.curs.execute("""insert into cleanupsub values (?,?,?)""",t)
        self.conn.commit()
        
    def GetReportDiverDetails(self, cleanupNumber):
        """returns a dictionary of divers and rates"""
        t = ( int(cleanupNumber), )
        self.curs.execute( """select name, percent from cleanupsub where number=?""",t )
        return dict( self.curs.fetchall() )
        
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
                if seconds < 0:
                    seconds += 86400 #add 24hours if dive was overnight
                divestr += '\n%s to %s' %(row[4], row[5])
                divestr += '\nTending: %s' %(row[10])
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
            ##add date
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
                if seconds < 0:
                    seconds += 86400 #add 24hours if dive was overnight
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
    
    def GetRoundDateRange(self, cleanupNumber=1):
        t = (cleanupNumber,)
        self.curs.execute( 'select distinct diveDate from dives where cleanupNumber=?', t)
            
        epochlst = []
        for dates in self.curs.fetchall():
            #print dates[0]
            epochlst.append(time.mktime(time.strptime(dates[0], '%b %d %Y')))
        if epochlst.__len__() > 0:
            firstday = time.strftime('%b, %d to ', time.localtime(min(epochlst)))
            lastday = time.strftime('%b, %d %Y', time.localtime(max(epochlst)))
            return firstday + lastday
        else:
            return ''
    
    def GetTotalHours(self, cleanupNumber):
        data = self.GetDataTable(cleanupNumber)
        hmstr = data[-1][-1]
        hrs = hmstr[0:hmstr.index('hrs' )]
        min = hmstr[hmstr.index(' '):hmstr.index('min')].strip()
        
        result = float(hrs)+float(min)/60
        return  str( round( result, 2 ) )
    
    def GetCleanupTotals(self, cleanupNumber):
        diverlst = self.GetDiverList(cleanupNumber)
        totals = self.GetDataTable(cleanupNumber)[-1]
        lst = []
        i=0 
        for diver in diverlst:
            i += 1
            hmstr = totals[i]
            hrs = hmstr[0:hmstr.index('hrs' )]
            min = hmstr[hmstr.index(' '):hmstr.index('min')].strip()
            result = float(hrs)+float(min)/60
            hmstr = str( round( result, 2 ) )
            lst.append( (diver, hmstr) )
        directory = dict( lst )
        return directory
    
    def AppendDive(self, cleanup, date, diver, start, stop, lat, long, bearing, notes, tender):
        #print 'sql inserting record into dives'
        #recordID, cleanupNumber, diveDate, diverName, start, stop, latitude, longitude, heading
        t = (cleanup, date, diver, start, stop, lat, long, bearing, notes, tender)
        self.curs.execute("""insert into dives values(NULL,?,?,?,?,?,?,?,?,?,?)""", t)
        self.conn.commit()
        return self.curs.lastrowid
    
    def DeleteDive(self, id):
        #print 'sql deleting from dives rowid: ', id
        t = (str(id),)
        self.curs.execute("""delete from dives where rowid=?""", t)
        self.conn.commit()
        
    def UpdateDive(self, id, cleanup, date, diver, start, stop, lat, long, bearing, notes, tender):
        #print 'sql updating record in dives rowid: ', id
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
        #print 'sql updating record in dives rowid: ', id
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
    
    print ds.GetExtraDiverList(1)
    print ds.GetOperatorDiverList(1)
    
    ds.Close()
        