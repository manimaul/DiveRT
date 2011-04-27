#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Copyright (C) 2010 by Will Kamp <manimaul!gmail.com>

import Grid, time, GUI, Sql, os, wx.aui, GPSCom, wx.grid as gridlib
from re import sub

class ConfirmDlg(GUI.ConfirmDlg): #dialog shown before dive session is deleted
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
        self.Destroy()
    
    def _evtCancel(self, evt):
        self.Destroy()

class EditDlg(GUI.EditDlg):
    def _evtHr(self, evt):
        ctrl = evt.GetEventObject()
        val = str(ctrl.GetValue())
        newval = sub(r'\D+', '', val) #remove any non digits
        if newval != val:
            ctrl.SetValue(newval)
            ctrl.SetInsertionPointEnd()
        if newval != '':
            if int(newval) > 12:
                ctrl.SetValue('12')
    
    def _evtMinSec(self, evt):
        ctrl = evt.GetEventObject()
        val = str(ctrl.GetValue())
        newval = sub(r'\D+', '', val) #remove any non digits
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
            lat = data[6]
            self.lat_textCtrl.SetValue(lat)
            long = data[7]
            self.lon_textCtrl.SetValue(long)
            bearing = data[8]
            self.bearing_textCtrl.SetValue(bearing)
            datastore.Close()         
        else: #non full edits have no intormation stored in the database
            self.tender_staticText.Hide()
            self.tender_choice.Hide()
            self.m_staticline7.Hide()
            self.m_staticTextLat.Hide()
            self.lat_textCtrl.Hide()
            self.m_staticTextLon.Hide()
            self.lon_textCtrl.Hide()
            self.m_staticTextBearing.Hide()
            self.bearing_textCtrl.Hide()
            self.m_staticline1.Hide()
            self.Fit()
            #todo
           
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
                lat = self.lat_textCtrl.GetValue()
                long = self.lon_textCtrl.GetValue()
                bearing = self.bearing_textCtrl.GetValue()
                notes = data[9]
                tender = self.tender_choice.GetStringSelection()
                datastore.UpdateDive(id, cleanup, date, diver, start, stop, lat, long, bearing, notes, tender)
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
            frame.divepanel.lat = self.lat_textCtrl.GetValue()
            frame.divepanel.long = self.lon_textCtrl.GetValue()
            frame.divepanel.bearing = self.bearing_textCtrl.GetValue()
            frame.divepanel.SaveDive()
        self.Destroy()

class DataPanel(GUI.DataPanel):
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
            long = frame.gps.fmt_lon('DDD')
            if lat is not None and long is not None:
                #frame.divepanel.lat = unicode(lat)
                #frame.divepanel.long = unicode(long)
                self.lat_staticText.SetLabel(unicode(lat))
                self.long_staticText.SetLabel(unicode(long))
            bearing = frame.gps.fmt_bearing('M')
            if bearing is not 'None':
                #frame.divepanel.bearing = unicode(bearing)
                self.bearing_staticText.SetLabel(unicode(bearing))
        frame.divepanel.CalcTimeUW()

class DivePanel(GUI.DivePanel):
    def init(self):
        self.lat = '00.0000000'
        self.long = '000.0000000'
        self.bearing = '000.00'
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
            print 'Starting Dive'
            if hasattr(frame, 'gps'):
                lat = frame.gps.fmt_lat('DDD')
                long = frame.gps.fmt_lon('DDD')
                if lat is not None and long is not None:
                    frame.divepanel.lat = unicode(lat)
                    frame.divepanel.long = unicode(long)
                bearing = frame.gps.fmt_bearing('M')
                if bearing is not 'None':
                    frame.divepanel.bearing = unicode(bearing)
            print 'Locking in coordinates', frame.divepanel.lat, frame.divepanel.long, frame.divepanel.bearing
            frame.listpanel.edit_Button.Enable()
            frame.listpanel.delete_Button.Enable()
            frame.listpanel.times_listBox.Append(now)
            frame.listpanel.insert_Button.Enable(False)
            self.diver_choice.Disable()
            self.datePicker.Disable()
            self.startstop_button.SetLabel('Stop Dive')
            self.status_textCtrl.SetValue('Dive in progress')
        else:
            print 'Stopping Dive'
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
                print 'Saving Dive to database'
                self.SaveDive()
            print 'Resetting coordinates'
            frame.divepanel.lat = '00.0000000'
            frame.divepanel.long = '000.0000000'
            frame.divepanel.bearing = '000.00'
        nsel = frame.listpanel.times_listBox.GetItems().__len__()-1
        frame.listpanel.times_listBox.SetSelection(nsel)
        if evt is not None:
            evt.Skip()
        
    def _evtTenderChoice(self, evt):
        self.tender = self.tender_choice.GetStringSelection()
        print 'tender selected:', self.tender
        
    def _evtDiverChoice(self, evt=None):
        self.diver = self.diver_choice.GetStringSelection()
        date = self.datePicker.GetValue().Format('%b %d %Y')
        print 'diver selected:', self.diver
        print 'date selected:', date
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
        print 'dive recordIDs in listbox: ', frame.listpanel.diveidlst
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
        #TODO: retrieve this data:
        lastid = datastore.AppendDive(CleanupRound, date, self.diver, start, stop, self.lat, self.long, self.bearing, self.notes, self.tender)
        frame.listpanel.diveidlst.append(lastid) #track IDs of dives in list so records can be deleted
        datastore.Close()
        frame.grid._evtRefresh(None)
        #print frame.listpanel.diveidlst

class GridPanel(GUI.GridPanel):
    def _evtRefresh(self, evt=None):
        self.grid.Table = Grid.CustomDataTable(CleanupRound, DiveRTdbFile)
        self.grid.FormatCells()
        self.grid.AutoSizeColumns(True)
        self.grid.AutoSizeRows(True)
        msg = gridlib.GridTableMessage(self.grid.Table, gridlib.GRIDTABLE_REQUEST_VIEW_GET_VALUES)
        self.grid.Table.GetView().ProcessTableMessage(msg)
        self.Layout()
    
    def updateRoundChoices(self):
        print 'updating round choices'
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
        ds = Sql.DataStore(DiveRTdbFile)
        CleanupRound = ds.GetLastCleanupRound()+1
        if self.cround_choice.GetItems().count(str(CleanupRound)) == 0:
            self.cround_choice.Append(str(CleanupRound))
        self.cround_choice.SetSelection(CleanupRound-1)
        self._evtRoundChange()
        ds.Close()
        
class DetailPanel(GUI.DetailPanel):
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
            print 'editing recordID', frame.listpanel.diveidlst[dex]
            EditDialog.IsFullEdit = True
            EditDialog.EnableFullEdit()
        EditDialog.EditFillValues()
        EditDialog.ShowModal()
              
class GPSSettings(GUI.GPSSettings):
    def SetCtrlValues(self, evt):
        ds = Sql.DataStore(DiveRTdbFile)
        com, baud = ds.GetGPSSettings()
        if com is not None and baud is not None:
            com = int(com[3:com.__len__()])
            print com, baud
            self.com_spinCtrl.SetValue(com)
            self.baud_comboBox.SetStringSelection(str(baud))
        ds.Close()
    
    def _evtCom(self, evt):
        if hasattr(frame, 'gps'):
            print 'closing previous gps connection'
            frame.gps.close()
        com = 'COM' + str(self.com_spinCtrl.GetValue())
        baud = self.baud_comboBox.GetValue()
        print 'connecting to:', com, baud
        frame.gps = GPSCom.gps(com, baud)
        
        ds = Sql.DataStore(DiveRTdbFile)
        ds.SetGPSSettings(com, baud)
        ds.Close()
    
    def _evtDone(self, evt):
        self.Destroy()

class MyFrame(wx.Frame):
    def __init__(self, parent, id=-1, title='Dive Recovery Tracker',
                 pos=wx.DefaultPosition, size=(1000, 700),
                 style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        self._mgr = wx.aui.AuiManager(self)
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
        
        self.managedivers_menuItem = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Manage Divers && Tenders", wx.EmptyString, wx.ITEM_NORMAL )
        self.file_menu.AppendItem( self.managedivers_menuItem )
        
        self.gps_menuItem = wx.MenuItem( self.file_menu, wx.ID_ANY, u"GPS Settings", wx.EmptyString, wx.ITEM_NORMAL )
        self.file_menu.AppendItem( self.gps_menuItem )
        
        self.quit_menuItem = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Quit", wx.EmptyString, wx.ITEM_NORMAL )
        self.file_menu.AppendItem( self.quit_menuItem )
        
        self.MenuBar.Append( self.file_menu, u"Menu" ) 
        self.SetMenuBar( self.MenuBar )        
                
    def DefaultLayout(self):
        # add the panes to the manager
        self._mgr.AddPane(self.listpanel, wx.aui.AuiPaneInfo().Layer(0).
                          MinSize(self.listpanel.GetBestSize()).
                          Caption("Dive List Panel").
                          CloseButton(False).
                          MaximizeButton(False).
                          Bottom().
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

        
        self._mgr.Update()# tell the manager to 'commit' all the changes just made
    
    def BindEvents(self):
        self.Bind(wx.EVT_CLOSE, self._evtClose)
        self.Bind(wx.EVT_MENU, self._evtManageCrew, id = self.managedivers_menuItem.GetId())
        self.Bind(wx.EVT_MENU, self._evtClose, id = self.quit_menuItem.GetId())
        self.Bind(wx.EVT_MENU, self._evtGPSSettings, id = self.gps_menuItem.GetId())
        
    def _evtGPSSettings(self, evt):
        gpswindow = GPSSettings(None)
        gpswindow.ShowModal()
        
    def _evtManageCrew(self, evt):
        crewmanager = CrewManager(None)
        crewmanager.ShowModal()
    
    def _evtClose(self, evt):
        if hasattr(self, 'gps'):
            print 'closing gps connection'
            self.gps.close()
        # deinitialize the frame manager
        self._mgr.UnInit()
        # delete the frame
        self.Destroy()

class Rows:
    def __init__(self):
        self.rowNumber = 0
        self.rowStack = []

class CrewManager(wx.Dialog):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Crew Manager", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        self.bxSizer1 = wx.BoxSizer( wx.VERTICAL)
        self.bxSizer2 = wx.BoxSizer( wx.VERTICAL )
        self.fgSizer = wx.FlexGridSizer( 99, 5, 0, 0 )
        self.fgSizer.SetFlexibleDirection( wx.BOTH )
        self.fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.rows = Rows()
        
        self.bxSizer1.Add( self.bxSizer2, 1, wx.EXPAND, 5)
        self.bxSizer2.Add( self.fgSizer, 1, wx.EXPAND, 5 )
        
        self.addStaticControls()

        datastore = Sql.DataStore(DiveRTdbFile)
        crewlist = datastore.GetCrewList()
        for each in crewlist:
            self.addRow(each[1], each[2], int(each[3]), int(each[4]))
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
        
        tenderRate_staticText = wx.StaticText( self, wx.ID_ANY, u"Tender Rate ($/hr)", wx.DefaultPosition, wx.DefaultSize, 0 )
        tenderRate_staticText.Wrap( -1 )
        self.fgSizer.Add( tenderRate_staticText, 0, wx.ALL, 5 )
        
        self.fgSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.save_button = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.bxSizer1.Add( self.save_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.save_button.Bind(wx.EVT_BUTTON, self._evtSave)
        self.Bind(wx.EVT_CLOSE, self._evtClose)
        
    def addRow(self, Name="", Duty="Diver and Tender", DiveRate=50, TendRate=20):
        #print 'adding row#', self.rows.rowNumber
        name_textCtrl = wx.TextCtrl( self, wx.ID_ANY, Name, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.fgSizer.Add( name_textCtrl, 0, wx.ALL, 5 )
        
        duty_choiceChoices = [ u"Diver and Tender", u"Tender" ]
        duty_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, duty_choiceChoices, 0 )
        duty_choice.SetStringSelection(Duty)
        self.fgSizer.Add( duty_choice, 0, wx.ALL, 5 )
        
        diveRate_spinCtrl = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 25, 100, 50 )
        diveRate_spinCtrl.SetValue(DiveRate)
        self.fgSizer.Add( diveRate_spinCtrl, 0, wx.ALL, 5 )
        
        tenderRate_spinCtrl = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 10, 40, 20 )
        tenderRate_spinCtrl.SetValue(TendRate)
        self.fgSizer.Add( tenderRate_spinCtrl, 0, wx.ALL, 5 )
        
        delete_button = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.fgSizer.Add( delete_button, 0, wx.ALL, 5 )
        
        self.SetSizer( self.bxSizer1)
        self.Layout()
        self.bxSizer1.Fit( self )
        
        self.rows.rowStack.append([name_textCtrl, duty_choice, diveRate_spinCtrl, tenderRate_spinCtrl, delete_button])
        name_textCtrl.Bind( wx.EVT_TEXT, lambda evt, rownum=self.rows.rowNumber: self._evtNameTxt(evt, rownum))
        duty_choice.Bind( wx.EVT_CHOICE, lambda evt, rownum=self.rows.rowNumber: self._evtDuty(evt, rownum))
        delete_button.Bind( wx.EVT_BUTTON, lambda evt, rownum=self.rows.rowNumber: self._evtDelete(evt, rownum))
        delete_button.Disable()
        self.rows.rowStack[self.rows.rowNumber-1][4].Enable()
        self._evtDuty(None, self.rows.rowNumber)
        self.rows.rowNumber += 1
        
    def deleteRow(self, rownum):
        print 'deleting row: ', rownum
        listofdestroy = self.rows.rowStack[rownum]
        for each in listofdestroy:
            each.Destroy()
            
        self.rows.rowStack.pop(rownum)
        self.rows.rowStack.insert(rownum, None)
        
        self.SetSizer( self.bxSizer1)
        self.Layout()
        self.bxSizer1.Fit( self )
    
    def _evtDuty(self, evt, rownum):
        rowobjlst = self.rows.rowStack[rownum]
        if rowobjlst[1].GetStringSelection() == "Diver and Tender":
            rowobjlst[2].Enable() #diveRate_spinCtrl.Enable()
        else:
            rowobjlst[2].Disable()
    
    def _evtNameTxt(self, evt, rownum):
        #print 'typing in: ', rownum
        if rownum == self.rows.rowNumber - 1:
            self.addRow()
            
    def _evtDelete(self, evt, rownum):
        self.deleteRow(rownum)
        
    def _evtSave(self, evt):
        datastore = Sql.DataStore(DiveRTdbFile)
        datastore.DropCrewData()
        for each in self.rows.rowStack[0:-1]:
            if each is not None:
                print each[0].GetValue(), each[1].GetStringSelection(), each[2].GetValue(), each[3].GetValue()
                datastore.AddCrew(each[0].GetValue(), each[1].GetStringSelection(), each[2].GetValue(), each[3].GetValue())
        datastore.Close()
        frame.divepanel.updateDiverTenderChoice()
        self.Destroy()
    
    def _evtClose(self, evt):
        self.Destroy()

DiveRTDir = 'C:\ProgramData\DiveRT'
DiveRTdbFile = 'C:\ProgramData\DiveRT\DiveRT.db'

if not os.path.isdir(DiveRTDir):
    print 'creating', DiveRTDir
    os.mkdir(DiveRTDir)
    
if not os.path.isfile(DiveRTdbFile):
    print 'creating DiveRT.db'
    Sql.CreateEmptyDiveDB(DiveRTdbFile)

ds = Sql.DataStore(DiveRTdbFile)
CleanupRound = ds.GetLastCleanupRound()
print 'Setting CleanupRound', CleanupRound
ds.Close()

app = wx.App(redirect=False)
frame = MyFrame(None)
frame.divepanel._evtDiverChoice() #force event to populate listbox if diver had dives on this date
frame.datapanel.init()
frame.grid.updateRoundChoices()

frame.Show()
app.MainLoop()
