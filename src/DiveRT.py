#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Copyright (C) 2010 by Will Kamp <manimaul!gmail.com>

import Grid, time, GUI, Sql, os, wx.aui, GPSCom, re, shutil, Kml, subprocess
import wx.grid as gridlib, wx.lib.scrolledpanel as scrolled

class ConfirmDlg(GUI.ConfirmDlg): #POPUP WINDOW
    def _evtYes(self, evt):
        sel = frame.listpanel.times_listBox.GetStringSelection()
        if sel.__len__() == 8: #only has start time... dive needs to be stopped
            frame.divepanel._evtStartStop(None)
        else: #delete from db
            dex = frame.listpanel.times_listBox.GetSelection()
            id = frame.listpanel.diveidlst[dex]
            frame.listpanel.diveidlst.pop(dex)
            datastore = Sql.DataStore(DiveRTdbFile)
            datastore.DeleteDive(id)
            datastore.Close()
            frame.grid._evtRefresh(None)
            
        frame.listpanel.times_listBox.Delete(frame.listpanel.times_listBox.GetSelection())
        nsel = frame.listpanel.times_listBox.GetItems().__len__()-1
        frame.listpanel.times_listBox.SetSelection(nsel)
        if nsel == -1:
            frame.listpanel.edit_Button.Enable(False)
            frame.listpanel.delete_Button.Enable(False)
        diveKml.compileDiveFolders() #update kml map
        diveKml.writeKmlToServer()
        self.Destroy()
    
    def _evtCancel(self, evt):
        self.Destroy()
        
class MsgDialog(GUI.MsgDialog): #POPUP DIALOG
    def changeMessage(self, msg=u"Message"):
        self.msg_staticText.SetLabel( msg )
        self.SetSizer( self.bSizer )
        self.Layout()
        self.bSizer.Fit( self )
        
    def _evtOK(self, evt):
        evt.Skip()
        self.Destroy()
        
class SimpleConfirmDlg(GUI.ConfirmDlg): #POPUP DIALOG
    def changeMessage(self, msg=u"Are you sure?"):
        self.message.SetLabel( msg )
        self.SetSizer( self.bSizer )
        self.Layout()
        self.bSizer.Fit( self )
        
    def _evtYes(self, evt):
        self.Parent.flag = True
        evt.Skip()
        self.Destroy()
        
    def _evtCancel(self, evt):
        self.Parent.flag = False
        evt.Skip()
        self.Destroy()

class EditDlg(GUI.EditDlg): #POPUP WINDOW
    def _evtHr(self, evt):
        ctrl = evt.GetEventObject()
        val = str(ctrl.GetValue())
        newval = re.sub(r'\D+', '', val) #remove any non digits
        if newval != val:
            ctrl.SetValue(newval)
            ctrl.SetInsertionPointEnd()
        if newval != '':
            if int(newval) > 12:
                ctrl.SetValue('12')
    
    def _evtMinSec(self, evt):
        ctrl = evt.GetEventObject()
        val = str(ctrl.GetValue())
        newval = re.sub(r'\D+', '', val) #remove any non digits
        if newval != val:
            ctrl.SetValue(newval)
            ctrl.SetInsertionPointEnd()
        if newval != '':
            if int(newval) > 59:
                ctrl.SetValue('59')
                                
    def EnableFullEdit(self, full=True):
        if full:
            self.hrtxt.Enable()
            self.mintxt.Enable()
            self.enhr.Enable()
            self.enmin.Enable()
            self.enampm.Enable()
            self.IsFullEdit = True
        else:
            self.IsFullEdit = False
    
    def InsertFillValues(self):
        tenders = frame.divepanel.tender_choice.GetItems()
        self.tender_choice.SetItems(tenders)
        self.tender_choice.SetStringSelection(frame.divepanel.tender)
        self.shour = '6'
        self.sminute = '00'
        apm = 'AM'
        self.sthr.SetValue(self.shour)
        self.stmin.SetValue(self.sminute)
        self.stampm.SetStringSelection(apm)
        self.ehour = str(int(self.shour)+1)
        self.eminute = '00'
        #apm = apm
        self.enhr.SetValue(self.ehour)
        self.enmin.SetValue(self.eminute)
        self.enampm.SetStringSelection(apm)
        
    def EditFillValues(self):
        tenders = frame.divepanel.tender_choice.GetItems()
        self.tender_choice.SetItems(tenders)
        sel = frame.listpanel.times_listBox.GetStringSelection()
        self.shour = sel[0:2]
        self.sminute = sel[3:5]
        apm = sel[6:8]
        self.sthr.SetValue(self.shour)
        self.stmin.SetValue(self.sminute)
        self.stampm.SetStringSelection(apm)
        if self.IsFullEdit: #full edits have information stored in the database
            self.ehour = sel[12:14]
            self.eminute = sel[15:17]
            apm = sel[18:20]
            self.enhr.SetValue(self.ehour)
            self.enmin.SetValue(self.eminute)
            self.enampm.SetStringSelection(apm)
            #begin datastore retrieval
            dex = frame.listpanel.times_listBox.GetSelection()
            id = frame.listpanel.diveidlst[dex]
            datastore = Sql.DataStore(DiveRTdbFile)
            data = datastore.GetDive(id)
            tender = str(data[10])
            self.tender_choice.SetStringSelection(tender)
            lat = data[6].split('*')
            self.lat_textCtrl.SetValue(lat[0])
            self.lat_choice.SetStringSelection(lat[1])
            lon = data[7].split('*')
            self.lon_textCtrl.SetValue(lon[0])
            self.lon_choice.SetStringSelection(lon[1])
            if data[8] != 'None':
                bearing = data[8].split('*')
                self.bearing_textCtrl.SetValue(bearing[0])
                self.bearing_choice.SetStringSelection(bearing[1])
            datastore.Close()         
        else: #non full edits have no intormation stored in the database
            self.tender_staticText.Hide()
            self.tender_choice.Hide()
            self.m_staticline7.Hide()
            self.m_staticTextLat.Hide()
            self.lat_textCtrl.Hide()
            self.lat_choice.Hide()
            self.m_staticTextLon.Hide()
            self.lon_textCtrl.Hide()
            self.lon_choice.Hide()
            self.m_staticTextBearing.Hide()
            self.bearing_textCtrl.Hide()
            self.bearing_choice.Hide()
            self.m_staticline1.Hide()
            self.Fit()
           
    def FmtString(self):
        #fix empty values
        str = ''
        hr = self.sthr.GetValue()
        if hr.__len__() == 1:
            str += '0'
        if hr == '':
            hr = self.shour
        str += hr + ':'
                
        min = self.stmin.GetValue()
        if min.__len__() == 1:
            str += '0'
        if min == '':
            min = self.sminute
        str += min + ' '
        
        apm = self.stampm.GetStringSelection()
        str += apm
        
        if self.IsFullEdit:
            str += ' to '
            hr = self.enhr.GetValue()
            if hr.__len__() == 1:
                str += '0'
            if hr == '':
                hr = self.ehour
            str += hr + ':'
                    
            min = self.enmin.GetValue()
            if min.__len__() == 1:
                str += '0'
            if min == '':
                min = self.eminute
            str += min + ' '
            
            apm = self.enampm.GetStringSelection()
            str += apm
        return str
    
    def floatstr(self, somestring):
        mystr = ''
        decimal = False
        for each in somestring:
            srch = re.search(r'\d', each)
            if srch is not None:
                mystr += srch.group(0)
            srch = re.search(r'\.', each)
            if srch is not None and decimal is False:
                mystr += srch.group(0)
                decimal = True
        return mystr
    
    def _evtLatTxt(self, evt):
        #only allow numbers and  one decimal
        ctrl = evt.GetEventObject()
        value = ctrl.GetValue()
        newval = self.floatstr(value)
        if newval != value:
            ctrl.SetValue(newval)
            ctrl.SetInsertionPointEnd()
        if newval != '':
            if float( newval ) > 90.0:
                ctrl.SetValue( '90.0' )
                ctrl.SetInsertionPointEnd()
                
    def _evtLonTxt(self, evt):
        #only allow numbers and  one decimal
        ctrl = evt.GetEventObject()
        value = ctrl.GetValue()
        newval = self.floatstr(value)
        if newval != value:
            ctrl.SetValue(newval)
            ctrl.SetInsertionPointEnd()
        if newval != '':
            if float( newval ) > 180.0:
                ctrl.SetValue( '180.0' )
                ctrl.SetInsertionPointEnd()
                
    def _evtBearingTxt(self, evt):
        #only allow numbers and  one decimal
        ctrl = evt.GetEventObject()
        value = ctrl.GetValue()
        newval = self.floatstr(value)
        if newval != value:
            ctrl.SetValue(newval)
            ctrl.SetInsertionPointEnd()
        if newval != '':
            if float( newval ) > 359.99:
                ctrl.SetValue( '359.99' )
                ctrl.SetInsertionPointEnd()
    
    def _evtCancel(self, evt):
        self.Destroy()
        
    def _evtOK(self, evt):
        if self.GetTitle() != 'Insert Dive Record': #Edit Time Entry
            dex = frame.listpanel.times_listBox.GetSelection()
            if self.IsFullEdit: #full edits have information stored in the database that need to be updated
                id = frame.listpanel.diveidlst[dex]
                datastore = Sql.DataStore(DiveRTdbFile)
                data = datastore.GetDive(id)
                cleanup = data[1]
                date =  data[2]
                diver = data[3]
                start = self.FmtString()[0:8] 
                stop = self.FmtString()[12:20]
                latval = self.lat_textCtrl.GetValue()
                if latval == '':
                    latval = '00.000000'
                lat = latval + '*' + self.lat_choice.GetStringSelection()
                lonval = self.lon_textCtrl.GetValue()
                if lonval == '':
                    lonval = '000.000000'
                lon = lonval + '*' + self.lon_choice.GetStringSelection()
                bval = self.bearing_textCtrl.GetValue()
                if bval == '':
                    bval = '000.00'
                bearing = bval + '*' + self.bearing_choice.GetStringSelection()
                notes = data[9]
                tender = self.tender_choice.GetStringSelection()
                datastore.UpdateDive(id, cleanup, date, diver, start, stop, lat, lon, bearing, notes, tender)
                datastore.Close()
                frame.grid._evtRefresh(None)
            
            frame.listpanel.times_listBox.Delete(dex)
            frame.listpanel.times_listBox.Insert(self.FmtString(), dex)
            #set listbox selection to one you were editing
            frame.listpanel.times_listBox.SetSelection(dex)
            
                
        else: #Insert Time Entry
            sel = frame.listpanel.times_listBox.GetSelection()+1
            frame.listpanel.edit_Button.Enable()
            frame.listpanel.delete_Button.Enable()
            frame.listpanel.times_listBox.Insert(self.FmtString(), sel)
            #set listbox selection to one you were editing
            frame.listpanel.times_listBox.SetSelection(sel)
            frame.divepanel.tender = self.tender_choice.GetStringSelection()
            #frame.divepanel.lat = self.lat_textCtrl.GetValue()
            #frame.divepanel.long = self.lon_textCtrl.GetValue()
            #frame.divepanel.bearing = self.bearing_textCtrl.GetValue()
            ##
            latval = self.lat_textCtrl.GetValue()
            if latval == '':
                latval = '00.000000'
            frame.divepanel.lat = latval + '*' + self.lat_choice.GetStringSelection()
            lonval = self.lon_textCtrl.GetValue()
            if lonval == '':
                lonval = '000.000000'
            frame.divepanel.long = lonval + '*' + self.lon_choice.GetStringSelection()
            bval = self.bearing_textCtrl.GetValue()
            if bval == '':
                bval = '000.00'
            frame.divepanel.bearing = bval + '*' + self.bearing_choice.GetStringSelection()
            ##
            frame.divepanel.SaveDive()
            
        diveKml.compileDiveFolders() #update kml map
        diveKml.writeKmlToServer()
        self.Destroy()

class GPSSettings(GUI.GPSSettings): #POPUP WINDOW
    def SetCtrlValues(self, evt):
        ds = Sql.DataStore(DiveRTdbFile)
        com, baud = ds.GetGPSSettings()
        if com is not None and baud is not None:
            com = int(com[3:com.__len__()])
            #print com, baud
            self.com_spinCtrl.SetValue(com)
            self.baud_comboBox.SetStringSelection(str(baud))
        ds.Close()
    
    def _evtCom(self, evt):
        if hasattr(frame, 'gps'):
            #print 'closing previous gps connection'
            frame.gps.close()
        com = 'COM' + str(self.com_spinCtrl.GetValue())
        baud = self.baud_comboBox.GetValue()
        #print 'connecting to:', com, baud
        frame.gps = GPSCom.gps(com, baud)
        
        ds = Sql.DataStore(DiveRTdbFile)
        ds.SetGPSSettings(com, baud)
        ds.Close()
    
    def _evtDone(self, evt):
        self.Destroy()

class Report(GUI.RoundReport): #POPUP WINDOW
    def _evtInit(self, evt):
        ds = Sql.DataStore(DiveRTdbFile)
        self.round_textCtrl.SetValue( str(CleanupRound) )
        self.dateRange_staticText.SetLabel( ds.GetRoundDateRange(CleanupRound) )
        self.totaltime = ds.GetTotalHours(CleanupRound)
        self.totalHours_textCtrl.SetValue(self.totaltime)
        
        ##extra diver ... ladies firt
        exDiverLst = ds.GetExtraDiverList(CleanupRound)
        diverhours = ds.GetCleanupTotals(CleanupRound)
        #get default diver percentages here... will be updated later if cleanup/round has saved data
        diverrates = ds.GetDiverRates(exDiverLst)
        
        #now get saved diver percentages
        savedDiverRates = ds.GetReportDiverDetails(CleanupRound)
        comparelst = savedDiverRates.keys()
        comparelst.reverse()
        if comparelst == exDiverLst:
            #print 'retrieving saved diver rates'
            diverrates = savedDiverRates
        
        self.diverRows = []
        self.exDiverRows = []
        for diver in exDiverLst:
            self.addExDiverRow(diver, diverhours[diver], diverrates[diver])
        if exDiverLst.__len__() == 0:
            self.extraDiver_staticline.Hide()
            self.extraDiver_staticText.Hide()
            self.exName_staticText.Hide()
            self.exHours_staticText.Hide()
            self.exPay_staticText.Hide()
            self.exGrams_staticText.Hide()
            self.exValue_staticText.Hide()
            #self.extraDiving_fgSizer.Hide()
        
        #operator / divers    
        diverLst = ds.GetOperatorDiverList(CleanupRound)
        for diver in diverLst:
            self.addDiverRow(diver, diverhours[diver])
        
        #get any saved data
        data = ds.GetReportTotals(CleanupRound)
        if data is not None:
            self.totalGrams_textCtrl.SetValue(data[1])
            self._evtSetTroyOz( None, data[1] )
            self.londonSpot_textCtrl.SetValue(data[2])
            self.percentLoss_textCtrl.SetValue(data[3])
        
        #self.SetEstTotal()
        self.updateCuts()
            
        ds.Close()
        
        self.bSizer.Fit( self )
        self.Layout()
    
    def updateCuts(self):
        gramstr = self.totalGrams_textCtrl.GetValue()
        if gramstr != '':
            totalGrams = float( gramstr )
        else:
            totalGrams = 0.0
        
        ownerPct = self.ownerPercent_textCtrl.GetValue()
        if ownerPct == "":
            ownergrams = 0.0
        else:
            ownergrams = totalGrams * ( float(ownerPct) / 100 )
        self.ownerGrams_textCtrl.SetValue( str( ownergrams ) )
        self.ownerEstimate_textCtrl.SetValue( self.grams2EstDollars(ownergrams) )
        
        operPct = self.operatorPercent_textCtrl.GetValue()
        if operPct == "":
            operatorgrams = 0.0
        else:
            operatorgrams = totalGrams * ( float(operPct) / 100 )
        self.operatorGrams_textCtrl.SetValue( str( operatorgrams ) )
        self.operatorEstimate_textCtrl.SetValue( self.grams2EstDollars( operatorgrams ) )
        
        #extra diver rows
        diverGrams = 0.0
        for row in self.exDiverRows:
            self._evtDiverPercentSet(row[0], row[1], row[2], row[3] )
            diverGrams += float( row[2].GetValue() )
            
        #set net grams
        net = float( self.operatorGrams_textCtrl.GetValue() ) - diverGrams
        self.operNetGrams_textCtrl.SetValue( str( net ) )
        
        #operator diver times
        operatorHrs = 0.0
        for row in self.diverRows:
            operatorHrs += float( row[0].GetValue() )
        for row in self.diverRows:
            pct = float( row[0].GetValue() ) / operatorHrs
            dgrams = round(pct*net, 3)
            row[1].SetValue( str( dgrams ) )
            row[2].SetValue( self.grams2EstDollars( dgrams) )
        
        #set oz per hr
        ozPerHr = round( (self.grams2TroyOz(totalGrams) / float( self.totalHours_textCtrl.GetValue() )), 2 )
        self.ozPerHr_textCtrl.SetValue( str(ozPerHr) )
        
    def addDiverRow(self, name, hours):
        divername_textCtrl = wx.TextCtrl( self, wx.ID_ANY, name, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        divername_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
        self.diving_fgSizer.Add( divername_textCtrl, 0, wx.ALL, 5 )
        
        diverhours_textCtrl = wx.TextCtrl( self, wx.ID_ANY, hours, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        diverhours_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
        self.diving_fgSizer.Add( diverhours_textCtrl, 0, wx.ALL, 5 )
        
        diverpay_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        diverpay_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
        self.diving_fgSizer.Add( diverpay_textCtrl, 0, wx.ALL, 5 )
        
        payvalue_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        payvalue_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
        self.diving_fgSizer.Add( payvalue_textCtrl, 0, wx.ALL, 5)
                
        self.diverRows.append( (diverhours_textCtrl, diverpay_textCtrl, payvalue_textCtrl, divername_textCtrl) )
    
    def addExDiverRow(self, name, hours, percent):
        divername_textCtrl = wx.TextCtrl( self, wx.ID_ANY, name, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        divername_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
        self.extraDiving_fgSizer.Add( divername_textCtrl, 0, wx.ALL, 5 )
        
        diverhours_textCtrl = wx.TextCtrl( self, wx.ID_ANY, hours, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        diverhours_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
        self.extraDiving_fgSizer.Add( diverhours_textCtrl, 0, wx.ALL, 5 )
        
        diverperct_textCtrl = wx.TextCtrl( self, wx.ID_ANY, percent, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.extraDiving_fgSizer.Add( diverperct_textCtrl, 0, wx.ALL, 5 )
        
        diverpay_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        diverpay_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
        self.extraDiving_fgSizer.Add( diverpay_textCtrl, 0, wx.ALL, 5 )
        
        payvalue_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        payvalue_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
        self.extraDiving_fgSizer.Add( payvalue_textCtrl, 0, wx.ALL, 5)
        
        diverperct_textCtrl.Bind( wx.EVT_TEXT, lambda evt, h=diverhours_textCtrl, p=diverperct_textCtrl, g=diverpay_textCtrl, e=payvalue_textCtrl, : self._evtDiverPercentSet(h, p, g, e, evt))
        
        self.exDiverRows.append( (diverhours_textCtrl, diverperct_textCtrl, diverpay_textCtrl, payvalue_textCtrl, divername_textCtrl) )
        
    def _evtDiverPercentSet(self, diverhours_textCtrl, diverperct_textCtrl, diverpay_textCtrl, payvalue_textCtrl, evt=None ):
        val = diverperct_textCtrl.GetValue()
        newval = self.floatstr(val)
        if newval != val:
            diverperct_textCtrl.SetValue(newval)
            diverperct_textCtrl.SetInsertionPointEnd()
        if newval == "":
            newval = 0.0
        
        t = self.totalGrams_textCtrl.GetValue().strip()
        if t == "":
            tgrams = 0.0
        else:
            tgrams = float ( t )
        
        t = self.totalHours_textCtrl.GetValue()
        if t == "":
            thrs = 0.0
        else:
            thrs = float( t )
            
        hrs = float( diverhours_textCtrl.GetValue() )
        pct = float( newval ) / 100.0
        if thrs != 0:
            grams = ( hrs / thrs ) * tgrams * pct
            diverpay_textCtrl.SetValue( str(round(grams, 1)) )
            payvalue_textCtrl.SetValue ( self.grams2EstDollars(grams) )
               
    def SetEstTotal(self):
        grams = self.totalGrams_textCtrl.GetValue().strip()
        if grams == '':
            grams = 0
        else:
            grams = float( grams )
        dollars = self.grams2EstDollars(grams)
        self.estTotal_textCtrl.SetValue(dollars)
        
    def grams2EstDollars(self, grams):
        percentLoss = self.percentLoss_textCtrl.GetValue()
        if percentLoss == '':
            pct = 0
        else:
            pct = float( percentLoss ) / 100.0
            
        londonSpot = self.londonSpot_textCtrl.GetValue()
        if londonSpot == '':
            spot = 0
        else:
            spot = float( londonSpot )
            
        toz = self.grams2TroyOz(grams)
            
        return '$' + '{:20,.2f}'.format( round( toz*pct*spot, 2) ).strip()
    
    def grams2TroyOz(self, grams):
        gramsPerToz = 31.1034768
        return grams / gramsPerToz
        
    def floatstr(self, somestring):
        mystr = ''
        decimal = False
        for each in somestring:
            srch = re.search(r'\d', each)
            if srch is not None:
                mystr += srch.group(0)
            srch = re.search(r'\.', each)
            if srch is not None and decimal is False:
                mystr += srch.group(0)
                decimal = True
        return mystr
        
    def _evtOwnerCut(self, evt):
        ctrl = evt.GetEventObject()
        value = ctrl.GetValue()
        newval = self.floatstr(value)
        if newval != value:
            ctrl.SetValue(newval)
            ctrl.SetInsertionPointEnd()
        if newval != '':
            pct = float(newval)
            if pct > 100:
                pct = 100
                ctrl.SetValue( '100' )
                ctrl.SetInsertionPointEnd()
            self.operatorPercent_textCtrl.SetValue( str( 100 - pct ) )
        self.updateCuts()
            
    def _evtOperatorCut(self, evt):
        ctrl = evt.GetEventObject()
        value = ctrl.GetValue()
        newval = self.floatstr(value)
        if newval != value:
            ctrl.SetValue(newval)
            ctrl.SetInsertionPointEnd()
        if newval != '':
            pct = float(newval)
            if pct > 100:
                pct = 100
                ctrl.SetValue( '100' )
                ctrl.SetInsertionPointEnd()
            self.ownerPercent_textCtrl.SetValue( str( 100 - pct ) )
        self.updateCuts()     
    
    def _evtGramsChange(self, evt):
        ctrl = evt.GetEventObject()
        #only allow numbers and  one decimal
        value = ctrl.GetValue()
        newval = self.floatstr(value)
        if newval != value:
            ctrl.SetValue(newval)
            ctrl.SetInsertionPointEnd()
        self._evtSetTroyOz( None, newval )
        #recalculate Estimated Total Value
        self.SetEstTotal()
        #recalculate each divers pay and dredge owner's total
        self.updateCuts()
        
    def _evtSetTroyOz(self, evt=None, grams=None):
        if evt != None:
            grams = self.totalGrams_textCtrl.GetValue()
        if grams != '':
            troyOz = round( (float( grams ) / 31.1034768), 3 )
            self.totalOz_textCtrl.SetValue( str(troyOz) )
    
    def _evtTozChange(self, evt):
        ctrl = evt.GetEventObject()        
        #only allow numbers and  one decimal
        value = ctrl.GetValue()
        newval = self.floatstr(value)
        if newval != value:
            ctrl.SetValue(newval)
            ctrl.SetInsertionPointEnd()
        self._evtSetGrams( None, newval )
        #recalculate Estimated Total Value
        self.SetEstTotal()
        #recalculate each divers pay and dredge owner's total
        self.updateCuts()
            
    def _evtSetGrams(self, evt=None, TroyOz=None):
        if evt != None:
            TroyOz = self.totalOz_textCtrl.GetValue()
        if TroyOz != '':
            grams = round( (float( TroyOz ) * 31.1034768), 2 )
            self.totalGrams_textCtrl.SetValue( str(grams) )
    
    def _evtPctLossChange(self, evt):
        #only allow numbers and  one decimal
        value = self.percentLoss_textCtrl.GetValue()
        newval = self.floatstr(value)
        if newval != value:
            self.percentLoss_textCtrl.SetValue(newval)
            self.percentLoss_textCtrl.SetInsertionPointEnd()
        if newval != '':
            if float(newval) > 100.0:
                self.percentLoss_textCtrl.SetValue('100')
                self.percentLoss_textCtrl.SetInsertionPointEnd()
        #recalculate Estimated Total Value
        self.SetEstTotal()
        #recalculate each divers pay
        self.updateCuts()
        
    def _evtLondonSpotChange(self, evt):
        #only allow numbers and  one decimal
        value = self.londonSpot_textCtrl.GetValue()
        newval = self.floatstr(value)
        if newval != value:
            self.londonSpot_textCtrl.SetValue(newval)
            self.londonSpot_textCtrl.SetInsertionPointEnd()
        #recalculate Estimated Total Value
        self.SetEstTotal()
        #recalculate each divers pay
        self.updateCuts()
        
    def _evtSave(self, evt):
        ds = Sql.DataStore(DiveRTdbFile)
        grams = self.totalGrams_textCtrl.GetValue()
        spot = self.londonSpot_textCtrl.GetValue()
        loss = self.percentLoss_textCtrl.GetValue()
        ds.SaveReportTotals(CleanupRound, grams, spot, loss)
        
        i=0
        exDiverLst = ds.GetExtraDiverList(CleanupRound)
        for row in self.exDiverRows:
            name = exDiverLst[i]
            rate = self.exDiverRows[i][1].GetValue()
            ds.SaveReportDiverDetails(CleanupRound, name, rate)
            i+=1
            
        ds.Close()
        self.Destroy()
        
    def _evtPrintView(self, evt):
        #templates
        top = """\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<HEAD>
    <META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=windows-1252">
    <TITLE></TITLE>
    <META NAME="GENERATOR" CONTENT="DiveRT">
    <STYLE TYPE="text/css">
    <!--
        @page { margin: 0.79in }
        P { margin-bottom: 0.08in }
        TD P { margin-bottom: 0in }
        A:link { so-language: zxx }
    -->
    </STYLE>
</HEAD>
<BODY LANG="en-US" DIR="LTR">
<P ALIGN=CENTER STYLE="margin-bottom: 0in"><B>Dive RT Report</B></P>
<P ALIGN=CENTER STYLE="margin-bottom: 0in"></P>
<P ALIGN=CENTER STYLE="margin-bottom: 0in"><I><B>Cleanup / Round %s</B></I></P>
<CENTER>
    <TABLE WIDTH=316 BORDER=1 BORDERCOLOR="#000000" CELLPADDING=4 CELLSPACING=0>
        <COL WIDTH=215>
        <COL WIDTH=83>
        <TR VALIGN=TOP>
            <TD WIDTH=215>
                <P ALIGN=CENTER>Total Dive Hours</P>
            </TD>
            <TD WIDTH=83 >
                <P ALIGN=CENTER>%s</P>
            </TD>
        </TR>
        <TR VALIGN=TOP>
            <TD WIDTH=215>
                <P ALIGN=CENTER>Total Grams Recovered</P>
            </TD>
            <TD WIDTH=83>
                <P ALIGN=CENTER>%s</P>
            </TD>
        </TR>
        <TR VALIGN=TOP>
            <TD WIDTH=215>
                <P ALIGN=CENTER>London Spot</P>
            </TD>
            <TD WIDTH=83 >
                <P ALIGN=CENTER>%s</P>
            </TD>
        </TR>
        <TR VALIGN=TOP>
            <TD WIDTH=215>
                <P ALIGN=CENTER>Estimated Refinement Recovery</P>
            </TD>
            <TD WIDTH=83>
                <P ALIGN=CENTER>%s</P>
            </TD>
        </TR>
        <TR VALIGN=TOP>
            <TD WIDTH=215>
                <P ALIGN=CENTER>Estimated Refinement Value</P>
            </TD>
            <TD WIDTH=83>
                <P ALIGN=CENTER>%s</P>
            </TD>
        </TR>
        <TR VALIGN=TOP>
            <TD WIDTH=215>
                <P ALIGN=CENTER>Troy Ounces / Hour</P>
            </TD>
            <TD WIDTH=83>
                <P ALIGN=CENTER>%s</P>
            </TD>
        </TR>
    </TABLE>    
</CENTER>
<P ALIGN=CENTER STYLE="margin-bottom: 0in"></P><P ALIGN=CENTER STYLE="margin-bottom: 0in"><I><B>Dredge Owner Cut</B></I></P>
<TABLE WIDTH=100%% BORDER=1 BORDERCOLOR="#000000" CELLPADDING=4 CELLSPACING=0>
    <COL WIDTH=51*>
    <COL WIDTH=51*>
    <COL WIDTH=51*>
    <TR VALIGN=TOP>
        <TD WIDTH=25%%>
            <P ALIGN=CENTER>Percent</P>
        </TD>
        <TD WIDTH=25%%>
            <P ALIGN=CENTER>Grams</P>
        </TD>
        <TD WIDTH=25%%>
            <P ALIGN=CENTER>Estimated Value</P>
        </TD>
    </TR>
    <TR VALIGN=TOP>
        <TD WIDTH=25%%>
            <P ALIGN=CENTER>%s</P>
        </TD>
        <TD WIDTH=25%%>
            <P ALIGN=CENTER>%s</P>
        </TD>
        <TD WIDTH=25%%>
            <P ALIGN=CENTER>%s</P>
        </TD>
    </TR>
</TABLE>
<P ALIGN=CENTER STYLE="margin-bottom: 0in"></P><P ALIGN=CENTER STYLE="margin-bottom: 0in"><I><B>Operator / Diver's Cut</B></I></P>
<TABLE WIDTH=100%% BORDER=1 BORDERCOLOR="#000000" CELLPADDING=4 CELLSPACING=0>
    <COL WIDTH=51*>
    <COL WIDTH=51*>
    <COL WIDTH=51*>
    <COL WIDTH=51*>
    <TR VALIGN=TOP>
        <TD WIDTH=25%%>
            <P ALIGN=CENTER>Percent</P>
        </TD>
        <TD WIDTH=25%%>
            <P ALIGN=CENTER>Gross Grams</P>
        </TD>
        <TD WIDTH=25%%>
            <P ALIGN=CENTER>Net Grams</P>
        </TD>
        <TD WIDTH=25%%>
            <P ALIGN=CENTER>Estimated Gross Value</P>
        </TD>
    </TR>
    <TR VALIGN=TOP>
        <TD WIDTH=25%%>
            <P ALIGN=CENTER>%s</P>
        </TD>
        <TD WIDTH=25%%>
            <P ALIGN=CENTER>%s</P>
        </TD>
        <TD WIDTH=25%%>
            <P ALIGN=CENTER>%s</P>
        </TD>
        <TD WIDTH=25%%>
            <P ALIGN=CENTER>%s</P>
        </TD>
    </TR>
</TABLE>
<P ALIGN=CENTER STYLE="margin-bottom: 0in"></P>\
""" #%( round, hours, grams, spot, percentloss, estimate, ozperhr, ownerpercent, ownergrams, ownerestimate, oppercent, opgross, opnet, opestimate  )
        
        DiveTop = """\
<P ALIGN=CENTER STYLE="margin-bottom: 0in"><I><B>Operator / Diver Distribution</B></I></P>
<TABLE WIDTH=100% BORDER=1 BORDERCOLOR="#000000" CELLPADDING=4 CELLSPACING=0>
    <COL WIDTH=51*>
    <COL WIDTH=51*>
    <COL WIDTH=51*>
    <COL WIDTH=51*>
    <TR VALIGN=TOP>
        <TD WIDTH=20%>
            <P ALIGN=CENTER>Diver Name</P>
        </TD>
        <TD WIDTH=20%>
            <P ALIGN=CENTER>Diver Hours</P>
        </TD>
        <TD WIDTH=20%>
            <P ALIGN=CENTER>Grams</P>
        </TD>
        <TD WIDTH=20%>
            <P ALIGN=CENTER>Estimated Value</P>
        </TD>
    </TR>
"""
        
        Dive = """\
    <TR VALIGN=TOP>
        <TD WIDTH=20%%>
            <P ALIGN=CENTER>%s</P>
        </TD>
        <TD WIDTH=20%% >
            <P ALIGN=CENTER>%s</P>
        </TD>
        <TD WIDTH=20%% >
            <P ALIGN=CENTER>%s</P>
        </TD>
        <TD WIDTH=20%% >
            <P ALIGN=CENTER>%s</P>
    </TR>
""" #%( name, hours, grams, estimate)

        exDiveTop = """\
<P ALIGN=CENTER STYLE="margin-bottom: 0in"><I><B>Extra Divers</B></I></P>
<TABLE WIDTH=100% BORDER=1 BORDERCOLOR="#000000" CELLPADDING=4 CELLSPACING=0>
    <COL WIDTH=51*>
    <COL WIDTH=51*>
    <COL WIDTH=51*>
    <COL WIDTH=51*>
    <COL WIDTH=51*>
    <TR VALIGN=TOP>
        <TD WIDTH=20%>
            <P ALIGN=CENTER>Diver Name</P>
        </TD>
        <TD WIDTH=20%>
            <P ALIGN=CENTER>Diver Hours</P>
        </TD>
        <TD WIDTH=20%>
            <P ALIGN=CENTER>% of time</P>
        </TD>
        <TD WIDTH=20%>
            <P ALIGN=CENTER>Grams</P>
        </TD>
        <TD WIDTH=20%>
            <P ALIGN=CENTER>Estimated Value</P>
        </TD>
    </TR>
"""
        
        exDive = """\
    <TR VALIGN=TOP>
        <TD WIDTH=20%%>
            <P ALIGN=CENTER>%s</P>
        </TD>
        <TD WIDTH=20%% >
            <P ALIGN=CENTER>%s</P>
        </TD>
        <TD WIDTH=20%% >
            <P ALIGN=CENTER>%s</P>
        </TD>
        <TD WIDTH=20%% >
            <P ALIGN=CENTER>%s</P>
        </TD>
        <TD WIDTH=20%% >
            <P ALIGN=CENTER>%s</P>
        </TD>
    </TR>
""" #%( name, hours, rate, grams, estimate)
            
        bottom = """\
<P ALIGN=CENTER STYLE="margin-bottom: 0in"><BR>
</P>
</BODY>
</HTML>
"""
        
        #compile templates
        top = top %( self.round_textCtrl.GetValue() + '<BR>' + self.dateRange_staticText.GetLabel(), 
                     self.totalHours_textCtrl.GetValue(), 
                     self.totalGrams_textCtrl.GetValue(), 
                     self.londonSpot_textCtrl.GetValue(), 
                     self.percentLoss_textCtrl.GetValue(), 
                     self.estTotal_textCtrl.GetValue(),
                     self.ozPerHr_textCtrl.GetValue(),
                     self.ownerPercent_textCtrl.GetValue(),
                     self.ownerGrams_textCtrl.GetValue(),
                     self.ownerEstimate_textCtrl.GetValue(),
                     self.operatorPercent_textCtrl.GetValue(),
                     self.operatorGrams_textCtrl.GetValue(),
                     self.operNetGrams_textCtrl.GetValue(),
                     self.operatorEstimate_textCtrl.GetValue() )
        
        for row in self.diverRows:
            DiveTop += Dive %( row[3].GetValue(),
                               row[0].GetValue(),
                               row[1].GetValue(),
                               row[2].GetValue() )
        DiveTop += "</TABLE>"
        
        if self.exDiverRows.__len__() > 0:
            for row in self.exDiverRows:
                exDiveTop += exDive %( row[4].GetValue(),
                                       row[0].GetValue(),
                                       row[1].GetValue(),
                                       row[2].GetValue(),
                                       row[3].GetValue() )
            exDiveTop += "</TABLE>"
        else:
            exDiveTop = ""
         
        #write to html file
        filepath = DiveRTDir+'\\DiveRT_R%s.html' %( self.round_textCtrl.GetValue())
        fd = open( filepath, 'w' )
        fd.write( top+DiveTop+exDiveTop+bottom )
        fd.close()
        os.startfile( filepath )
        #open file in default browser
        
    def _evtClose(self, evt):
        self.Destroy()

class CrewManager(wx.Dialog): #POPUP WINDOW   
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Crew Manager", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        self.bxSizer1 = wx.BoxSizer( wx.VERTICAL)
        #self.bxSizer2 = wx.BoxSizer( wx.VERTICAL )
        self.fgSizer = wx.FlexGridSizer( 99, 4, 0, 0 )
        self.fgSizer.SetFlexibleDirection( wx.BOTH )
        self.fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.rowNumber = 0
        self.rowStack = []
        
        self.bxSizer1.Add( self.fgSizer, 1, wx.EXPAND, 5)
        #self.bxSizer2.Add( self.fgSizer, 1, wx.EXPAND, 5 )
        
        self.addStaticControls()

        datastore = Sql.DataStore(DiveRTdbFile)
        crewlist = datastore.GetCrewList()
        for each in crewlist:
            self.addRow( each[1], each[2], int(each[3]) )
            tendRate = each[4]
        self.tenderRate_textCtrl.SetValue(tendRate)
        #print crewlist
        datastore.Close()
        self.addRow()
        
        self.Centre( wx.BOTH )
        
    def addStaticControls(self):
        name_staticText = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        name_staticText.Wrap( -1 )
        self.fgSizer.Add( name_staticText, 0, wx.ALL, 5 )
        
        duty_staticText = wx.StaticText( self, wx.ID_ANY, u"Duty", wx.DefaultPosition, wx.DefaultSize, 0 )
        duty_staticText.Wrap( -1 )
        self.fgSizer.Add( duty_staticText, 0, wx.ALL, 5 )
        
        diveRate_staticText = wx.StaticText( self, wx.ID_ANY, u"Dive Rate  (% of time)", wx.DefaultPosition, wx.DefaultSize, 0 )
        diveRate_staticText.Wrap( -1 )
        self.fgSizer.Add( diveRate_staticText, 0, wx.ALL, 5 )
        
        self.fgSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticline16 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        self.bxSizer1.Add( self.m_staticline16, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.tenderRate_staticText = wx.StaticText( self, wx.ID_ANY, u"Tending Rate ($/hr)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.tenderRate_staticText.Wrap( -1 )
        self.bxSizer1.Add( self.tenderRate_staticText, 0, wx.ALL, 5 )
        
        self.tenderRate_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.bxSizer1.Add( self.tenderRate_textCtrl, 0, wx.ALL, 5)
        
        fgs = wx.FlexGridSizer( 1, 2, 0, 0 )
        fgs.SetFlexibleDirection( wx.BOTH )
        fgs.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        self.bxSizer1.Add( fgs, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.save_button = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgs.Add( self.save_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        self.save_button.Bind(wx.EVT_BUTTON, self._evtSave)
        
        self.cancel_button = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgs.Add( self.cancel_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        self.cancel_button.Bind( wx.EVT_BUTTON, self._evtClose )
        
        self.Bind( wx.EVT_CLOSE, self._evtClose )
        self.tenderRate_textCtrl.Bind( wx.EVT_TEXT, self._evtTendRateTxt )
        
    def addRow(self, Name="", Duty="Extra Diver", DiveRate=45):
        #print 'adding row#', self.rowNumber
        name_textCtrl = wx.TextCtrl( self, wx.ID_ANY, Name, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.fgSizer.Add( name_textCtrl, 0, wx.ALL, 5 )
        
        duty_choiceChoices = [ u"Operator Diver", u"Extra Diver", u"Tender" ]
        duty_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, duty_choiceChoices, 0 )
        duty_choice.SetStringSelection(Duty)
        self.fgSizer.Add( duty_choice, 0, wx.ALL, 5 )
        
        diveRate_spinCtrl = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 25, 100, 45 )
        diveRate_spinCtrl.SetValue(DiveRate)
        self.fgSizer.Add( diveRate_spinCtrl, 0, wx.ALL, 5 )
        
        delete_button = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.fgSizer.Add( delete_button, 0, wx.ALL, 5 )
        
        self.SetSizer( self.bxSizer1)
        self.Layout()
        self.bxSizer1.Fit( self )
        
        self.rowStack.append([name_textCtrl, duty_choice, diveRate_spinCtrl, delete_button])
        name_textCtrl.Bind( wx.EVT_TEXT, lambda evt, rownum=self.rowNumber: self._evtNameTxt(evt, rownum))
        duty_choice.Bind( wx.EVT_CHOICE, lambda evt, rownum=self.rowNumber: self._evtDuty(evt, rownum))
        delete_button.Bind( wx.EVT_BUTTON, lambda evt, rownum=self.rowNumber: self._evtDelete(evt, rownum))
        delete_button.Disable()
        self.rowStack[self.rowNumber-1][3].Enable()
        self._evtDuty(None, self.rowNumber)
        self.rowNumber += 1
        
    def deleteRow(self, rownum):
        #print 'deleting row: ', rownum
        listofdestroy = self.rowStack[rownum]
        for each in listofdestroy:
            each.Destroy()
            
        self.rowStack.pop(rownum)
        self.rowStack.insert(rownum, None)
        
        self.SetSizer( self.bxSizer1)
        self.Layout()
        self.bxSizer1.Fit( self )
    
    def _evtDuty(self, evt, rownum):
        rowobjlst = self.rowStack[rownum]
        if rowobjlst[1].GetStringSelection() == "Extra Diver":
            rowobjlst[2].Enable() #diveRate_spinCtrl.Enable()
        else:
            rowobjlst[2].Disable()
    
    def floatstr(self, somestring):
        mystr = ''
        decimal = False
        for each in somestring:
            srch = re.search(r'\d', each)
            if srch is not None:
                mystr += srch.group(0)
            srch = re.search(r'\.', each)
            if srch is not None and decimal is False:
                mystr += srch.group(0)
                decimal = True
        return mystr
    
    def _evtNameTxt(self, evt, rownum):
        #print 'typing in: ', rownum
        if rownum == self.rowNumber - 1:
            self.addRow()
            
    def _evtTendRateTxt(self, evt):
        #only allow numbers and  one decimal
        ctrl = evt.GetEventObject()
        value = ctrl.GetValue()
        newval = self.floatstr(value)
        if newval != value:
            ctrl.SetValue(newval)
            ctrl.SetInsertionPointEnd()
        if newval != '':
            ctrl.SetInsertionPointEnd()
            
    def _evtDelete(self, evt, rownum):
        self.deleteRow(rownum)
        
    def _evtSave(self, evt):
        condition1 = False
        condition2 = True
        for each in self.rowStack[0:-1]: #don't allow null stacks or empty names
            if each is not None:
                if each[0].GetValue().strip() != "":
                    condition1 = True #non empty name found
                else:
                    condition2 = False #empty name found
                    
        if condition1 and condition2 and (self.tenderRate_textCtrl.GetValue() != ""):
            datastore = Sql.DataStore(DiveRTdbFile)
            datastore.DropCrewData()
            for each in self.rowStack[0:-1]:
                if each is not None:
                    #print each[0].GetValue(), each[1].GetStringSelection(), each[2].GetValue(), each[3].GetValue()
                    datastore.AddCrew(each[0].GetValue(), each[1].GetStringSelection(), each[2].GetValue(), self.tenderRate_textCtrl.GetValue() )
            datastore.Close()
            frame.divepanel.updateDiverTenderChoice()
            frame.divepanel.diver_choice.SetSelection(0)
            frame.divepanel.tender_choice.SetSelection(0)
            self.Destroy()
    
    def _evtClose(self, evt):
        self.Destroy()

class About(GUI.About): #POPUP WINDOW
    def _evtOK(self, evt):
        global aboutok
        aboutok = True
        frame.Show()
        self.Destroy()

class DataPanel(GUI.DataPanel): #AUI PANEL
    def init(self):
        self.Ticker()
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Ticker, self.timer)
        self.timer.Start(1000)
        
        ds = Sql.DataStore(DiveRTdbFile)
        com, baud = ds.GetGPSSettings()
        if com is not None and baud is not None:
            frame.gps = GPSCom.gps(com, baud)
        ds.Close()
        
    def Ticker(self, evt=None):
        now = time.localtime()
        fmtnow = time.strftime('%A %I:%M:%S %p', now)
        self.date_staticText.SetLabel(fmtnow)
        if hasattr(frame, 'gps'):
            lat = frame.gps.fmt_lat('DDD')
            lon = frame.gps.fmt_lon('DDD')
            if lat is not None and lon is not None:
                #frame.divepanel.lat = unicode(lat)
                #frame.divepanel.long = unicode(long)
                self.lat_staticText.SetLabel(unicode(lat))
                self.long_staticText.SetLabel(unicode(lon))
            bearing = frame.gps.fmt_bearing()
            if bearing != 'None':
                #frame.divepanel.bearing = unicode(bearing)
                self.bearing_staticText.SetLabel(unicode(bearing))
            
            #generate kml current and start positions
            if ( lat != None ) and ( lon != None ):
                latitude = float( lat.split('*')[0] )
                if lat.split('*')[1] == 'S':
                    latitude = -latitude
                longitude = float ( lon.split('*')[0] )
                if lon.split('*')[1] == 'W':
                    longitude = -longitude
                if bearing == 'None':
                    shipIcon = "circle"
                    heading = 0.0
                else:
                    heading = float ( bearing.split('*')[0] )
                    shipIcon ="arrow"    
                    if bearing.split('*')[1] == 'M':
                        heading += frame.divepanel.bearingVariance
                    #print latitude, longitude, heading
                startLatitude = float( frame.divepanel.lat.split('*')[0] )
                if frame.divepanel.lat.split('*')[1] == 'S':
                    startLatitude = -startLatitude
                startLongitude = float ( frame.divepanel.long.split('*')[0] )
                if frame.divepanel.long.split('*')[1] == 'W':
                    startLongitude = -startLongitude
                if frame.divepanel.bearing != 'None':
                    startHeading = float ( frame.divepanel.bearing.split('*')[0] )
                else:
                    startHeading = 0.0
                #print frame.divepanel.lat, frame.divepanel.long, frame.divepanel.bearing
                diveKml.compileLocationFolders( heading, longitude, latitude, startHeading, startLongitude, startLatitude, shipIcon)
                diveKml.writeKmlToServer()
        frame.divepanel.CalcTimeUW()

class DivePanel(GUI.DivePanel): #AUI PANEL frame.divepanel
    def init(self):
        self.lat = '00.0000000*'
        self.long = '000.0000000*'
        self.bearing = '000.00*'
        self.bearingVariance = 12.3
        self.notes = ''
        
        self.updateDiverTenderChoice()
        
        self.tender = self.tender_choice.GetStringSelection()
        self.diver = self.diver_choice.GetStringSelection()
        
    def updateDiverTenderChoice(self):
        ds = Sql.DataStore(DiveRTdbFile)
        self.diver_choice.SetItems(ds.GetBasicDiverList())
        self.tender_choice.SetItems(ds.GetBasicTenderList())
        
        ds.Close()
        
        if hasattr(self, 'tender'):
            self.tender_choice.SetStringSelection(self.tender)
        else:
            self.tender_choice.SetSelection(0)
            
        if hasattr(self, 'diver'):
            self.diver_choice.SetStringSelection(self.diver)
        else:
            self.diver_choice.SetSelection(0)
              
    def SecondsToHMString(self, seconds):
        minutes = seconds/60
        hours = int(minutes/60)
        minutes = int(minutes-hours*60)
        seconds = int(seconds-(minutes*60)-(hours*3600))
        return str(hours) + ':' + str(minutes) + ':' + str(seconds)
        
    def CalcTimeUW(self):
        times = frame.listpanel.times_listBox.GetItems()
        seconds = 0
        for each in times:
            if each.__len__() > 11:
                start = time.mktime(time.strptime(each[0:9] +' 1970', "%I:%M %p %Y"))
                stop = time.mktime(time.strptime(each[12:25] +' 1970', "%I:%M %p %Y"))
                seconds += stop-start
            else:
                start = time.mktime(time.strptime(each[0:11] +' 1970', "%I:%M %p %Y"))
                now = time.strftime('%I:%M:%S %p', time.localtime())
                stop = time.mktime(time.strptime(now +' 1970', "%I:%M:%S %p %Y"))
                seconds += stop-start
        if seconds < 0:
            seconds = seconds + 86400 #24 hours
        self.total_textCtrl.SetLabel(self.SecondsToHMString(seconds))
        
        try:
            hsec = int(self.TargetHr_textCtrl.GetValue())*3600
        except ValueError:
            hsec = 0
        try:
            msec = int(self.TargetMin_textCtrl.GetValue())*60
        except ValueError:
            msec = 0
        seconds = (hsec + msec) - seconds
        if seconds >= 0:
            self.countdown_textCtrl.SetLabel(self.SecondsToHMString(seconds))
        else:
            self.countdown_textCtrl.SetLabel('Target Reached!')
            
    def _evtTargetHr(self, evt):
        val = str(self.TargetHr_textCtrl.GetValue())
        newval = sub(r'\D+', '', val) #remove any non digits
        if newval != val:
            self.TargetHr_textCtrl.SetValue(newval)
            self.TargetHr_textCtrl.SetInsertionPointEnd()
    
    def _evtTargetMin(self, evt):
        min = str(self.TargetMin_textCtrl.GetValue())
        newmin = sub(r'\D+', '', min) #remove any non digits
        if newmin != min:
            self.TargetMin_textCtrl.SetValue(newmin)
            self.TargetMin_textCtrl.SetInsertionPointEnd()
            
    def _evtStartStop(self, evt):
        val = self.startstop_button.GetLabel()
        now = time.strftime('%I:%M %p', time.localtime())
        if val == 'Start Dive':
            #print 'Starting Dive'
            if hasattr(frame, 'gps'):
                lat = frame.gps.fmt_lat('DDD')
                long = frame.gps.fmt_lon('DDD')
                if lat is not None and long is not None:
                    frame.divepanel.lat = unicode(lat)
                    frame.divepanel.long = unicode(long)
                bearing = frame.gps.fmt_bearing()
                if bearing is not 'None':
                    frame.divepanel.bearing = unicode(bearing)
            #print 'Locking in coordinates', frame.divepanel.lat, frame.divepanel.long, frame.divepanel.bearing
            ##force last cleanup and current date
            frame.grid.cround_choice.SetSelection( frame.grid.cround_choice.GetItems().__len__()-1 )
            self.datePicker.SetValue( wx.DateTime_Now() )
            frame.grid._evtRoundChange()
            ##disable round change
            frame.grid.cround_choice.Disable()
            frame.grid.newRound_button.Disable()
            ##
            frame.listpanel.edit_Button.Enable()
            frame.listpanel.delete_Button.Enable()
            frame.listpanel.times_listBox.Append(now)
            frame.listpanel.insert_Button.Enable(False)
            self.diver_choice.Disable()
            self.datePicker.Disable()
            self.startstop_button.SetLabel('Stop Dive')
            self.status_textCtrl.SetValue('Dive in progress')
        else:
            #print 'Stopping Dive'
            lst = frame.listpanel.times_listBox.GetItems()
            start = lst[-1]
            dex = lst.__len__()-1
            frame.listpanel.times_listBox.SetString(dex, start + ' to ' + now)
            frame.listpanel.insert_Button.Enable()
            self.diver_choice.Enable()
            self.datePicker.Enable()
            self.startstop_button.SetLabel('Start Dive')
            self.status_textCtrl.SetValue('Dive stopped')
            if evt is not None: #evt is None only when dive cancelled from ConfirmDlg
                #print 'Saving Dive to database'
                self.SaveDive()
            #print 'Resetting coordinates'
            frame.divepanel.lat = '00.0000000*'
            frame.divepanel.long = '000.0000000*'
            frame.divepanel.bearing = '000.00*'
            ##disable round change
            frame.grid.cround_choice.Enable()
            frame.grid.newRound_button.Enable()
            ##
            
        nsel = frame.listpanel.times_listBox.GetItems().__len__()-1
        frame.listpanel.times_listBox.SetSelection(nsel)
        if evt is not None:
            evt.Skip()
        
    def _evtTenderChoice(self, evt):
        self.tender = self.tender_choice.GetStringSelection()
        #print 'tender selected:', self.tender
        
    def _evtDiverChoice(self, evt=None):
        self.diver = self.diver_choice.GetStringSelection()
        date = self.datePicker.GetValue().Format('%b %d %Y')
        #print 'diver selected:', self.diver
        #print 'date selected:', date
        #see if there is anything in the database:
        datastore = Sql.DataStore(DiveRTdbFile)
        data = datastore.GetDiverDateSQLData(self.diver, date, CleanupRound)
        #print data
        frame.listpanel.times_listBox.Clear()
        frame.listpanel.diveidlst = []
        if data != []:
            frame.listpanel.edit_Button.Enable()
            frame.listpanel.delete_Button.Enable()
        else:
            frame.listpanel.edit_Button.Disable()
            frame.listpanel.delete_Button.Disable()
        for each in data:
            start = each[4]
            stop = each[5]
            lastid = each[0]
            frame.listpanel.times_listBox.Append(start + ' to ' + stop)
            frame.listpanel.diveidlst.append(lastid)
        #print 'dive recordIDs in listbox: ', frame.listpanel.diveidlst
        nsel = frame.listpanel.times_listBox.GetItems().__len__()-1
        frame.listpanel.times_listBox.SetSelection(nsel)
        datastore.Close()
        
    def _evtDateChange(self,evt):
        self._evtDiverChoice()
        
    def SaveDive(self):
        datastore = Sql.DataStore(DiveRTdbFile)
        date = self.datePicker.GetValue().Format('%b %d %Y')
        lastitem = frame.listpanel.times_listBox.GetItems()[-1]
        start = lastitem[0:8]
        stop = lastitem[12:20]
        lastid = datastore.AppendDive(CleanupRound, date, self.diver, start, stop, self.lat, self.long, self.bearing, self.notes, self.tender)
        frame.listpanel.diveidlst.append(lastid) #track IDs of dives in list so records can be deleted
        datastore.Close()
        frame.grid._evtRefresh(None)
        diveKml.compileDiveFolders()
        diveKml.writeKmlToServer()
        #print frame.listpanel.diveidls

class CustomDataTable(gridlib.PyGridTableBase): #BEGIN GRID STUFF
    def __init__(self, cleanupNumber, dbfile):
        gridlib.PyGridTableBase.__init__(self)
        self.DataStore = Sql.DataStore(dbfile)
        self.GetData(cleanupNumber)
        
        self.dataTypes = [gridlib.GRID_VALUE_DATETIME,
                          gridlib.GRID_VALUE_STRING,
                          gridlib.GRID_VALUE_STRING,
                          gridlib.GRID_VALUE_STRING,
                          gridlib.GRID_VALUE_STRING
                          ]
        
        self.DataStore.Close()
        
    def GetData(self, cleanupNumber):
        #columns
        self.colLabels = ['Dive Date']
        for diver in self.DataStore.GetDiverList(cleanupNumber):
            self.colLabels.append(diver)
        self.colLabels.append('Dives Totals')  
        #rows     
        self.data = self.DataStore.GetDataTable(cleanupNumber)
        
    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.data[0])

    def IsEmptyCell(self, row, col):
        try:
            return not self.data[row][col]
        except IndexError:
            return True

    def GetValue(self, row, col): # Get/Set values in the table.
        try:
            return self.data[row][col]
        except IndexError:
            return ''

    def GetColLabelValue(self, col):
        return self.colLabels[col]

class CustTableGrid(gridlib.Grid): #GRID STUFF
    def __init__(self, parent, dbfile, cleanup=0):
        gridlib.Grid.__init__(self, parent, -1)
        
        if cleanup == 0:
            ds = Sql.DataStore(dbfile)
            cleanup = ds.GetLastCleanupRound()
            ds.Close()
        #print 'grid using cleanup #', cleanup
        table = CustomDataTable(cleanup, dbfile)

        # The second parameter means that the grid is to take ownership of the
        # table and will destroy it when done.  Otherwise you would need to keep
        # a reference to it and call it's Destroy method later.
        self.SetTable(table, True)

        self.SetRowLabelSize(0) #hides row labels row
        #self.SetMargins(0,0)
        self.EnableEditing(False)
        self.EnableDragColMove(False)
        self.EnableDragColSize(False)
        self.EnableDragRowSize(False)
        self.EnableDragGridSize(False)
        self.FormatCells()
        
        self.AutoSizeColumns(True)
        self.AutoSizeRows(True)
        self.Bind(gridlib.EVT_GRID_CELL_LEFT_CLICK, self.onCellSelect)

    def onCellSelect(self, event):
        self.ClearSelection()
        col = event.GetCol()
        row = event.GetRow()
        self.SetGridCursor(row, col)
        day = self.GetCellValue(row, 0)
        #print self.GetRowLabelValue(row)
        name = self.GetColLabelValue(col)
        if frame.divepanel.startstop_button.GetLabel() == 'Start Dive':
            if (name != "Dive Date") == (name != "Dives Totals") == (day != "Totals"):
                #print name, day
                frame.divepanel.diver_choice.SetStringSelection(name)
                
                str_strptime = time.strptime(day, '%b %d %Y')
                month = int(time.strftime('%m', str_strptime))
                day = int(time.strftime('%d', str_strptime))
                year = int(time.strftime('%Y', str_strptime))
                wxdate = wx.DateTime()
                wxdate.Set(day, month-1, year)
                frame.divepanel.datePicker.SetValue( wxdate )
                frame.divepanel._evtDiverChoice()
            else:
                frame.divepanel.datePicker.SetValue( wx.DateTime_Now() )
                if (name != "Dive Date") == (name != "Dives Totals"):
                    frame.divepanel.diver_choice.SetStringSelection(name)
                frame.divepanel._evtDiverChoice()
            
        
    def FormatCells(self):
        #cell formating
        lastrow = self.GetNumberRows()-1
        lastcol = self.GetNumberCols()-1
        
        #ALL / EVEN ROWS
        attr = gridlib.GridCellAttr()
        LIGHTGREY = wx.Colour(235,235,235)
        attr.SetBackgroundColour(LIGHTGREY)
        for rownum in range(lastrow):
            if rownum%2 != 0:
                self.SetRowAttr(rownum, attr)
            
        ##LAST ROW
        DARKGREY = wx.Colour(117,117,117)
        attr = gridlib.GridCellAttr()
        attr.SetTextColour(wx.WHITE)
        attr.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        attr.SetBackgroundColour(DARKGREY)
        self.SetRowAttr(lastrow, attr)
        
        #LAST CELL
        DARKRED = wx.Colour(127,0,0)
        self.SetCellTextColour(lastrow, lastcol, DARKRED)

class GridGridPanel( scrolled.ScrolledPanel ): #GRID STUFF
    def __init__( self, parent ):
        scrolled.ScrolledPanel.__init__( self, parent, -1)
        self.bSizer = wx.BoxSizer( wx.VERTICAL )
        self.grid = CustTableGrid(self,  'C:\ProgramData\DiveRT\DiveRT.db')
        self.bSizer.Add( self.grid, 0, wx.ALL, 5 )
        self.SetSizer( self.bSizer )
        self.SetAutoLayout(1)
        self.SetupScrolling()        

class GridPanel ( wx.Panel ): #END GRID STUFF
    def __init__( self, parent ):
        wx.Panel.__init__( self, parent, -1)
        
        self.bSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Dive Table", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )
        self.m_staticText19.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
        
        self.bSizer.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_staticline36 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        self.bSizer.Add( self.m_staticline36, 0, wx.EXPAND |wx.ALL, 5 )
        
        fgSizer12 = wx.FlexGridSizer( 1, 5, 0, 0 )
        fgSizer12.SetFlexibleDirection( wx.BOTH )
        fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText39 = wx.StaticText( self, wx.ID_ANY, u"Cleanup / Round", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText39.Wrap( -1 )
        fgSizer12.Add( self.m_staticText39, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        cround_choiceChoices = []
        self.cround_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 50,-1 ), cround_choiceChoices, 0 )
        self.cround_choice.SetSelection( 0 )
        fgSizer12.Add( self.cround_choice, 0, wx.ALL, 5 )
        
        self.newRound_button = wx.Button( self, wx.ID_ANY, u"Start New Round", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer12.Add( self.newRound_button, 0, wx.ALL, 5 )
        
        self.report_button = wx.Button( self, wx.ID_ANY, u"View Round Report", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer12.Add( self.report_button, 0, wx.ALL, 5 )
        
        #self.map_button = wx.Button( self, wx.ID_ANY, u"View Map", wx.DefaultPosition, wx.DefaultSize, 0 )
        #fgSizer12.Add( self.map_button, 0, wx.ALL, 5 )
        
        self.bSizer.Add( fgSizer12, 0, 0, 5 )
        
        self.hline = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        self.bSizer.Add( self.hline, 0, wx.EXPAND|wx.ALL, 5 )
        self.grid = GridGridPanel( self )        
        self.bSizer.Add( self.grid, 1, wx.EXPAND|wx.ALL, 5 )
        self.SetSizer( self.bSizer )
        self.SetAutoLayout(1)
        
        # Connect Events
        self.cround_choice.Bind( wx.EVT_CHOICE, self._evtRoundChange )
        self.newRound_button.Bind( wx.EVT_BUTTON, self._evtNewRound )
        self.report_button.Bind( wx.EVT_BUTTON, self._evtReport )
        #self.map_button.Bind( wx.EVT_BUTTON, self._evtMap )   
    
    def _evtRefresh(self, evt=None):
        self.grid.grid.Table = Grid.CustomDataTable(CleanupRound, DiveRTdbFile)
        self.grid.grid.FormatCells()
        self.grid.grid.AutoSizeColumns(True)
        self.grid.grid.AutoSizeRows(True)
        msg = gridlib.GridTableMessage(self.grid.grid.Table, gridlib.GRIDTABLE_REQUEST_VIEW_GET_VALUES)
        self.grid.grid.Table.GetView().ProcessTableMessage(msg)
        self.grid.SetSizer( self.grid.bSizer )
        self.grid.Layout()
        #self.grid.SetAutoLayout(1)
        self.grid.SetupScrolling()
        if (self.grid.grid.Table.GetNumberCols() == 2) and (self.cround_choice.GetSelection() == self.cround_choice.GetItems().__len__()-1):
            self.newRound_button.SetLabel( u"Cancel New Round" )
        else:
            self.newRound_button.SetLabel( u"Start New Round" )
    
    def updateRoundChoices(self):
        datastore = Sql.DataStore(DiveRTdbFile)
        self.cround_choice.SetItems(datastore.GetBasicCleanupList())
        datastore.Close()
        self.cround_choice.SetSelection(CleanupRound-1)
        
    def _evtRoundChange(self, evt=None):
        global CleanupRound
        round = self.cround_choice.GetStringSelection()
        CleanupRound = int(round)
        frame.divepanel._evtDiverChoice() #refresh dive list
        self._evtRefresh() #refresh grid
            
    def _evtNewRound(self, evt):
        global CleanupRound
        
        if self.newRound_button.GetLabel() == u"Start New Round":
            self.flag = False
            confirm = SimpleConfirmDlg(self)
            confirm.changeMessage( u"Are you sure you want to start a new dive round?" )
            confirm.ShowModal()
            while confirm.IsModal():
                wx.Sleep(.1)
            if self.flag:
                ds = Sql.DataStore(DiveRTdbFile)
                CleanupRound = ds.GetLastCleanupRound()+1
                if self.cround_choice.GetItems().count(str(CleanupRound)) == 0:
                    self.cround_choice.Append(str(CleanupRound))
                self.cround_choice.SetSelection(CleanupRound-1)
                self._evtRoundChange()
                ds.Close()
                if self.cround_choice.GetSelection() == self.cround_choice.GetItems().__len__()-1:
                    self.newRound_button.SetLabel( u"Cancel New Round")
        else:
            CleanupRound = CleanupRound - 1
            self.cround_choice.Delete( CleanupRound )
            self.cround_choice.SetSelection( CleanupRound-1 )
            self._evtRoundChange()
            self.newRound_button.SetLabel( u"Start New Round")
        
    def _evtReport(self, evt):
        check = False
        ds = Sql.DataStore(DiveRTdbFile)
        if ds.GetTotalHours( CleanupRound ) != "0.0":
            report = Report(None)
            report.SetPosition( wx.Point(-1,0) )
            report.ShowModal()
        else:
            msgDlg = MsgDialog( self )
            msgDlg.changeMessage( u"There is zero dive time in this round. \n Report is not available.")
            msgDlg.ShowModal()
        ds.Close()
        
class DetailPanel(GUI.DetailPanel): #AUI PANEL
    def init(self):
        self.diveidlst = []
        
    def _evtInsEntry(self, evt):
        EditDialog = EditDlg(None)
        EditDialog.CenterOnParent()
        EditDialog.SetTitle('Insert Dive Record')
        EditDialog.EnableFullEdit()
        EditDialog.InsertFillValues()
        EditDialog.ShowModal()
        
    def _evtDeleteEntry(self, evt):
        ConfirmDialog = ConfirmDlg(None)
        ConfirmDialog.cancelButton.SetFocus()
        ConfirmDialog.CentreOnParent()
        ConfirmDialog.ShowModal()
        
    def _evtEditEntry(self, evt):
        selStr = self.times_listBox.GetStringSelection()
        EditDialog = EditDlg(None)
        EditDialog.CenterOnParent()
        if selStr.__len__() == 8: #only has start time
            EditDialog.EnableFullEdit(False)
        if selStr.__len__() == 20: #has start and stop time
            dex = frame.listpanel.times_listBox.GetSelection()
            #print 'editing recordID', frame.listpanel.diveidlst[dex]
            EditDialog.IsFullEdit = True
            EditDialog.EnableFullEdit()
        EditDialog.EditFillValues()
        EditDialog.ShowModal()

class AUIFrame(wx.Frame): #AUI FRAME
    def __init__(self, parent, id=-1, title='Dive Recovery Tracker',
                 pos=wx.DefaultPosition, size=(1300, 700),
                 style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        self._mgr = wx.aui.AuiManager(self)
        self._mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT|wx.aui.AUI_MGR_TRANSPARENT_DRAG)
        self.CreateMenu()
        self.grid = GridPanel(self) #create grid panel
        self.datapanel = DataPanel(self) #create data panel
        self.divepanel = DivePanel(self) #create dive panel
        self.divepanel.init()
        self.listpanel = DetailPanel(self) #create list panel
        self.listpanel.init() 
        self.DefaultLayout()
        self.BindEvents()
        
    def CreateMenu(self):
        self.MenuBar = wx.MenuBar( 0 )
        self.file_menu = wx.Menu()
        self.map_menu = wx.Menu()
        
        #self.export_menuItem = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Export Map", wx.EmptyString, wx.ITEM_NORMAL )
        #self.file_menu.AppendItem( self.export_menuItem )
        
        ###Menu menu
        self.managedivers_menuItem = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Manage Divers && Tenders", wx.EmptyString, wx.ITEM_NORMAL )
        self.file_menu.AppendItem( self.managedivers_menuItem )
        
        self.gps_menuItem = wx.MenuItem( self.file_menu, wx.ID_ANY, u"GPS Settings", wx.EmptyString, wx.ITEM_NORMAL )
        self.file_menu.AppendItem( self.gps_menuItem )
        
        self.quit_menuItem = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Quit", wx.EmptyString, wx.ITEM_NORMAL )
        self.file_menu.AppendItem( self.quit_menuItem )
        
        self.about_menuItem = wx.MenuItem( self.file_menu, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
        self.file_menu.AppendItem( self.about_menuItem )
        
        self.MenuBar.Append( self.file_menu, u"Menu" )
        self.MenuBar.Append( self.map_menu, u"Map" )
        self.SetMenuBar( self.MenuBar )
        
        ###Map menu items
        self.viewmap_menuItem = wx.MenuItem( self.map_menu, wx.ID_ANY, u"View Map in Google Earth", wx.EmptyString, wx.ITEM_NORMAL )
        self.map_menu.AppendItem( self.viewmap_menuItem )
                
    def DefaultLayout(self):
        # add the panes to the manager
        self._mgr.AddPane(self.listpanel, wx.aui.AuiPaneInfo().Layer(0).
                          MinSize(self.listpanel.GetBestSize()).
                          Caption("Dive List Panel").
                          CloseButton(False).
                          MaximizeButton(False).
                          Right().
                          Name('divelist'))
        self.divelistPane = self._mgr.GetPane('divelist')
        
        self._mgr.AddPane(self.datapanel, wx.aui.AuiPaneInfo().Layer(1).
                          MinSize(self.datapanel.GetBestSize()).
                          Caption("Data Panel").
                          CloseButton(False).
                          MaximizeButton(False).
                          Left().
                          Position(0).
                          Name('datapanel'))
        self.dataPane = self._mgr.GetPane('datapanel')
        self._mgr.LoadPaneInfo('prop=35000', self.dataPane)
        
        self._mgr.AddPane(self.divepanel, wx.aui.AuiPaneInfo().Layer(1).
                          MinSize(self.divepanel.GetBestSize()).
                          Caption("Current Dive Panel").
                          CloseButton(False).
                          MaximizeButton(False).
                          Left().
                          Position(1).
                          Name('divepanel'))
        self.divepanelPane = self._mgr.GetPane('divepanel')
        
        self._mgr.AddPane(self.grid, wx.CENTER)
#        self._mgr.AddPane(self.grid, wx.aui.AuiPaneInfo().Layer(0).
#                          MinSize(self.grid.GetBestSizeTuple()).
#                          Caption("Grid").CloseButton(False).
#                          MaximizeButton(False).
#                          Name('gridpanel'))

        self._mgr.Update()# tell the manager to 'commit' all the changes just made
    
    def BindEvents(self):
        self.Bind(wx.EVT_CLOSE, self._evtClose)
        self.Bind(wx.EVT_MENU, self._evtManageCrew, id = self.managedivers_menuItem.GetId())
        self.Bind(wx.EVT_MENU, self._evtClose, id = self.quit_menuItem.GetId())
        self.Bind(wx.EVT_MENU, self._evtGPSSettings, id = self.gps_menuItem.GetId())
        self.Bind(wx.EVT_MENU, self._evtShowAbout, id = self.about_menuItem.GetId())
        
        self.Bind( wx.EVT_MENU, self._evtMap, id = self.viewmap_menuItem.GetId() )
        
    def _evtMap(self, evt):
        #look for google earth
        filepath64 = "C:\\Program Files (x86)\\Google\\Google Earth\\client\\googleearth.exe"
        filepath32 = "C:\\Program Files\\Google\\Google Earth\\client\\googleearth.exe"
        if os.path.isfile( filepath64 ):
            os.startfile( "C:\\ProgramData\\DiveRT\\DiveRT.kml" )
        elif os.path.isfile( filepath32 ):
            os.startfile( "C:\\ProgramData\\DiveRT\\DiveRT.kml" )
        else:
            print 'google earth isn\'t installed'
        
    def _evtShowAbout(self, evt):
        about = About(None)
        about.ShowModal()
        
    def _evtGPSSettings(self, evt):
        gpswindow = GPSSettings(None)
        gpswindow.ShowModal()
        
    def _evtManageCrew(self, evt):
        crewmanager = CrewManager(None)
        crewmanager.ShowModal()
    
    def _evtClose(self, evt):
        self.Hide()
        if hasattr(self, 'gps'):
            #print 'closing gps connection'
            self.gps.close()
        diveKml.server.close()
        # deinitialize the frame manager
        self._mgr.UnInit()
        # delete the frame
        self.Destroy()

def Main():
    global DiveRTDir
    global DiveRTdbFile
    global IconDir
    global diveKml
    DiveRTDir = 'C:\\ProgramData\\DiveRT'
    DiveRTdbFile = 'C:\\ProgramData\\DiveRT\\DiveRT.db'
    
    if not os.path.isdir(DiveRTDir):
        #print 'creating', DiveRTDir
        os.mkdir(DiveRTDir)
        
    if not os.path.isfile(DiveRTdbFile):
        #print 'creating DiveRT.db'
        Sql.CreateEmptyDiveDB(DiveRTdbFile)
    
    diveKml = Kml.diveRTKml(DiveRTDir, DiveRTdbFile)
    diveKml.compileDiveFolders()
    diveKml.writeKmlToServer()
    
    ds = Sql.DataStore(DiveRTdbFile)
    global CleanupRound
    CleanupRound = ds.GetLastCleanupRound()
    #print 'Setting CleanupRound', CleanupRound
    ds.Close()
    
    app = wx.App(redirect=False)
    
    aboutdlg = About(None)
    aboutdlg.Show()
    
    global frame
    frame = AUIFrame(None)
    frame.SetPosition( wx.Point(0,0) )
    frame.divepanel._evtDiverChoice() #force event to populate listbox if diver had dives on this date
    frame.datapanel.init()
    frame.grid.updateRoundChoices()
    
    app.MainLoop()

Main()
