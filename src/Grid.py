
import wx, Sql
import wx.grid as gridlib
import wx.lib.scrolledpanel as scrolled

class CustomDataTable(gridlib.PyGridTableBase):
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

class CustTableGrid(gridlib.Grid):
    def __init__(self, parent, dbfile, cleanup=0):
        gridlib.Grid.__init__(self, parent, -1)
        
        if cleanup == 0:
            ds = Sql.DataStore(dbfile)
            cleanup = ds.GetLastCleanupRound()
            ds.Close()
        print 'grid using cleanup #', cleanup
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
        print "Cell Select", row, col
        self.SetGridCursor(row, col)
        print self.GetCellValue(row, col)
        
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

class GridGridPanel( scrolled.ScrolledPanel ):
    def __init__( self, parent ):
        scrolled.ScrolledPanel.__init__( self, parent, -1)
        self.bSizer = wx.BoxSizer( wx.VERTICAL )
        self.grid = CustTableGrid(self,  'C:\ProgramData\DiveRT\DiveRT.db')
        self.bSizer.Add( self.grid, 0, wx.ALL, 5 )
        self.SetSizer( self.bSizer )
        self.SetAutoLayout(1)
        self.SetupScrolling()
        
    def onWheel(self, event):
        print 'wheel'
        
class GridPanel ( wx.Panel ):
    def __init__( self, parent ):
        wx.Panel.__init__( self, parent, -1)
        
        self.bSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Dive Table", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )
        self.m_staticText19.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
        
        self.bSizer.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_staticline36 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        self.bSizer.Add( self.m_staticline36, 0, wx.EXPAND |wx.ALL, 5 )
        
        fgSizer12 = wx.FlexGridSizer( 1, 4, 0, 0 )
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
    
    def __del__( self ):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def _evtRoundChange( self, event ):
        event.Skip()
    
    def _evtNewRound( self, event ):
        event.Skip()
    
    def _evtReport( self, event ):
        event.Skip()

if __name__=='__main__':
    app = wx.App(redirect=False)
    frame = wx.Frame(None, title='Grid')
    frame.SetSize(wx.Size(600,400))
    bsizer = wx.BoxSizer(wx.VERTICAL)
    gridpanel = GridPanel(frame)
    bsizer.Add(gridpanel)
    
    frame.Show()
    app.MainLoop()
        