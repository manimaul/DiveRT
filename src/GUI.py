# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import Grid

###########################################################################
## Class DivePanel
###########################################################################

class DivePanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 450,-1 ), style = wx.TAB_TRAVERSAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Current Dive", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		self.m_staticText21.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer3.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline7 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.diver_staticText = wx.StaticText( self, wx.ID_ANY, u"Diver", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.diver_staticText.Wrap( -1 )
		fgSizer2.Add( self.diver_staticText, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		diver_choiceChoices = []
		self.diver_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), diver_choiceChoices, 0 )
		self.diver_choice.SetSelection( 0 )
		fgSizer2.Add( self.diver_choice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.datePicker = wx.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
		fgSizer2.Add( self.datePicker, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.diver_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Tender", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.diver_staticText1.Wrap( -1 )
		fgSizer2.Add( self.diver_staticText1, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		tender_choiceChoices = []
		self.tender_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), tender_choiceChoices, 0 )
		self.tender_choice.SetSelection( 0 )
		fgSizer2.Add( self.tender_choice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer3.Add( fgSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline61 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline61, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Target dive time:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer3.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 1, 4, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Hrs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		fgSizer3.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.TargetHr_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.TargetHr_textCtrl.SetMaxLength( 2 ) 
		fgSizer3.Add( self.TargetHr_textCtrl, 0, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Min", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		fgSizer3.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.TargetMin_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.TargetMin_textCtrl.SetMaxLength( 2 ) 
		fgSizer3.Add( self.TargetMin_textCtrl, 0, wx.ALL, 5 )
		
		bSizer3.Add( fgSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer41 = wx.FlexGridSizer( 5, 2, 0, 0 )
		fgSizer41.SetFlexibleDirection( wx.BOTH )
		fgSizer41.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.total_staticText = wx.StaticText( self, wx.ID_ANY, u"Total dive time today:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.total_staticText.Wrap( -1 )
		fgSizer41.Add( self.total_staticText, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.total_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), wx.TE_READONLY )
		self.total_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer41.Add( self.total_textCtrl, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Countdown to target:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer41.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.countdown_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"05:00:00", wx.DefaultPosition, wx.Size( 120,-1 ), wx.TE_READONLY )
		self.countdown_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer41.Add( self.countdown_textCtrl, 0, wx.ALL, 5 )
		
		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Dive Status:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		fgSizer41.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.status_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"Dive stopped", wx.DefaultPosition, wx.Size( 120,-1 ), wx.TE_READONLY )
		self.status_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer41.Add( self.status_textCtrl, 0, wx.ALL, 5 )
		
		bSizer3.Add( fgSizer41, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.startstop_button = wx.Button( self, wx.ID_ANY, u"Start Dive", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.startstop_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer7.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		bSizer4.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		# Connect Events
		self.diver_choice.Bind( wx.EVT_CHOICE, self._evtDiverChoice )
		self.datePicker.Bind( wx.EVT_DATE_CHANGED, self._evtDateChange )
		self.tender_choice.Bind( wx.EVT_CHOICE, self._evtTenderChoice )
		self.TargetHr_textCtrl.Bind( wx.EVT_TEXT, self._evtTargetHr )
		self.TargetMin_textCtrl.Bind( wx.EVT_TEXT, self._evtTargetMin )
		self.startstop_button.Bind( wx.EVT_BUTTON, self._evtStartStop )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtDiverChoice( self, event ):
		event.Skip()
	
	def _evtDateChange( self, event ):
		event.Skip()
	
	def _evtTenderChoice( self, event ):
		event.Skip()
	
	def _evtTargetHr( self, event ):
		event.Skip()
	
	def _evtTargetMin( self, event ):
		event.Skip()
	
	def _evtStartStop( self, event ):
		event.Skip()
	

###########################################################################
## Class DetailPanel
###########################################################################

class DetailPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText211 = wx.StaticText( self, wx.ID_ANY, u"Dive List / Editor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )
		self.m_staticText211.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer4.Add( self.m_staticText211, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline3, 0, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer8 = wx.FlexGridSizer( 1, 4, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.insert_Button = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"icons/insert.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.insert_Button.SetToolTipString( u"Insert Dive" )
		
		self.insert_Button.SetToolTipString( u"Insert Dive" )
		
		fgSizer8.Add( self.insert_Button, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.edit_Button = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"icons/edit.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.edit_Button.Enable( False )
		self.edit_Button.SetToolTipString( u"Edit Dive" )
		
		self.edit_Button.Enable( False )
		self.edit_Button.SetToolTipString( u"Edit Dive" )
		
		fgSizer8.Add( self.edit_Button, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.delete_Button = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"icons/delete.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.delete_Button.Enable( False )
		self.delete_Button.SetToolTipString( u"Delete Dive" )
		
		self.delete_Button.Enable( False )
		self.delete_Button.SetToolTipString( u"Delete Dive" )
		
		fgSizer8.Add( self.delete_Button, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		bSizer4.Add( fgSizer8, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		times_listBoxChoices = []
		self.times_listBox = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,200 ), times_listBoxChoices, wx.LB_SINGLE )
		bSizer4.Add( self.times_listBox, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( bSizer4 )
		self.Layout()
		bSizer4.Fit( self )
		
		# Connect Events
		self.insert_Button.Bind( wx.EVT_BUTTON, self._evtInsEntry )
		self.edit_Button.Bind( wx.EVT_BUTTON, self._evtEditEntry )
		self.delete_Button.Bind( wx.EVT_BUTTON, self._evtDeleteEntry )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtInsEntry( self, event ):
		event.Skip()
	
	def _evtEditEntry( self, event ):
		event.Skip()
	
	def _evtDeleteEntry( self, event ):
		event.Skip()
	

###########################################################################
## Class DataPanel
###########################################################################

class DataPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText85 = wx.StaticText( self, wx.ID_ANY, u"Live Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText85.Wrap( -1 )
		self.m_staticText85.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer4.Add( self.m_staticText85, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline62 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline62, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer9 = wx.FlexGridSizer( 4, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText40 = wx.StaticText( self, wx.ID_ANY, u"Date / Time:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )
		self.m_staticText40.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer9.Add( self.m_staticText40, 0, wx.ALL, 5 )
		
		self.date_staticText = wx.StaticText( self, wx.ID_ANY, u"Monday, 0:00:00 AM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.date_staticText.Wrap( -1 )
		self.date_staticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer9.Add( self.date_staticText, 0, wx.ALL, 5 )
		
		self.m_staticText281 = wx.StaticText( self, wx.ID_ANY, u"Latitude:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText281.Wrap( -1 )
		fgSizer9.Add( self.m_staticText281, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.lat_staticText = wx.StaticText( self, wx.ID_ANY, u"00.000000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lat_staticText.Wrap( -1 )
		fgSizer9.Add( self.lat_staticText, 0, wx.ALL, 5 )
		
		self.m_staticText2811 = wx.StaticText( self, wx.ID_ANY, u"Longitude:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2811.Wrap( -1 )
		fgSizer9.Add( self.m_staticText2811, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.long_staticText = wx.StaticText( self, wx.ID_ANY, u"000.000000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.long_staticText.Wrap( -1 )
		fgSizer9.Add( self.long_staticText, 0, wx.ALL, 5 )
		
		self.m_staticText28111 = wx.StaticText( self, wx.ID_ANY, u"Vessel Bearing:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28111.Wrap( -1 )
		fgSizer9.Add( self.m_staticText28111, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.bearing_staticText = wx.StaticText( self, wx.ID_ANY, u"000.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bearing_staticText.Wrap( -1 )
		fgSizer9.Add( self.bearing_staticText, 0, wx.ALL, 5 )
		
		bSizer4.Add( fgSizer9, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( bSizer4 )
		self.Layout()
		bSizer4.Fit( self )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class EditDlg
###########################################################################

class EditDlg ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Edit Dive Record", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.CAPTION|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer3 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		self.m_staticText19.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		gSizer3.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		self.m_staticText20.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		gSizer3.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer4.Add( gSizer3, 0, wx.EXPAND, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 3, 7, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.shrtxt = wx.StaticText( self, wx.ID_ANY, u"Hour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.shrtxt.Wrap( -1 )
		fgSizer3.Add( self.shrtxt, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.smintxt = wx.StaticText( self, wx.ID_ANY, u"Minute", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.smintxt.Wrap( -1 )
		fgSizer3.Add( self.smintxt, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.hrtxt = wx.StaticText( self, wx.ID_ANY, u"Hour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hrtxt.Wrap( -1 )
		self.hrtxt.Enable( False )
		
		fgSizer3.Add( self.hrtxt, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		self.mintxt = wx.StaticText( self, wx.ID_ANY, u"Minute", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mintxt.Wrap( -1 )
		self.mintxt.Enable( False )
		
		fgSizer3.Add( self.mintxt, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.sthr = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.sthr.SetMaxLength( 2 ) 
		fgSizer3.Add( self.sthr, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.stmin = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.stmin.SetMaxLength( 2 ) 
		fgSizer3.Add( self.stmin, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		stampmChoices = [ u"AM", u"PM" ]
		self.stampm = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,-1 ), stampmChoices, 0 )
		self.stampm.SetSelection( 0 )
		fgSizer3.Add( self.stampm, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.enhr = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.enhr.SetMaxLength( 2 ) 
		self.enhr.Enable( False )
		
		fgSizer3.Add( self.enhr, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.enmin = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.enmin.SetMaxLength( 2 ) 
		self.enmin.Enable( False )
		
		fgSizer3.Add( self.enmin, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		enampmChoices = [ u"AM", u"PM" ]
		self.enampm = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,-1 ), enampmChoices, 0 )
		self.enampm.SetSelection( 0 )
		self.enampm.Enable( False )
		
		fgSizer3.Add( self.enampm, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer4.Add( fgSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer4.AddSpacer( ( 0, 0), 0, wx.TOP|wx.BOTTOM, 5 )
		
		self.m_staticline7 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.tender_staticText = wx.StaticText( self, wx.ID_ANY, u"Tender", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tender_staticText.Wrap( -1 )
		fgSizer2.Add( self.tender_staticText, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		tender_choiceChoices = []
		self.tender_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, tender_choiceChoices, 0 )
		self.tender_choice.SetSelection( 2 )
		fgSizer2.Add( self.tender_choice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer4.Add( fgSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline61 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline61, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer9 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticTextLat = wx.StaticText( self, wx.ID_ANY, u"Latitude:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextLat.Wrap( -1 )
		fgSizer9.Add( self.m_staticTextLat, 0, wx.ALL, 5 )
		
		self.lat_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"00.000000", wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
		self.lat_textCtrl.SetMaxLength( 12 ) 
		fgSizer9.Add( self.lat_textCtrl, 0, wx.ALL, 5 )
		
		self.m_staticTextLon = wx.StaticText( self, wx.ID_ANY, u"Longitude:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextLon.Wrap( -1 )
		fgSizer9.Add( self.m_staticTextLon, 0, wx.ALL, 5 )
		
		self.lon_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"000.000000", wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
		self.lon_textCtrl.SetMaxLength( 12 ) 
		fgSizer9.Add( self.lon_textCtrl, 0, wx.ALL, 5 )
		
		self.m_staticTextBearing = wx.StaticText( self, wx.ID_ANY, u"Vessel Bearing:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextBearing.Wrap( -1 )
		fgSizer9.Add( self.m_staticTextBearing, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.bearing_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"000.00", wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
		self.bearing_textCtrl.SetMaxLength( 6 ) 
		fgSizer9.Add( self.bearing_textCtrl, 0, wx.ALL, 5 )
		
		bSizer4.Add( fgSizer9, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer10 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.okbutton = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.okbutton, 0, wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_button6, 0, wx.ALL, 5 )
		
		bSizer4.Add( fgSizer10, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( bSizer4 )
		self.Layout()
		bSizer4.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.sthr.Bind( wx.EVT_TEXT, self._evtHr )
		self.stmin.Bind( wx.EVT_TEXT, self._evtMinSec )
		self.enhr.Bind( wx.EVT_TEXT, self._evtHr )
		self.enmin.Bind( wx.EVT_TEXT, self._evtMinSec )
		self.okbutton.Bind( wx.EVT_BUTTON, self._evtOK )
		self.m_button6.Bind( wx.EVT_BUTTON, self._evtCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtHr( self, event ):
		event.Skip()
	
	def _evtMinSec( self, event ):
		event.Skip()
	
	
	
	def _evtOK( self, event ):
		event.Skip()
	
	def _evtCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class ConfirmDlg
###########################################################################

class ConfirmDlg ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Confirmation needed:", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.CAPTION|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.message = wx.StaticText( self, wx.ID_ANY, u"Are you sure you would like to delete this?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.message.Wrap( -1 )
		bSizer5.Add( self.message, 0, wx.ALL, 5 )
		
		gSizer2 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.cancelButton = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.cancelButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.yesButton = wx.Button( self, wx.ID_ANY, u"Yes", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.yesButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer5.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer5 )
		self.Layout()
		bSizer5.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.cancelButton.Bind( wx.EVT_BUTTON, self._evtCancel )
		self.yesButton.Bind( wx.EVT_BUTTON, self._evtYes )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtCancel( self, event ):
		event.Skip()
	
	def _evtYes( self, event ):
		event.Skip()
	

###########################################################################
## Class GridPanel
###########################################################################

class GridPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Dive Table", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		self.m_staticText19.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer6.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline36 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer6.Add( self.m_staticline36, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer12 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText39 = wx.StaticText( self, wx.ID_ANY, u"Cleanup / Round", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )
		fgSizer12.Add( self.m_staticText39, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		cround_choiceChoices = []
		self.cround_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cround_choiceChoices, 0 )
		self.cround_choice.SetSelection( 0 )
		fgSizer12.Add( self.cround_choice, 0, wx.ALL, 5 )
		
		self.newRound_button = wx.Button( self, wx.ID_ANY, u"Start New Round", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer12.Add( self.newRound_button, 0, wx.ALL, 5 )
		
		bSizer6.Add( fgSizer12, 0, 0, 5 )
		
		self.grid = Grid.CustTableGrid(self,  'C:\ProgramData\DiveRT\DiveRT.db')
		bSizer6.Add( self.grid, 0, wx.ALL, 5 )
		
		self.SetSizer( bSizer6 )
		self.Layout()
		
		# Connect Events
		self.cround_choice.Bind( wx.EVT_CHOICE, self._evtRoundChange )
		self.newRound_button.Bind( wx.EVT_BUTTON, self._evtNewRound )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtRoundChange( self, event ):
		event.Skip()
	
	def _evtNewRound( self, event ):
		event.Skip()
	

###########################################################################
## Class GPSSettings
###########################################################################

class GPSSettings ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"GPS Settings", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText = wx.StaticText( self, wx.ID_ANY, u"Select GPS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText.Wrap( -1 )
		self.m_staticText.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer11.Add( self.m_staticText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline13 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer16 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer16.SetFlexibleDirection( wx.BOTH )
		fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"COM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		fgSizer16.Add( self.m_staticText50, 0, wx.ALL, 5 )
		
		self.com_spinCtrl = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 99, 1 )
		fgSizer16.Add( self.com_spinCtrl, 0, wx.ALL, 5 )
		
		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"BAUD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		fgSizer16.Add( self.m_staticText51, 0, wx.ALL, 5 )
		
		baud_comboBoxChoices = [ u"4800", u"38400" ]
		self.baud_comboBox = wx.ComboBox( self, wx.ID_ANY, u"4800", wx.DefaultPosition, wx.DefaultSize, baud_comboBoxChoices, 0 )
		fgSizer16.Add( self.baud_comboBox, 0, wx.ALL, 5 )
		
		bSizer11.Add( fgSizer16, 0, wx.EXPAND, 5 )
		
		self.m_button131 = wx.Button( self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button131, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline15 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline15, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_button13 = wx.Button( self, wx.ID_ANY, u"Done", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( bSizer11 )
		self.Layout()
		bSizer11.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self._evtDone )
		self.Bind( wx.EVT_INIT_DIALOG, self.SetCtrlValues )
		self.m_button131.Bind( wx.EVT_BUTTON, self._evtCom )
		self.m_button13.Bind( wx.EVT_BUTTON, self._evtDone )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtDone( self, event ):
		event.Skip()
	
	def SetCtrlValues( self, event ):
		event.Skip()
	
	def _evtCom( self, event ):
		event.Skip()
	
	

###########################################################################
## Class CrewManager
###########################################################################

class CrewManager ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Crew Manager", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bxSizer = wx.BoxSizer( wx.VERTICAL )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer = wx.FlexGridSizer( 99, 4, 0, 0 )
		fgSizer.SetFlexibleDirection( wx.BOTH )
		fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.name_staticText = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name_staticText.Wrap( -1 )
		fgSizer.Add( self.name_staticText, 0, wx.ALL, 5 )
		
		self.duty_staticText = wx.StaticText( self, wx.ID_ANY, u"Duty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.duty_staticText.Wrap( -1 )
		fgSizer.Add( self.duty_staticText, 0, wx.ALL, 5 )
		
		self.diveRate_staticText = wx.StaticText( self, wx.ID_ANY, u"Dive Rate  (% of time)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.diveRate_staticText.Wrap( -1 )
		fgSizer.Add( self.diveRate_staticText, 0, wx.ALL, 5 )
		
		self.tenderRate_staticText = wx.StaticText( self, wx.ID_ANY, u"Tender Rate ($/hr)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tenderRate_staticText.Wrap( -1 )
		fgSizer.Add( self.tenderRate_staticText, 0, wx.ALL, 5 )
		
		self.name_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.name_textCtrl, 0, wx.ALL, 5 )
		
		duty_choiceChoices = [ u"Diver and Tender", u"Tender" ]
		self.duty_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, duty_choiceChoices, 0 )
		self.duty_choice.SetSelection( 0 )
		fgSizer.Add( self.duty_choice, 0, wx.ALL, 5 )
		
		self.diveRate_spinCtrl = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 25, 100, 50 )
		fgSizer.Add( self.diveRate_spinCtrl, 0, wx.ALL, 5 )
		
		self.tenderRate_spinCtrl = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 10, 40, 0 )
		fgSizer.Add( self.tenderRate_spinCtrl, 0, wx.ALL, 5 )
		
		bSizer11.Add( fgSizer, 1, wx.EXPAND, 5 )
		
		bxSizer.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		self.save_button = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bxSizer.Add( self.save_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bxSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.SetSizer( bxSizer )
		self.Layout()
		bxSizer.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.name_textCtrl.Bind( wx.EVT_TEXT, self._evtNameTxt )
		self.save_button.Bind( wx.EVT_BUTTON, self._evtSave )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtNameTxt( self, event ):
		event.Skip()
	
	def _evtSave( self, event ):
		event.Skip()
	
