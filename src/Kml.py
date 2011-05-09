#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Copyright (C) 2010 by Will Kamp <manimaul!gmail.com>

import os, Sql, shutil, KmlServer

def iconList():
    return [ 'Aqu.png', 'Blu.png', 'BPk.png', 'Bwn.png', 'DkG.png', 'Grn.png', 'Gry.png', 'LBu.png', 'LGn.png', 'Pnk.png', 'Prp.png', 'Red.png', 'Tan.png', 'Wht.png', 'Yel.png']

class diveRTKml():
    def __init__(self, DiveRTDir, DiveRTdbFile):
        print 'initializing diveRTKml'
        self.DiveRTDir = DiveRTDir
        self.DiveRTdbFile = DiveRTdbFile
        self.diveFolders = ""
        self.locationFolders = ""
        ## Templates
        self._diveRTnetLink = """\
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.2">
<NetworkLink>
  <name>DiveRT</name>
  <open>1</open>
  <Link>
    <href>http://127.0.0.1:8080/data.kml</href>
    <refreshInterval>3</refreshInterval>
    <refreshMode>onInterval</refreshMode>
  </Link>
</NetworkLink>
</kml>
"""
        self._diveRTdata = """\
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.0">
  <Document>
    <name>DiveRT</name>
%s
%s
  </Document>
</kml>
""" #%(diveFolders, locationFolders)
        self._diveFolders = """\
<Folder>
  <name>Cleanup-Round %s</name>
  <description>%s Oz/Hr</description>
""" #%(round, ozperhr)
        self._divePlacemark = """\
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
        self._locationFolders = """\
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
""" #%(heading, long, lat, startHeading, startLong, startLat)
        ## Templates end
        self.createKmlIcons()
        self.createNetworkLink()
        self.server = KmlServer.KMLServer()
    
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
        fd.writelines( self._diveRTnetLink )
        fd.close()
        
    def compileDiveFolders(self):
        #print 'compiling dive folders for kml'
        self.diveFolders = "" #clear existing
        ds = Sql.DataStore( self.DiveRTdbFile )
        for each in ds.GetKMLData():
            folderBegin = self._diveFolders %each[0]
            self.diveFolders += folderBegin
            for ea in each[1]:
                placemark =  self._divePlacemark %ea
                self.diveFolders += placemark
            self.diveFolders += "</Folder>\n"
        ds.Close()
    
    def compileLocationFolders(self, heading, long, lat, startHeading, startLong, startLat):
        #print 'compiloing location folder for kml'
        self.locationFolders = self._locationFolders %( str(heading), str(long), str(lat), str(startHeading), str(startLong), str(startLat) )
        
    
    def writeKmlToServer(self):
        #print 'writing kml data to KmlServe memory'
        self.server.handler.dataKml = self._diveRTdata %( self.diveFolders, self.locationFolders )   
    
if __name__=="__main__":
    from time import sleep
    DiveRTDir = 'C:\\ProgramData\\DiveRT'
    DiveRTdbFile = 'C:\\ProgramData\\DiveRT\\DiveRT.db'
    dkml = diveRTKml(DiveRTDir, DiveRTdbFile)
    dkml.compileDiveFolders()
    dkml.compileLocationFolders( 190.0, 0.0, 0.0, 90.0, 0.0, 0.0 )
    #print dkml._diveRTdata %( dkml.diveFolders, dkml.locationFolders )
    dkml.writeKmlToServer()
    sleep(60)
    