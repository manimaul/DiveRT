import wx, GUI, Sql, re

class Report(GUI.RoundReport):
    def _evtInit(self, evt):
        self.round_textCtrl.SetValue( str(CleanupRound) )
        self.totaltime = ds.GetTotalHours(CleanupRound)
        self.totalHours_textCtrl.SetValue(self.totaltime)
        self.SetEstTotal()
        
        diverlist = ds.GetDiverList(CleanupRound)
        diverhours = ds.GetCleanupTotals(CleanupRound)
        #get default diver percentages here... will be updated later if cleanup/round has saved data
        diverrates = ds.GetDiverRates(diverlist)
        
        self.diverRows = []
        for diver in diverlist:
            self.addDiverRow(diver, diverhours[diver], diverrates[diver])
        
        self.updateDiverRows()
            
    def updateDiverRows(self):
        for row in self.diverRows:
            self._evtDiverPercentSet(row[0], row[1], row[2], row[3] )
            
    def addDiverRow(self, name, hours, percent):
        divername_textCtrl = wx.TextCtrl( self, wx.ID_ANY, name, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        divername_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
        self.diving_fgSizer.Add( divername_textCtrl, 0, wx.ALL, 5 )
        
        diverhours_textCtrl = wx.TextCtrl( self, wx.ID_ANY, hours, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        diverhours_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
        self.diving_fgSizer.Add( diverhours_textCtrl, 0, wx.ALL, 5 )
        
        diverperct_textCtrl = wx.TextCtrl( self, wx.ID_ANY, percent, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.diving_fgSizer.Add( diverperct_textCtrl, 0, wx.ALL, 5 )
        
        diverpay_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        diverpay_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
        self.diving_fgSizer.Add( diverpay_textCtrl, 0, wx.ALL, 5 )
        
        payvalue_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        payvalue_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
        self.diving_fgSizer.Add( payvalue_textCtrl, 0, wx.ALL, 5)
        
        diverperct_textCtrl.Bind( wx.EVT_TEXT, lambda evt, h=diverhours_textCtrl, p=diverperct_textCtrl, g=diverpay_textCtrl, e=payvalue_textCtrl, : self._evtDiverPercentSet(h, p, g, e, evt))
        
        self.diverRows.append( (diverhours_textCtrl, diverperct_textCtrl, diverpay_textCtrl, payvalue_textCtrl) )
        self.bSizer.Fit( self )
        self.Layout()
        
    def _evtDiverPercentSet(self, diverhours_textCtrl, diverperct_textCtrl, diverpay_textCtrl, payvalue_textCtrl, evt=None ):
        val = diverperct_textCtrl.GetValue()
        newval = self.floatstr(val)
        if newval != val:
            diverperct_textCtrl.SetValue(newval)
            diverperct_textCtrl.SetInsertionPointEnd()
        thrs = float ( self.totalHours_textCtrl.GetValue() )
        tgrams = float ( self.totalGrams_textCtrl.GetValue() )
        hrs = float( diverhours_textCtrl.GetValue() )
        pct = float( newval ) / 100.0
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
        
    def _evtTotalGramsChange(self, evt):
        #only allow numbers and  one decimal
        value = self.totalGrams_textCtrl.GetValue()
        newval = self.floatstr(value)
        if newval != value:
            self.totalGrams_textCtrl.SetValue(newval)
            self.totalGrams_textCtrl.SetInsertionPointEnd()
        #recalculate Estimated Total Value
        self.SetEstTotal()
        #recalculate each divers pay
        self.updateDiverRows()
    
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
        self.updateDiverRows()
        
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
        self.updateDiverRows()
        
    def _evtSave(self, evt):
        ds.Close()
        self.Destroy()
        
DiveRTdbFile = 'C:\ProgramData\DiveRT\DiveRT.db'
ds = Sql.DataStore(DiveRTdbFile)
CleanupRound = 1

app = wx.App(redirect=False)
report = Report(None)
report.Show()
app.MainLoop()

##15hr 6 min for round 1