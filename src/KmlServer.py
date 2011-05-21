#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Copyright (C) 2010 by Will Kamp <manimaul!gmail.com>

from threading import Thread
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
import os

class ThreadedHttpRequestHandler(BaseHTTPRequestHandler):      
    def do_HEAD(self):
        try:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
        except:
            print 'HTTP HEAD response not sent'
    def do_GET(self):
        """Respond to a GET request."""
        try:
            self.send_response(200)
            if self.path == '/arrowship.png':
                self.send_header("Content-type", "image/png")
                self.end_headers()
                self.wfile.write(self.arrowshipPng)
            if self.path == '/arrowstart.png':
                self.send_header("Content-type", "image/png")
                self.end_headers()
                self.wfile.write(self.arrowstartPng)
            if self.path == '/data.kml':
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(self.dataKml)
        except:
            print 'HTTP GET response not sent'
            
    def log_message(self, format, *args):
        return #supress log messages

class HTTPServer(ThreadingMixIn, HTTPServer):
    pass

class KMLServer:
    def __init__(self, host='', port=8080):
        self.port = port
        self.handler = ThreadedHttpRequestHandler
        #load arrowship icon into handler memory
        self.iconhref = '/arrowship.png</href>'
        iconpath = os.getcwd() + '\\icons\\arrowship.png'
        fd = open(iconpath, 'rb')
        self.handler.arrowshipPng = fd.read()
        fd.close()
        #load startship icon into handler memory
        self.iconhref = '/arrowstart.png</href>'
        iconpath = os.getcwd() + '\\icons\\arrowstart.png'
        fd = open(iconpath, 'rb')
        self.handler.arrowstartPng = fd.read()
        fd.close()
        #load data.kml into handler memory
        self.handler.dataKml = u"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<kml xmlns=\"http://earth.google.com/kml/2.0\">"
        
        self.server = HTTPServer((host, port), self.handler)
        server_thread = Thread(target=self.server.serve_forever, name='kmld-thread')
        server_thread.setDaemon(True)
        server_thread.start()
        #print "KmlServer loop running in thread:", server_thread.getName()
        
    def close(self):
        #print "Shutting down kml server..."
        self.server.shutdown()
        self.server.server_close()
        #print "kml server down"
        
        
if __name__ == '__main__':
    from time import sleep
    myserver = KMLServer()
    print 'updating kml'
    myserver.handler.dataKml = """\
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
            <href>/arrowship.png</href>
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
            <href>/arrowstart.png</href>
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
""" %( '000.00', '000.000000', '00.00000', '90.0', '-000.000200', '00.000200' )
    sleep(60)
    myserver.close()
        
        
    