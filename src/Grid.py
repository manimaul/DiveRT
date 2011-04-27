
import  wx, Sql
import  wx.grid as gridlib

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
        self.colLabels = ['Dive Date']
        for diver in self.DataStore.GetDiverList(cleanupNumber):
            self.colLabels.append(diver)
        self.colLabels.append('Dives Totals')       
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
    def __init__(self, parent, dbfile):
        gridlib.Grid.__init__(self, parent, -1)
        table = CustomDataTable(self.GetLastCleanupNumber(dbfile), dbfile)

        # The second parameter means that the grid is to take ownership of the
        # table and will destroy it when done.  Otherwise you would need to keep
        # a reference to it and call it's Destroy method later.
        self.SetTable(table, True)

        self.SetRowLabelSize(0) #hides row labels row
        #self.SetMargins(0,0)
        self.EnableEditing(False)
        self.EnableDragColMove(True)
        self.EnableDragColSize(False)
        self.EnableDragRowSize(False)
        self.EnableDragGridSize(False)
        self.FormatCells()
        
        self.AutoSizeColumns(True)
        self.AutoSizeRows(True)
        
    def GetLastCleanupNumber(self, dbfile):
        ds = Sql.DataStore(dbfile)
        cleanupNumber = ds.GetLastCleanupRound()
        ds.Close()
        return cleanupNumber
        
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
        
if __name__=='__main__':
    app = wx.App(redirect=False)
    frame = wx.Frame(None, title='Grid')
    frame.SetSize(wx.Size(600,400))
    bsizer = wx.BoxSizer(wx.VERTICAL)
    grid = CustTableGrid(frame, 'C:\ProgramData\DiveRT\DiveRT.db')
    bsizer.Add(grid)
    frame.Show()
    app.MainLoop()
        