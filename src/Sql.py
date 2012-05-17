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
    
    def IsCleanupData(self):
        self.curs.execute("select number from cleanups")
        num = self.curs.fetchall().__len__()
        if num > 0:
            return True;
        else:
            return False
        
    def GetAverageLondonSpot(self):
        self.curs.execute('select londonspot from cleanups')
        fetch = self.curs.fetchall()
        i = 0
        p = 0
        for price in fetch:
            if price[0] != '':
                spot = float(price[0])
            else:
                spot = 0
            if spot > 0:
                p += spot
                i+=1
        if i == 0:
            return p
        else:
            return round(p/i, 2)
        
    def GetLastCleanupRound(self):
        self.curs.execute('select max(cleanupNumber) from dives')
        r = self.curs.fetchall()[0][0]
        if r is None:
            r = 1
        return int(r)
        
    def GetCleanupSQLData(self, cleanupNumber=None):
        if cleanupNumber == None:
            self.curs.execute('select * from dives')
        else:
            sql = "select * from dives where cleanupNumber=\'%s\'" %(str(cleanupNumber))
            self.curs.execute(sql)
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
        sql = "select * from dives where rowid=%s"  %(str(id))
        self.curs.execute(sql)
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
    
#    def GetCleanupList(self):
#        self.curs.execute('select cleanupNumber from dives')
#        lst = self.curs.fetchall()
#        unique = []
#        strlst = []
#        for row in lst:
#            try:
#                unique.index(row[0])
#            except ValueError:
#                unique.append(row[0])
#        for each in unique:
#            self.curs.execute('select * from dives where cleanupNumber=?', str(each))
#            lst = self.curs.fetchall()
#            datelst = self.GetDateList(lst)
#            epochlst = []
#            for date in datelst:
#                epochlst.append(time.mktime(time.strptime(date, '%b %d %Y')))
#            firstday = time.strftime('%b-%d-%y', time.localtime(min(epochlst)))
#            lastday = time.strftime('%b-%d-%y', time.localtime(max(epochlst)))
#            if each == self.GetLastCleanupRound():
#                strlst.append(str(each) + ': ' + firstday + ' to ...')
#            else:
#                strlst.append(str(each) + ': ' + firstday + ' to ' + lastday)
#        return strlst
    
    def GetCleanupList(self):
        self.curs.execute('select distinct cleanupNumber from dives')
        clist = self.curs.fetchall()
        strlst = []
        for each in clist:
            sql = 'select * from dives where cleanupNumber=%s' %(str(each[0]))
            self.curs.execute(sql)
            lst = self.curs.fetchall()
            datelst = self.GetDateList(lst)
            epochlst = []
            #print datelst
            for date in datelst:
                epochlst.append(time.mktime(time.strptime(date, '%b %d %Y')))
            firstday = time.strftime('%b-%d-%y', time.localtime(min(epochlst)))
            lastday = time.strftime('%b-%d-%y', time.localtime(max(epochlst)))
            strlst.append(str(each[0]) + ': ' + firstday + ' to ' + lastday)
        return strlst
    
    def GetSeasonDates(self):
        self.curs.execute('select distinct diveDate from dives')
        datelst = self.curs.fetchall()
        epochlst = []
        for date in datelst:
            epochlst.append(time.mktime(time.strptime(date[0], '%b %d %Y')))
        numdays = epochlst.__len__()
        firstday = time.strftime('%b-%d-%y', time.localtime(min(epochlst)))
        lastday = time.strftime('%b-%d-%y', time.localtime(max(epochlst)))
        return str(numdays) + " days worked from " + firstday + " to " + lastday
        
    def GetDiverList(self, cleanupNumber=None):
        if cleanupNumber == None:
            self.curs.execute('select distinct diverName from dives')
        else:
            sql = "select distinct diverName from dives where cleanupNumber=\'%s\'" %(cleanupNumber)
            self.curs.execute(sql)
        lst = []
        for each in self.curs.fetchall():
            lst.append( each[0] )
        return lst
    
    def GetOperatorDiverList(self, cleanupNumber=None):
        self.curs.execute('select name from crew where duty == \'Operator Diver\'')
        lst = []
        for each in self.curs.fetchall():
            lst.append( each[0] )
        if cleanupNumber == None:
            return lst
        else:
            return list(set(lst).intersection(self.GetDiverList(cleanupNumber)))
    
    def GetExtraDiverList(self, cleanupNumber=None):
        self.curs.execute('select name from crew where duty == \'Diver\' or duty == \'Extra Diver\' ')
        lst = []
        for each in self.curs.fetchall():
            lst.append( each[0] )
        if cleanupNumber == None:
            return lst
        else:
            return list(set(lst).intersection(self.GetDiverList(cleanupNumber)))
    
    def GetTenderList(self, cleanupNumber=1):
        sql = 'select distinct(ans) from (select diverName as ans from dives where cleanupNumber=%s union select tenderName as ans from dives where cleanupNumber=%s)' %(cleanupNumber,cleanupNumber)
        self.curs.execute(sql)
        lst = []
        for each in self.curs.fetchall():
            lst.append( each[0] )
        return lst
    
    def GetTendingHours(self, cleanupNumber, tenderName):
        sql = 'select start, stop from dives where cleanupNumber=%s and tenderName=%s' %(cleanupNumber, tenderName)
        self.curs.execute(sql)
        seconds = 0
        for startstop in self.curs.fetchall():
            start = time.mktime( time.strptime( startstop[0] +' 1970', "%I:%M %p %Y" ) )
            stop = time.mktime( time.strptime( startstop[1] +' 1970', "%I:%M %p %Y" ) )
            seconds += stop - start
            if seconds < 0:
                    seconds += 86400 #add 24hours if dive was overnight
        tending = seconds / 60 / 60
        
        sql = 'select start, stop from dives where cleanupNumber=%s and diverName=%s' %(cleanupNumber, tenderName)
        self.curs.execute(sql)
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
        sql = 'select tendrate from crew where name=%s' %(tenderName)
        self.curs.execute(sql)
        rate = self.curs.fetchone()
        if rate is not None:
            return float(rate[0])
        else:
            return defaultRate
    
    def GetDiverRates(self, diverlist):
        lst = []
        for each in diverlist:
            sql = "select diverate from crew where name=\'%s\'" %(each)
            self.curs.execute(sql)
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
            sql = 'select * from dives where cleanupNumber=%s' %(number)
            self.curs.execute(sql)
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
        sql = 'select grams from cleanups where number=%s' %(cleanupNumber)
        self.curs.execute(sql)
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
    
    def GetSavedPerspective(self):
        self.curs.execute("select value from settings where setting = \'perspective\' ")
        fetch = self.curs.fetchone()
        if fetch != None:
            return fetch[0]
    
    def SavePerspective(self, perspective):
        self.curs.execute("delete from settings where setting = \'perspective\' ")
        sql = "insert into settings values (\'perspective\', \'%s\')" %(perspective)
        self.curs.execute(sql)
        self.conn.commit()
    
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
        
    def SaveReportTotals(self, cleanupNumber, grams, spot, loss, ownerpct, operpct):
        #remove any old report first
        sql = "delete from cleanups where number=%s" %(str(cleanupNumber))
        self.curs.execute(sql)
        sql = "delete from cleanupsub where number=%s" %(str(cleanupNumber))
        self.curs.execute(sql)
        
        #save new report
        sql = "insert into cleanups values (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')" %( str(cleanupNumber), str(grams), str(spot), str(loss), str(ownerpct), str(operpct) )
        self.curs.execute(sql)
        self.conn.commit()
        
    def GetReportTotals(self, cleanupNumber):
        sql = "select * from cleanups where number=%s" %(str(cleanupNumber))
        self.curs.execute( sql )
        return self.curs.fetchone()
    
    def SaveReportDiverDetails(self, cleanupNumber, name, rate):
        sql = "insert into cleanupsub values (\'%s\',\'%s\',\'%s\')" %( int(cleanupNumber), str(name), str(rate))
        self.curs.execute(sql)
        self.conn.commit()
        
    def GetReportDiverDetails(self, cleanupNumber):
        """returns a dictionary of divers and rates"""
        sql = "select name, percent from cleanupsub where number=%s" %(int(cleanupNumber))
        self.curs.execute( sql )
        return dict( self.curs.fetchall() )
        
    def DropCrewData(self):
        self.curs.execute('delete from crew')
        self.conn.commit()
        
    def AddCrew(self, name, duty, diverate, tendrate):
        name = name.strip()
        sql = "insert into crew values (NULL,\'%s\',\'%s\',\'%s\',\'%s\')" %(name, duty, diverate, tendrate)
        self.curs.execute(sql)
        self.conn.commit()
    
    def SecondsToHMString(self, seconds):
        minutes = seconds/60
        hours = int(minutes/60)
        minutes = int(minutes-hours*60)
        return str(hours) + 'hrs ' + str(minutes) + 'min'
    
    def StartStopToSeconds(self, start, stop):
        seconds = 0
        startsec = time.mktime(time.strptime(start +' 1970', "%I:%M %p %Y"))
        stopsec = time.mktime(time.strptime(stop +' 1970', "%I:%M %p %Y"))
        seconds += stopsec - startsec
        if seconds < 0:
            seconds += 86400 #add 24hours if dive was overnight
        return seconds
        
    def SecondsToHoursFloat(self, seconds):
        minutes = seconds/60.0
        hours = minutes/60.0
        return hours
    
    def GetDiveString(self, lst, date, diver):
        divestr = ''
        seconds = 0
        for row in lst:
            if row[2] == date and row[3] == diver:
                seconds += self.StartStopToSeconds(row[4], row[5])
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
        sql = 'select distinct diveDate from dives where cleanupNumber=%s' %(cleanupNumber)
        self.curs.execute(sql)
            
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
    
    def GetSeasonHours(self):
        total = 0.0
        for each in self.GetBasicCleanupList():
            total += float( self.GetTotalHours(each) )
        return total
    
    def GetSeasonGrams(self):
        self.curs.execute('select grams from cleanups')
        result = self.curs.fetchall()
        total = 0.0
        for each in result:
             try: total += float(each[0])
             except ValueError: total += 0
        return total
    
    def GetSeasonOwnerGrams(self):
        self.curs.execute("""select grams, ownerpct from cleanups""")
        grams = 0.0
        percent = 0.55
        for each in self.curs.fetchall():
            if each[1] == None:
                grams += ( float(each[0]) * percent )
            else:
                try: grams += ( float(each[0]) * ( float(each[1]) / 100) )
                except ValueError: grams += 0
        return grams
    
    def GetSeasonOperGrams(self):
        self.curs.execute("""select grams, operapct from cleanups""")
        grams = 0.0
        percent = 0.45
        for each in self.curs.fetchall():
            if each[1] == None:
                grams += ( float(each[0]) * percent )
            else:
                try: grams += ( float(each[0]) * ( float(each[1]) / 100) )
                except ValueError: grams += 0
        return grams
    
    def GetSeasonExtraDiverGrams(self, name):
        totalGrams = 0.0
        #list of cleanups
        sql = "select distinct cleanupNumber from dives where diverName=\'%s\'" %(name)
        self.curs.execute(sql)
        cleanups = []
        for each in self.curs.fetchall():
            cleanups.append(each[0])
        for cleanup in cleanups:
            #hrs/thrs * pct * tgrams
            hrs = float( self.GetCleanupTotals(cleanup)[name] )
            thrs = float ( self.GetTotalHours(cleanup) )
            if self.GetReportDiverDetails(cleanup).has_key(name):
                pct = float( self.GetReportDiverDetails(cleanup)[name] ) / 100.0
            else:
                pct = float( self.GetDiverRates([name])[name] ) / 100.0
            #print 'cleanup: ', cleanup, name, 'using: ', pct, '%'
            reportTotals = self.GetReportTotals(cleanup)
            if reportTotals != None:
                tgrams = float( reportTotals[1] )
            else:
                tgrams = 0.0
            totalGrams += round((hrs/thrs * pct * tgrams), 2)
        return totalGrams
    
    def GetSeasonDiverGrams(self, name):
        totalGrams = 0.0
        #list of cleanups
        sql = "select distinct cleanupNumber from dives where diverName=\'%s\'" %(name)
        self.curs.execute(sql)
        cleanups = []
        for each in self.curs.fetchall():
            cleanups.append(each[0])
        
        for cleanup in cleanups:
            hrs = float( self.GetCleanupTotals(cleanup)[name] )
            
            thrs = 0.0
            opDivers = self.GetOperatorDiverList(cleanup)
            for diver in opDivers:
                thrs += float( self.GetCleanupTotals(cleanup)[diver] )
            
            sql = "select operapct from cleanups where number=%s" %(cleanup)
            self.curs.execute(sql)
            fetch = self.curs.fetchone()
            if fetch != None:
                if fetch[0] == None:
                    pct = 0.45
                else:
                    pct = float(fetch[0]) / 100
            else:
                pct = 0.45
            
            try: tgrams = float( self.GetReportTotals(cleanup)[1] )
            except: tgrams = 0.0
            extraDiverGrams = 0
            exDivers = self.GetExtraDiverList(cleanup)
            for diver in exDivers:
                sql = "select percent from cleanupsub where number=\'%s\' and name=\'%s\'" %(cleanup, diver)
                self.curs.execute(sql)
                fetch = self.curs.fetchone()
                if fetch != None:
                    expct = float(fetch[0])
                else:
                    expct = float(self.GetDiverRates([diver])[diver])
 
                exhrs = float( self.GetCleanupTotals(cleanup)[diver] )
                exgrams = round( (exhrs / (exhrs + thrs) * tgrams * (expct / 100)), 1)
                extraDiverGrams += exgrams
                #print diver, expct, exhrs, exgrams
            netgrams = tgrams * pct - extraDiverGrams
            mygrams = round((hrs/thrs * netgrams), 3)
            #print hrs, thrs, pct, mygrams, tgrams
            totalGrams += mygrams
        return round(totalGrams, 2)
    
    def GetPercentages(self, cleanupNumber=1):
        sql = "select ownerpct, operapct from cleanups where number=%s" %(cleanupNumber)
        self.curs.execute(sql)
        result = self.curs.fetchone()
        if result == None:
            return (u'55.0', u'45.0')
        elif result == (None, None):
            return (u'55.0', u'45.0')
        else:
            return result
    
    def GetCleanupTotals(self, cleanupNumber=None):
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
        sql = "insert into dives values(NULL,\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')" %(cleanup, date, diver, start, stop, lat, long, bearing, notes, tender)
        self.curs.execute(sql)
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
                 where ROWID='%s'""" %val
        self.curs.execute(sql) 
        self.conn.commit()
        
    def VersionCheck(self, version):
        sql = "select value from settings where setting=\"version\""
        self.curs.execute(sql)
        sqlVersion = self.curs.fetchone()
        if sqlVersion == None: #v1.06 and prior
            #print "Updating SQL to version:", version
            sqlfile = open('DiveRT_1.07_Update.sql', 'r')
            sqldat = sqlfile.read()
            sqlfile.close()
            self.curs.executescript(sqldat)
            self.conn.commit()
            
    def GetVessel(self):
        sql = "select value from settings where setting=\"vessel\""
        self.curs.execute(sql)
        vessel = self.curs.fetchone()
        if (vessel != None):
            return vessel[0]
        else:
            return None
    
    def SetVessel(self, vessel):
        t = ('vessel', str(vessel))
        self.curs.execute("""insert into settings values (?,?)""",t)
        self.conn.commit()
            
    def Close(self):
        #print 'sql closing datastore'
        self.curs.close()
        
if __name__=='__main__':
    DiveRTdbFile = 'C:\ProgramData\DiveRT\DiveRT.db'
    ds = DataStore(DiveRTdbFile)
    #print ds.GetSeasonExtraDiverGrams("Mike")
    #print ds.GetSeasonDiverGrams("Dave")
    #print ds.GetAverageLondonSpot()
    #print ds.GetAverageLondonSpot()
    #print ds.GetCleanupList()
    #print ds.GetSeasonDates()
    #print ds.GetCleanupSQLData('1')
    #print ds.GetSeasonDiverGrams('Dave')
    #print ds.GetSeasonExtraDiverGrams('Mike')
    print ds.GetLastPerspective()
    
    ds.Close()
        