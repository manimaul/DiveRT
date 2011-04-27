import wx, GUI, Sql

DiveRTdbFile = 'C:\ProgramData\DiveRT\DiveRT.db'

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
        self.Destroy()
        
    def _evtClose(self, evt):
        print 'Destroying DM'
        self.Destroy()

if __name__=='__main__':
    app = wx.App(redirect=False)
    cm = CrewManager(None)
    cm.Show()
    app.MainLoop()