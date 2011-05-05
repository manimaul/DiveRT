import os, Sql, shutil

DiveRT_kml = """\
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

DiveRTdata_top = """\
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.0">
"""

DiveRTdata_folderBegin = """\
<Folder>
  <name>Cleanup-Round %s</name>
  <description>%s Oz/Hr</description>
  <Style></Style>
""" #%(round, ozperhr)

DiveRTdata_placemark = """\
  <Placemark>
    <name>%s</name>
      <description>%s %shrs</description>
      <Style>
        <IconStyle>
          <color>%sff</color>
          <heading>%s</heading>
          <Icon>
            <href>C:\ProgramData\DiveRT\icons\%s.png</href>
          </Icon>
        </IconStyle>
        <BalloonStyle>
          <text>$[name] $[description]
          %s</text>
        </BalloonStyle>
      </Style>
      <Point>
        <coordinates>%s, %s, 0.0</coordinates>
      </Point>
  </Placemark>
""" #%(date, name, hrs, color, bearing, icon, note, long, lat)

def main():
    

    
    DiveRT_kmlfile = 'C:\\ProgramData\\DiveRT\\DiveRT.kml'
    DiveRT_kmlfd = open( DiveRT_kmlfile, 'w' )
    DiveRT_kmlfd.writelines( DiveRT_kml )
    DiveRT_kmlfd.close()
    

    

    
    DiveRTdata_kmlfile =  'C:\\ProgramData\\DiveRT\\DiveRTdata.kml'
    DiveRTdata_kmlfd = open(DiveRTdata_kmlfile, 'w')
    DiveRTdata_kmlfd.writelines( DiveRTdata_top )
    ds = Sql.DataStore(DiveRTdbFile)
        
    for each in ds.GetKMLData():
        folderBegin = DiveRTdata_folderBegin %each[0]
        DiveRTdata_kmlfd.writelines ( folderBegin )
        for ea in each[1]:
            placemark =  DiveRTdata_placemark %ea
            DiveRTdata_kmlfd.writelines ( placemark )
        DiveRTdata_kmlfd.writelines ( """</Folder>""" )
        
    DiveRTdata_kmlfd.writelines ( """</kml>""" )
    ds.Close()
    
    ######
    
    DiveRTdata_kmlfd.close()

if __name__=="__main__":
    global DiveRTDir
    global DiveRTdbFile
    global IconDir
    DiveRTDir = 'C:\\ProgramData\\DiveRT'
    IconDir = 'C:\\ProgramData\DiveRT\\icons'
    DiveRTdbFile = 'C:\\ProgramData\\DiveRT\\DiveRT.db'
    
    if not os.path.isdir(DiveRTDir):
        print 'creating', DiveRTDir
        os.mkdir( DiveRTDir )
        
    if not os.path.isfile(DiveRTdbFile):
        print 'creating DiveRT.db'
        Sql.CreateEmptyDiveDB( DiveRTdbFile )
        
    if not os.path.isdir(IconDir):
        print 'creating ', IconDir
        os.mkdir( IconDir )
        
    if not os.path.isfile( IconDir + '\\arrow.png' ):
        print 'creating arrow.png'
        shutil.copy2('icons\\arrow.png', IconDir)
        
    if not os.path.isfile( IconDir + '\\circle.png' ):
        print 'creating circle.png'
        shutil.copy2('icons\\circle.png', IconDir)
        
    main()
        
    
        
    
        
