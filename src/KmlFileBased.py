import os, Sql, shutil

def iconList():
    return [ 'Aqu.png', 'Blu.png', 'BPk.png', 'Bwn.png', 'DkG.png', 'Grn.png', 'Gry.png', 'LBu.png', 'LGn.png', 'Pnk.png', 'Prp.png', 'Red.png', 'Tan.png', 'Wht.png', 'Yel.png']

class diveKml():
    def __init__(self, DiveRTDir, DiveRTdbFile):
        print 'initializing diveKml'
        self.DiveRTDir = DiveRTDir
        self.DiveRTdbFile = DiveRTdbFile
        self.DiveRT_kml = """\
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.2">
<NetworkLink>
  <name>DiveRT</name>
  <open>1</open>
  <Link>
    <href>C:\ProgramData\DiveRT\DiveRTdata.kml</href>
    <refreshInterval>5</refreshInterval>
    <refreshMode>onInterval</refreshMode>
  </Link>
</NetworkLink>
</kml>
"""
        self.DiveRTdata_top = """\
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.0">
<Document>
  <name>DiveRT Locations</name>
"""
        self.DiveRTdata_folderBegin = """\
<Folder>
  <name>Cleanup-Round %s</name>
  <description>%s Oz/Hr</description>
""" #%(round, ozperhr)
        self.DiveRTdata_placemark = """\
  <Placemark>
    <name>%s</name>
      <description>%s %shrs</description>
      <Style>
        <IconStyle>
          <heading>%s</heading>
          <Icon>
            <href>C:\ProgramData\DiveRT\icons\%s</href>
          </Icon>
        </IconStyle>
        <BalloonStyle>
          <text>$[description]
          %s</text>
        </BalloonStyle>
      </Style>
      <Point>
        <coordinates>%s, %s, 0.0</coordinates>
      </Point>
  </Placemark>
""" #%(title, diver, hrs, bearing, icon, note, long, lat)
        self.createKmlIcons()
        self.createNetworkLink()
        
    def createKmlIcons(self):
        IconDir = self.DiveRTDir + '\\icons'
        
        if not os.path.isdir(IconDir):
            print 'creating ', IconDir
            os.mkdir( IconDir )
        
        iconlst = iconList()
        iconlst.append('ship.png')
        iconlst.append('start.png')
        for icon in iconlst:
            if not os.path.isfile( IconDir + '\\arrow' + icon ):
                print 'creating arrow' + icon
                shutil.copy2('icons\\arrow' + icon, IconDir)
                
            if not os.path.isfile( IconDir + '\\circle' + icon ):
                print 'creating circle' + icon
                shutil.copy2('icons\\circle' + icon, IconDir)
    
    def createNetworkLink(self):
        filepath = self.DiveRTDir + '\\DiveRT.kml'
        fd = open( filepath, 'w' )
        fd.writelines( self.DiveRT_kml )
        fd.close()
        
    def createKmlData(self):
        print 'creating-updating diveKml data'
        DiveRTdata_kmlfile =  DiveRTDir + '\\DiveRTdata.kml'
        DiveRTdata_kmlfd = open(DiveRTdata_kmlfile, 'w')
        DiveRTdata_kmlfd.writelines( self.DiveRTdata_top )
        ds = Sql.DataStore(DiveRTdbFile)
        for each in ds.GetKMLData():
            folderBegin = self.DiveRTdata_folderBegin %each[0]
            DiveRTdata_kmlfd.writelines ( folderBegin )
            for ea in each[1]:
                placemark =  self.DiveRTdata_placemark %ea
                DiveRTdata_kmlfd.writelines ( placemark )
            DiveRTdata_kmlfd.writelines ( """</Folder>\n""" )
            
        DiveRTdata_kmlfd.writelines ( """</Document>\n</kml>""" )
        ds.Close()
        DiveRTdata_kmlfd.close()
              
class liveKml():
    def __init__(self, DiveRTDir, DiveRTdbFile):
        self.DiveRTDir = DiveRTDir
        self.DiveRTdbFile = DiveRTdbFile
        self.DiveRTL_kml = """\
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.2">
<NetworkLink>
  <name>DiveRT</name>
  <open>1</open>
  <Link>
    <href>C:\\ProgramData\\DiveRT\\DiveRTLdata.kml</href>
    <refreshInterval>2</refreshInterval>
    <refreshMode>onInterval</refreshMode>
  </Link>
</NetworkLink>
</kml>
"""
        self.DiveRTLdata = """\
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.0">
<Document>
  <name>DiveRT Locations</name>
<Folder>
  <name>Ship Location</name>
  <Placemark>
    <name>Current Location</name>
      <description></description>
      <Style>
        <LabelStyle>
          <color>ff0000ff</color>
          <scale>1</scale>
        </LabelStyle>
        <IconStyle>
          <heading>%s</heading>
          <scale>1</scale>
          <Icon>
            <href>C:\\ProgramData\\DiveRT\\icons\\arrowship.png</href>
          </Icon>
        </IconStyle>
        <BalloonStyle>
          <text></text>
        </BalloonStyle>
      </Style>
      <Point>
        <coordinates>%s, %s, 0</coordinates>
      </Point>
  </Placemark>
    <Placemark>
    <name>Dive Start Location</name>
      <description></description>
      <Style>
        <LabelStyle>
          <color>5014b4ff</color>
          <colorMode>normal</colorMode>
          <scale>1</scale>
        </LabelStyle>
        <IconStyle>
          <heading>%s</heading>
          <scale>1</scale>
          <Icon>
            <href>C:\\ProgramData\\DiveRT\\icons\\arrowstart.png</href>
          </Icon>
        </IconStyle>
        <BalloonStyle>
          <text>
          </text>
        </BalloonStyle>
      </Style>
      <Point>
        <coordinates>%s, %s, 0</coordinates>
      </Point>
  </Placemark>
 </Folder>
 </Document>
 </kml>
""" #%(heading, long, lat, startHeading, startLong, startLat)
        self.createNetworkLink()
    
    def createNetworkLink(self):
        filepath = self.DiveRTDir + '\\DiveRTL.kml'
        fd = open( filepath, 'w' )
        fd.writelines( self.DiveRTL_kml )
        fd.close()
        
    def createKmlData(self, heading, long, lat, startHeading, startLong, startLat):
        t = ( str(heading), str(long), str(lat), str(startHeading), str(startLong), str(startLat) )
        print 'creating-updating liveKml data'
        DiveRTdata_kmlfile =  DiveRTDir + '\\DiveRTLdata.kml'
        DiveRTdata_kmlfd = open(DiveRTdata_kmlfile, 'w')
        DiveRTdata_kmlfd.writelines( self.DiveRTLdata %t ) 
        
if __name__=="__main__":
    DiveRTDir = 'C:\\ProgramData\\DiveRT'
    DiveRTdbFile = 'C:\\ProgramData\\DiveRT\\DiveRT.db'
    dkml = diveKml(DiveRTDir, DiveRTdbFile)
    dkml.createKmlData()
    lkml = liveKml(DiveRTDir, DiveRTdbFile)
    lkml.createKmlData( 190.0, -165.457475, 64.497258, 290.9, -165.457641, 64.497293 )