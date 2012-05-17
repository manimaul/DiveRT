# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 30 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class DivePanel
###########################################################################

class DivePanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
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
		bSizer4.Fit( self )
		
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
		
		fgSizer8.Add( self.insert_Button, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.edit_Button = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"icons/edit.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.edit_Button.Enable( False )
		self.edit_Button.SetToolTipString( u"Edit Dive" )
		
		fgSizer8.Add( self.edit_Button, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.delete_Button = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"icons/delete.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.delete_Button.Enable( False )
		self.delete_Button.SetToolTipString( u"Delete Dive" )
		
		fgSizer8.Add( self.delete_Button, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		bSizer4.Add( fgSizer8, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		times_listBoxChoices = []
		self.times_listBox = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,150 ), times_listBoxChoices, wx.LB_SINGLE )
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
		
		fgSizer9 = wx.FlexGridSizer( 3, 3, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticTextLat = wx.StaticText( self, wx.ID_ANY, u"Latitude:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextLat.Wrap( -1 )
		fgSizer9.Add( self.m_staticTextLat, 0, wx.ALL, 5 )
		
		self.lat_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"00.000000", wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
		self.lat_textCtrl.SetMaxLength( 12 ) 
		fgSizer9.Add( self.lat_textCtrl, 0, wx.ALL, 5 )
		
		lat_choiceChoices = [ u"N", u"S" ]
		self.lat_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lat_choiceChoices, 0 )
		self.lat_choice.SetSelection( 0 )
		fgSizer9.Add( self.lat_choice, 0, wx.ALL, 5 )
		
		self.m_staticTextLon = wx.StaticText( self, wx.ID_ANY, u"Longitude:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextLon.Wrap( -1 )
		fgSizer9.Add( self.m_staticTextLon, 0, wx.ALL, 5 )
		
		self.lon_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"000.000000", wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
		self.lon_textCtrl.SetMaxLength( 12 ) 
		fgSizer9.Add( self.lon_textCtrl, 0, wx.ALL, 5 )
		
		lon_choiceChoices = [ u"W", u"E" ]
		self.lon_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lon_choiceChoices, 0 )
		self.lon_choice.SetSelection( 0 )
		fgSizer9.Add( self.lon_choice, 0, wx.ALL, 5 )
		
		self.m_staticTextBearing = wx.StaticText( self, wx.ID_ANY, u"Vessel Bearing:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextBearing.Wrap( -1 )
		fgSizer9.Add( self.m_staticTextBearing, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.bearing_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"000.00", wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
		self.bearing_textCtrl.SetMaxLength( 8 ) 
		fgSizer9.Add( self.bearing_textCtrl, 0, wx.ALL, 5 )
		
		bearing_choiceChoices = [ u"M", u"T" ]
		self.bearing_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, bearing_choiceChoices, 0 )
		self.bearing_choice.SetSelection( 0 )
		fgSizer9.Add( self.bearing_choice, 0, wx.ALL, 5 )
		
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
		self.lat_textCtrl.Bind( wx.EVT_TEXT, self._evtLatTxt )
		self.lon_textCtrl.Bind( wx.EVT_TEXT, self._evtLonTxt )
		self.bearing_textCtrl.Bind( wx.EVT_TEXT, self._evtBearingTxt )
		self.okbutton.Bind( wx.EVT_BUTTON, self._evtOK )
		self.m_button6.Bind( wx.EVT_BUTTON, self._evtCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtHr( self, event ):
		event.Skip()
	
	def _evtMinSec( self, event ):
		event.Skip()
	
	
	
	def _evtLatTxt( self, event ):
		event.Skip()
	
	def _evtLonTxt( self, event ):
		event.Skip()
	
	def _evtBearingTxt( self, event ):
		event.Skip()
	
	def _evtOK( self, event ):
		event.Skip()
	
	def _evtCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class MsgDialog
###########################################################################

class MsgDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Message", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.CAPTION )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.msg_staticText = wx.StaticText( self, wx.ID_ANY, u"Message", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.msg_staticText.Wrap( -1 )
		self.bSizer.Add( self.msg_staticText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button13 = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bSizer.Add( self.m_button13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( self.bSizer )
		self.Layout()
		self.bSizer.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button13.Bind( wx.EVT_BUTTON, self._evtOK )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtOK( self, event ):
		event.Skip()
	

###########################################################################
## Class ConfirmDlg
###########################################################################

class ConfirmDlg ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Confirmation needed:", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.CAPTION|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.message = wx.StaticText( self, wx.ID_ANY, u"Are you sure you would like to delete this?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.message.Wrap( -1 )
		self.bSizer.Add( self.message, 0, wx.ALL, 5 )
		
		gSizer2 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.cancelButton = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.cancelButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.yesButton = wx.Button( self, wx.ID_ANY, u"Yes", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.yesButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.bSizer.Add( gSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( self.bSizer )
		self.Layout()
		self.bSizer.Fit( self )
		
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
## Class GPSSettings
###########################################################################

class GPSSettings ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"GPS Settings", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.CAPTION )
		
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
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Crew Manager", pos = wx.DefaultPosition, size = wx.Size( 582,422 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.bxSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.scrollWin = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.scrollWin.SetScrollRate( 5, 5 )
		self.fgSizer = wx.FlexGridSizer( 99, 4, 0, 0 )
		self.fgSizer.SetFlexibleDirection( wx.BOTH )
		self.fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.name_staticText = wx.StaticText( self.scrollWin, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name_staticText.Wrap( -1 )
		self.fgSizer.Add( self.name_staticText, 0, wx.ALL, 5 )
		
		self.duty_staticText = wx.StaticText( self.scrollWin, wx.ID_ANY, u"Duty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.duty_staticText.Wrap( -1 )
		self.fgSizer.Add( self.duty_staticText, 0, wx.ALL, 5 )
		
		self.diveRate_staticText = wx.StaticText( self.scrollWin, wx.ID_ANY, u"Dive Rate  (% of time)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.diveRate_staticText.Wrap( -1 )
		self.fgSizer.Add( self.diveRate_staticText, 0, wx.ALL, 5 )
		
		self.name_textCtrl = wx.TextCtrl( self.scrollWin, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fgSizer.Add( self.name_textCtrl, 0, wx.ALL, 5 )
		
		duty_choiceChoices = [ u"Diver and Tender", u"Tender" ]
		self.duty_choice = wx.Choice( self.scrollWin, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, duty_choiceChoices, 0 )
		self.duty_choice.SetSelection( 0 )
		self.fgSizer.Add( self.duty_choice, 0, wx.ALL, 5 )
		
		self.diveRate_spinCtrl = wx.SpinCtrl( self.scrollWin, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 25, 100, 50 )
		self.fgSizer.Add( self.diveRate_spinCtrl, 0, wx.ALL, 5 )
		
		self.scrollWin.SetSizer( self.fgSizer )
		self.scrollWin.Layout()
		self.fgSizer.Fit( self.scrollWin )
		self.bxSizer1.Add( self.scrollWin, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline16 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bxSizer1.Add( self.m_staticline16, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgs = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgs.SetFlexibleDirection( wx.BOTH )
		fgs.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.save_button = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgs.Add( self.save_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button16 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgs.Add( self.m_button16, 0, wx.ALL, 5 )
		
		self.bxSizer1.Add( fgs, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( self.bxSizer1 )
		self.Layout()
		
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
	

###########################################################################
## Class About
###########################################################################

class About ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About DiveRT", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.titleVersion = wx.StaticText( self, wx.ID_ANY, u"Dive RT v0.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titleVersion.Wrap( -1 )
		self.titleVersion.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer12.Add( self.titleVersion, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.bssm_bitmap = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"icons/mvtt.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.bssm_bitmap, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self._staticText41 = wx.StaticText( self, wx.ID_ANY, u"DiveRT <Dive Recovery Tracker>\nCopyright (C) 2012 Will Kamp <manimaul!gmail.com>\n\nDiveRT was created for Bering SubSea Mining and the crews aboard Norpac, Tahta and Julianna.  Use of DiveRT without the expressed permission from Will Kamp is prohibited.\n\nDiveRT records diver and tender dive times, position and bearing data into a sqlite3 database\nConnects to Nema0183 GPS and bearing sensor (reads HDT,HDG*, RMC, GGA data)\n\n*12.3 degrees magnetic variance will be added to magnetic readings on map", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._staticText41.Wrap( -1 )
		bSizer12.Add( self._staticText41, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button10 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( bSizer12 )
		self.Layout()
		bSizer12.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self._evtOK )
		self.m_button10.Bind( wx.EVT_BUTTON, self._evtOK )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtOK( self, event ):
		event.Skip()
	
	

###########################################################################
## Class RoundReportTahta
###########################################################################

class RoundReportTahta ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Cleanup Round Report", pos = wx.Point( -1,-1 ), size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, u"Cleanup / Round Report", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText44.Wrap( -1 )
		self.m_staticText44.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		
		self.bSizer.Add( self.m_staticText44, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline14 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizer.Add( self.m_staticline14, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.scrollwindow = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.scrollwindow.SetScrollRate( 5, 5 )
		self.bSizerX = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer20 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer20.SetFlexibleDirection( wx.BOTH )
		fgSizer20.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText60 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Cleanup / Round", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText60.Wrap( -1 )
		fgSizer20.Add( self.m_staticText60, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		round_choiceChoices = []
		self.round_choice = wx.Choice( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.Size( 60,-1 ), round_choiceChoices, 0 )
		self.round_choice.SetSelection( 0 )
		fgSizer20.Add( self.round_choice, 0, wx.ALL, 5 )
		
		self.dateRange_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Jan, 00 to Jan, 00 2000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dateRange_staticText.Wrap( -1 )
		fgSizer20.Add( self.dateRange_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.bSizerX.Add( fgSizer20, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline13 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizerX.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer14 = wx.FlexGridSizer( 4, 2, 0, 0 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText42 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Total Dive Hours", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		fgSizer14.Add( self.m_staticText42, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.totalHours_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_READONLY )
		self.totalHours_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer14.Add( self.totalHours_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText43 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Total Grams", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )
		fgSizer14.Add( self.m_staticText43, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.totalGrams_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		fgSizer14.Add( self.totalGrams_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText71 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Total Troy Ounces", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		fgSizer14.Add( self.m_staticText71, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.totalOz_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		fgSizer14.Add( self.totalOz_textCtrl, 0, wx.ALL, 5 )
		
		self.m_staticText86 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Ounces / Hr", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText86.Wrap( -1 )
		fgSizer14.Add( self.m_staticText86, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.ozPerHr_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_READONLY )
		self.ozPerHr_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer14.Add( self.ozPerHr_textCtrl, 0, wx.ALL, 5 )
		
		bSizer13.Add( fgSizer14, 0, 0, 5 )
		
		self.m_staticline17 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer13.Add( self.m_staticline17, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer171 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer171.SetFlexibleDirection( wx.BOTH )
		fgSizer171.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText51 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Estimated Refinement Recovery", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		fgSizer171.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.percentLoss_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, u"80", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		fgSizer171.Add( self.percentLoss_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText50 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"London Spot Price", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		fgSizer171.Add( self.m_staticText50, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.londonSpot_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		fgSizer171.Add( self.londonSpot_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText78 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Estimated Refinement Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText78.Wrap( -1 )
		fgSizer171.Add( self.m_staticText78, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.estTotal_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY )
		self.estTotal_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer171.Add( self.estTotal_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer13.Add( fgSizer171, 0, 0, 5 )
		
		self.bSizerX.Add( bSizer13, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline12 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizerX.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText64 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Dredge Owner", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText64.Wrap( -1 )
		self.m_staticText64.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		self.bSizerX.Add( self.m_staticText64, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer18 = wx.FlexGridSizer( 1, 8, 0, 0 )
		fgSizer18.SetFlexibleDirection( wx.BOTH )
		fgSizer18.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.ownerPct_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Percent", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ownerPct_staticText.Wrap( -1 )
		fgSizer18.Add( self.ownerPct_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.ownerPercent_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, u"55", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.ownerPercent_textCtrl.SetMaxLength( 6 ) 
		fgSizer18.Add( self.ownerPercent_textCtrl, 0, wx.ALL, 5 )
		
		self.ownerPct_staticline = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		fgSizer18.Add( self.ownerPct_staticline, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.remainder_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Gross Grams", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.remainder_staticText.Wrap( -1 )
		fgSizer18.Add( self.remainder_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.ownerGrams_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_READONLY )
		self.ownerGrams_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer18.Add( self.ownerGrams_textCtrl, 0, wx.ALL, 5 )
		
		self.m_staticline19 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		fgSizer18.Add( self.m_staticline19, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText612 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Estimated Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText612.Wrap( -1 )
		fgSizer18.Add( self.m_staticText612, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.ownerEstimate_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY )
		self.ownerEstimate_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer18.Add( self.ownerEstimate_textCtrl, 0, wx.ALL, 5 )
		
		self.bSizerX.Add( fgSizer18, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.opDiver_staticline1 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizerX.Add( self.opDiver_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.opDiver_staticText1 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Operator / Divers", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.opDiver_staticText1.Wrap( -1 )
		self.opDiver_staticText1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		self.bSizerX.Add( self.opDiver_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer181 = wx.FlexGridSizer( 2, 8, 0, 0 )
		fgSizer181.SetFlexibleDirection( wx.BOTH )
		fgSizer181.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.opDiverPct_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Percent", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.opDiverPct_staticText.Wrap( -1 )
		fgSizer181.Add( self.opDiverPct_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.operatorPercent_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, u"45", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.operatorPercent_textCtrl.SetMaxLength( 6 ) 
		fgSizer181.Add( self.operatorPercent_textCtrl, 0, wx.ALL, 5 )
		
		self.m_staticline211 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		fgSizer181.Add( self.m_staticline211, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.opDiverGross_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Gross Grams", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.opDiverGross_staticText.Wrap( -1 )
		fgSizer181.Add( self.opDiverGross_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.operatorGrams_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_READONLY )
		self.operatorGrams_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer181.Add( self.operatorGrams_textCtrl, 0, wx.ALL, 5 )
		
		self.m_staticline28 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		fgSizer181.Add( self.m_staticline28, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.opDiverEstValue_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Estimated Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.opDiverEstValue_staticText.Wrap( -1 )
		fgSizer181.Add( self.opDiverEstValue_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.operatorEstimate_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY )
		self.operatorEstimate_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer181.Add( self.operatorEstimate_textCtrl, 0, wx.ALL, 5 )
		
		
		fgSizer181.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer181.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer181.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.opDiverNet_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Net Grams", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.opDiverNet_staticText.Wrap( -1 )
		fgSizer181.Add( self.opDiverNet_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.operNetGrams_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_READONLY )
		self.operNetGrams_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer181.Add( self.operNetGrams_textCtrl, 0, wx.ALL, 5 )
		
		
		fgSizer181.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.bSizerX.Add( fgSizer181, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.opDiver_staticline2 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizerX.Add( self.opDiver_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.opDiver_staticText2 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Operator / Diver Distribution", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.opDiver_staticText2.Wrap( -1 )
		self.opDiver_staticText2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		self.bSizerX.Add( self.opDiver_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.diving_fgSizer = wx.FlexGridSizer( 99, 4, 0, 0 )
		self.diving_fgSizer.SetFlexibleDirection( wx.BOTH )
		self.diving_fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.opDiverName_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.opDiverName_staticText.Wrap( -1 )
		self.diving_fgSizer.Add( self.opDiverName_staticText, 0, wx.ALL, 5 )
		
		self.opDiverHours_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Hours", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.opDiverHours_staticText.Wrap( -1 )
		self.diving_fgSizer.Add( self.opDiverHours_staticText, 0, wx.ALL, 5 )
		
		self.opDiverGrams_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Grams", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.opDiverGrams_staticText.Wrap( -1 )
		self.diving_fgSizer.Add( self.opDiverGrams_staticText, 0, wx.ALL, 5 )
		
		self.opDiverEstValue_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Estimated Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.opDiverEstValue_staticText.Wrap( -1 )
		self.diving_fgSizer.Add( self.opDiverEstValue_staticText, 0, wx.ALL, 5 )
		
		self.bSizerX.Add( self.diving_fgSizer, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.extraDiver_staticline = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizerX.Add( self.extraDiver_staticline, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.extraDiver_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Extra Diver Distribution", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.extraDiver_staticText.Wrap( -1 )
		self.extraDiver_staticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		self.bSizerX.Add( self.extraDiver_staticText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.extraDiving_fgSizer = wx.FlexGridSizer( 99, 5, 0, 0 )
		self.extraDiving_fgSizer.SetFlexibleDirection( wx.BOTH )
		self.extraDiving_fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.exName_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exName_staticText.Wrap( -1 )
		self.extraDiving_fgSizer.Add( self.exName_staticText, 0, wx.ALL, 5 )
		
		self.exHours_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Hours", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exHours_staticText.Wrap( -1 )
		self.extraDiving_fgSizer.Add( self.exHours_staticText, 0, wx.ALL, 5 )
		
		self.exPay_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Pay Rate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exPay_staticText.Wrap( -1 )
		self.extraDiving_fgSizer.Add( self.exPay_staticText, 0, wx.ALL, 5 )
		
		self.exGrams_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Grams", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exGrams_staticText.Wrap( -1 )
		self.extraDiving_fgSizer.Add( self.exGrams_staticText, 0, wx.ALL, 5 )
		
		self.exValue_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Estimated Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exValue_staticText.Wrap( -1 )
		self.extraDiving_fgSizer.Add( self.exValue_staticText, 0, wx.ALL, 5 )
		
		self.bSizerX.Add( self.extraDiving_fgSizer, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.scrollwindow.SetSizer( self.bSizerX )
		self.scrollwindow.Layout()
		self.bSizerX.Fit( self.scrollwindow )
		self.bSizer.Add( self.scrollwindow, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline26 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizer.Add( self.m_staticline26, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer17 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer17.SetFlexibleDirection( wx.BOTH )
		fgSizer17.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.save_button = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.save_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.printview_button = wx.Button( self, wx.ID_ANY, u"Print View", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.printview_button, 0, wx.ALL, 5 )
		
		self.cancel_button = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.cancel_button, 0, wx.ALL, 5 )
		
		self.bSizer.Add( fgSizer17, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( self.bSizer )
		self.Layout()
		self.bSizer.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self._evtClose )
		self.Bind( wx.EVT_INIT_DIALOG, self._evtInit )
		self.round_choice.Bind( wx.EVT_CHOICE, self._evtRoundChange )
		self.totalGrams_textCtrl.Bind( wx.EVT_KEY_UP, self._evtGramsChange )
		self.totalGrams_textCtrl.Bind( wx.EVT_KILL_FOCUS, self._evtSetGrams )
		self.totalOz_textCtrl.Bind( wx.EVT_KEY_UP, self._evtTozChange )
		self.totalOz_textCtrl.Bind( wx.EVT_KILL_FOCUS, self._evtSetTroyOz )
		self.percentLoss_textCtrl.Bind( wx.EVT_TEXT, self._evtPctLossChange )
		self.londonSpot_textCtrl.Bind( wx.EVT_TEXT, self._evtLondonSpotChange )
		self.ownerPercent_textCtrl.Bind( wx.EVT_KEY_UP, self._evtOwnerCut )
		self.operatorPercent_textCtrl.Bind( wx.EVT_KEY_UP, self._evtOperatorCut )
		self.save_button.Bind( wx.EVT_BUTTON, self._evtSave )
		self.printview_button.Bind( wx.EVT_BUTTON, self._evtPrintView )
		self.cancel_button.Bind( wx.EVT_BUTTON, self._evtClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtClose( self, event ):
		event.Skip()
	
	def _evtInit( self, event ):
		event.Skip()
	
	def _evtRoundChange( self, event ):
		event.Skip()
	
	def _evtGramsChange( self, event ):
		event.Skip()
	
	def _evtSetGrams( self, event ):
		event.Skip()
	
	def _evtTozChange( self, event ):
		event.Skip()
	
	def _evtSetTroyOz( self, event ):
		event.Skip()
	
	def _evtPctLossChange( self, event ):
		event.Skip()
	
	def _evtLondonSpotChange( self, event ):
		event.Skip()
	
	def _evtOwnerCut( self, event ):
		event.Skip()
	
	def _evtOperatorCut( self, event ):
		event.Skip()
	
	def _evtSave( self, event ):
		event.Skip()
	
	def _evtPrintView( self, event ):
		event.Skip()
	
	

###########################################################################
## Class SeasonReportTahta
###########################################################################

class SeasonReportTahta ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Season Report", pos = wx.Point( -1,-1 ), size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, u"Season Report", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText44.Wrap( -1 )
		self.m_staticText44.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		
		self.bSizer.Add( self.m_staticText44, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline14 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizer.Add( self.m_staticline14, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.scrollwindow = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.scrollwindow.SetScrollRate( 5, 5 )
		self.bSizerX = wx.BoxSizer( wx.VERTICAL )
		
		self.dateRange_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Jan, 00 to Jan, 00 2000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dateRange_staticText.Wrap( -1 )
		self.bSizerX.Add( self.dateRange_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline13 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizerX.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer14 = wx.FlexGridSizer( 4, 2, 0, 0 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText42 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Total Dive Hours", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		fgSizer14.Add( self.m_staticText42, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.totalHours_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_READONLY )
		self.totalHours_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer14.Add( self.totalHours_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText43 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Total Grams", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )
		fgSizer14.Add( self.m_staticText43, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.totalGrams_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_READONLY )
		self.totalGrams_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer14.Add( self.totalGrams_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText71 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Total Troy Ounces", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		fgSizer14.Add( self.m_staticText71, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.totalOz_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_READONLY )
		self.totalOz_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer14.Add( self.totalOz_textCtrl, 0, wx.ALL, 5 )
		
		self.m_staticText86 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Avg. Ounces / Hr", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText86.Wrap( -1 )
		fgSizer14.Add( self.m_staticText86, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.ozPerHr_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_READONLY )
		self.ozPerHr_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer14.Add( self.ozPerHr_textCtrl, 0, wx.ALL, 5 )
		
		bSizer13.Add( fgSizer14, 0, 0, 5 )
		
		self.m_staticline17 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer13.Add( self.m_staticline17, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer171 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer171.SetFlexibleDirection( wx.BOTH )
		fgSizer171.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText51 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Estimated Refinement Recovery", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		fgSizer171.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.percentLoss_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, u"80", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		fgSizer171.Add( self.percentLoss_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText50 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"London Spot Price", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		fgSizer171.Add( self.m_staticText50, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.londonSpot_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		fgSizer171.Add( self.londonSpot_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText78 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Estimated Refinement Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText78.Wrap( -1 )
		fgSizer171.Add( self.m_staticText78, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.estTotal_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY )
		self.estTotal_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer171.Add( self.estTotal_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer13.Add( fgSizer171, 0, 0, 5 )
		
		self.bSizerX.Add( bSizer13, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline12 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizerX.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText64 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Dredge Owner", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText64.Wrap( -1 )
		self.m_staticText64.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		self.bSizerX.Add( self.m_staticText64, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer18 = wx.FlexGridSizer( 1, 8, 0, 0 )
		fgSizer18.SetFlexibleDirection( wx.BOTH )
		fgSizer18.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.remainder_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Gross Grams", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.remainder_staticText.Wrap( -1 )
		fgSizer18.Add( self.remainder_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.ownerGrams_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_READONLY )
		self.ownerGrams_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer18.Add( self.ownerGrams_textCtrl, 0, wx.ALL, 5 )
		
		self.m_staticline19 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		fgSizer18.Add( self.m_staticline19, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText612 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Estimated Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText612.Wrap( -1 )
		fgSizer18.Add( self.m_staticText612, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.ownerEstimate_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY )
		self.ownerEstimate_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer18.Add( self.ownerEstimate_textCtrl, 0, wx.ALL, 5 )
		
		self.bSizerX.Add( fgSizer18, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline15 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizerX.Add( self.m_staticline15, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText63 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Operator / Divers", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )
		self.m_staticText63.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		self.bSizerX.Add( self.m_staticText63, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer181 = wx.FlexGridSizer( 2, 10, 0, 0 )
		fgSizer181.SetFlexibleDirection( wx.BOTH )
		fgSizer181.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.remainder_staticText1 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Gross Grams", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.remainder_staticText1.Wrap( -1 )
		fgSizer181.Add( self.remainder_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.operatorGrams_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_READONLY )
		self.operatorGrams_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer181.Add( self.operatorGrams_textCtrl, 0, wx.ALL, 5 )
		
		self.m_staticline28 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		fgSizer181.Add( self.m_staticline28, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText85 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Net Grams", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText85.Wrap( -1 )
		fgSizer181.Add( self.m_staticText85, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.operNetGrams_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_READONLY )
		self.operNetGrams_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer181.Add( self.operNetGrams_textCtrl, 0, wx.ALL, 5 )
		
		self.m_staticline49 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		fgSizer181.Add( self.m_staticline49, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText6121 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Estimated Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6121.Wrap( -1 )
		fgSizer181.Add( self.m_staticText6121, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.operatorEstimate_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY )
		self.operatorEstimate_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer181.Add( self.operatorEstimate_textCtrl, 0, wx.ALL, 5 )
		
		self.bSizerX.Add( fgSizer181, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.opDiver_staticline = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizerX.Add( self.opDiver_staticline, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.opDiver_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Operator Diver Distribution", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.opDiver_staticText.Wrap( -1 )
		self.opDiver_staticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		self.bSizerX.Add( self.opDiver_staticText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.diving_fgSizer = wx.FlexGridSizer( 99, 5, 0, 0 )
		self.diving_fgSizer.SetFlexibleDirection( wx.BOTH )
		self.diving_fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.opDiverName_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.opDiverName_staticText.Wrap( -1 )
		self.diving_fgSizer.Add( self.opDiverName_staticText, 0, wx.ALL, 5 )
		
		self.opDiverHours_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Hours", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.opDiverHours_staticText.Wrap( -1 )
		self.diving_fgSizer.Add( self.opDiverHours_staticText, 0, wx.ALL, 5 )
		
		self.opDiverGrams_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Grams", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.opDiverGrams_staticText.Wrap( -1 )
		self.diving_fgSizer.Add( self.opDiverGrams_staticText, 0, wx.ALL, 5 )
		
		self.opDiverToz_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Troy Oz.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.opDiverToz_staticText.Wrap( -1 )
		self.diving_fgSizer.Add( self.opDiverToz_staticText, 0, wx.ALL, 5 )
		
		self.opDiverEstValue_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Estimated Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.opDiverEstValue_staticText.Wrap( -1 )
		self.diving_fgSizer.Add( self.opDiverEstValue_staticText, 0, wx.ALL, 5 )
		
		self.bSizerX.Add( self.diving_fgSizer, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.extraDiver_staticline = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizerX.Add( self.extraDiver_staticline, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.extraDiver_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Diver Distribution", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.extraDiver_staticText.Wrap( -1 )
		self.extraDiver_staticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		self.bSizerX.Add( self.extraDiver_staticText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.extraDiving_fgSizer = wx.FlexGridSizer( 99, 5, 0, 0 )
		self.extraDiving_fgSizer.SetFlexibleDirection( wx.BOTH )
		self.extraDiving_fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.exName_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exName_staticText.Wrap( -1 )
		self.extraDiving_fgSizer.Add( self.exName_staticText, 0, wx.ALL, 5 )
		
		self.exHours_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Hours", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exHours_staticText.Wrap( -1 )
		self.extraDiving_fgSizer.Add( self.exHours_staticText, 0, wx.ALL, 5 )
		
		self.exGrams_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Grams", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exGrams_staticText.Wrap( -1 )
		self.extraDiving_fgSizer.Add( self.exGrams_staticText, 0, wx.ALL, 5 )
		
		self.exOz_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Troy Oz.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exOz_staticText.Wrap( -1 )
		self.extraDiving_fgSizer.Add( self.exOz_staticText, 0, wx.ALL, 5 )
		
		self.exValue_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Estimated Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exValue_staticText.Wrap( -1 )
		self.extraDiving_fgSizer.Add( self.exValue_staticText, 0, wx.ALL, 5 )
		
		self.bSizerX.Add( self.extraDiving_fgSizer, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.scrollwindow.SetSizer( self.bSizerX )
		self.scrollwindow.Layout()
		self.bSizerX.Fit( self.scrollwindow )
		self.bSizer.Add( self.scrollwindow, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline26 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizer.Add( self.m_staticline26, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer17 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer17.SetFlexibleDirection( wx.BOTH )
		fgSizer17.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.printview_button = wx.Button( self, wx.ID_ANY, u"Print View", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.printview_button, 0, wx.ALL, 5 )
		
		self.cancel_button = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.cancel_button, 0, wx.ALL, 5 )
		
		self.bSizer.Add( fgSizer17, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( self.bSizer )
		self.Layout()
		self.bSizer.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self._evtClose )
		self.Bind( wx.EVT_INIT_DIALOG, self._evtInit )
		self.totalGrams_textCtrl.Bind( wx.EVT_KILL_FOCUS, self._evtSetGrams )
		self.totalOz_textCtrl.Bind( wx.EVT_KILL_FOCUS, self._evtSetTroyOz )
		self.percentLoss_textCtrl.Bind( wx.EVT_TEXT, self._evtLondonSpotChange )
		self.londonSpot_textCtrl.Bind( wx.EVT_TEXT, self._evtLondonSpotChange )
		self.printview_button.Bind( wx.EVT_BUTTON, self._evtPrintView )
		self.cancel_button.Bind( wx.EVT_BUTTON, self._evtClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtClose( self, event ):
		event.Skip()
	
	def _evtInit( self, event ):
		event.Skip()
	
	def _evtSetGrams( self, event ):
		event.Skip()
	
	def _evtSetTroyOz( self, event ):
		event.Skip()
	
	def _evtLondonSpotChange( self, event ):
		event.Skip()
	
	
	def _evtPrintView( self, event ):
		event.Skip()
	
	

###########################################################################
## Class RoundReport
###########################################################################

class RoundReport ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Cleanup Round Report", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, u"Cleanup / Round Report", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText44.Wrap( -1 )
		self.m_staticText44.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		
		self.bSizer.Add( self.m_staticText44, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline14 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizer.Add( self.m_staticline14, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.scrollwindow = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.scrollwindow.SetScrollRate( 5, 5 )
		self.bSizerX = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer20 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer20.SetFlexibleDirection( wx.BOTH )
		fgSizer20.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText60 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Cleanup / Round", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText60.Wrap( -1 )
		fgSizer20.Add( self.m_staticText60, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		round_choiceChoices = []
		self.round_choice = wx.Choice( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.Size( 60,-1 ), round_choiceChoices, 0 )
		self.round_choice.SetSelection( 0 )
		fgSizer20.Add( self.round_choice, 0, wx.ALL, 5 )
		
		self.dateRange_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Jan, 00 to Jan, 00 2000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dateRange_staticText.Wrap( -1 )
		fgSizer20.Add( self.dateRange_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.bSizerX.Add( fgSizer20, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline13 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizerX.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer14 = wx.FlexGridSizer( 4, 2, 0, 0 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText42 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Total Dive Hours", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		fgSizer14.Add( self.m_staticText42, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.totalHours_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_READONLY )
		self.totalHours_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer14.Add( self.totalHours_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText43 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Total Grams", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )
		fgSizer14.Add( self.m_staticText43, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.totalGrams_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		fgSizer14.Add( self.totalGrams_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText71 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Total Troy Ounces", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		fgSizer14.Add( self.m_staticText71, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.totalOz_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		fgSizer14.Add( self.totalOz_textCtrl, 0, wx.ALL, 5 )
		
		self.m_staticText86 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Ounces / Hr", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText86.Wrap( -1 )
		fgSizer14.Add( self.m_staticText86, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.ozPerHr_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_READONLY )
		self.ozPerHr_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer14.Add( self.ozPerHr_textCtrl, 0, wx.ALL, 5 )
		
		bSizer13.Add( fgSizer14, 0, 0, 5 )
		
		self.m_staticline17 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer13.Add( self.m_staticline17, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer171 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer171.SetFlexibleDirection( wx.BOTH )
		fgSizer171.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText51 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Estimated Refinement Recovery", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		fgSizer171.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.percentLoss_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, u"80", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		fgSizer171.Add( self.percentLoss_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText50 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"London Spot Price", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		fgSizer171.Add( self.m_staticText50, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.londonSpot_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		fgSizer171.Add( self.londonSpot_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText78 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Estimated Refinement Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText78.Wrap( -1 )
		fgSizer171.Add( self.m_staticText78, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.estTotal_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY )
		self.estTotal_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer171.Add( self.estTotal_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer13.Add( fgSizer171, 0, 0, 5 )
		
		self.bSizerX.Add( bSizer13, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline12 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizerX.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText64 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Dredge Owner", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText64.Wrap( -1 )
		self.m_staticText64.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		self.bSizerX.Add( self.m_staticText64, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer181 = wx.FlexGridSizer( 2, 8, 0, 0 )
		fgSizer181.SetFlexibleDirection( wx.BOTH )
		fgSizer181.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.ownerGrams_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Grams", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ownerGrams_staticText.Wrap( -1 )
		fgSizer181.Add( self.ownerGrams_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.ownerGrams_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_READONLY )
		self.ownerGrams_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer181.Add( self.ownerGrams_textCtrl, 0, wx.ALL, 5 )
		
		self.m_staticline28 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		fgSizer181.Add( self.m_staticline28, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.ownerEstValue_staticText1 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Estimated Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ownerEstValue_staticText1.Wrap( -1 )
		fgSizer181.Add( self.ownerEstValue_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.ownerEstimate_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY )
		self.ownerEstimate_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer181.Add( self.ownerEstimate_textCtrl, 0, wx.ALL, 5 )
		
		self.bSizerX.Add( fgSizer181, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.diver_staticline2 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizerX.Add( self.diver_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.extraDiver_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Diver Distribution", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.extraDiver_staticText.Wrap( -1 )
		self.extraDiver_staticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		self.bSizerX.Add( self.extraDiver_staticText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.extraDiving_fgSizer = wx.FlexGridSizer( 99, 5, 0, 0 )
		self.extraDiving_fgSizer.SetFlexibleDirection( wx.BOTH )
		self.extraDiving_fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.exName_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exName_staticText.Wrap( -1 )
		self.extraDiving_fgSizer.Add( self.exName_staticText, 0, wx.ALL, 5 )
		
		self.exHours_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Hours", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exHours_staticText.Wrap( -1 )
		self.extraDiving_fgSizer.Add( self.exHours_staticText, 0, wx.ALL, 5 )
		
		self.exPay_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Pay Rate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exPay_staticText.Wrap( -1 )
		self.extraDiving_fgSizer.Add( self.exPay_staticText, 0, wx.ALL, 5 )
		
		self.exGrams_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Grams", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exGrams_staticText.Wrap( -1 )
		self.extraDiving_fgSizer.Add( self.exGrams_staticText, 0, wx.ALL, 5 )
		
		self.exValue_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Estimated Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exValue_staticText.Wrap( -1 )
		self.extraDiving_fgSizer.Add( self.exValue_staticText, 0, wx.ALL, 5 )
		
		self.bSizerX.Add( self.extraDiving_fgSizer, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.scrollwindow.SetSizer( self.bSizerX )
		self.scrollwindow.Layout()
		self.bSizerX.Fit( self.scrollwindow )
		self.bSizer.Add( self.scrollwindow, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline26 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizer.Add( self.m_staticline26, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer17 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer17.SetFlexibleDirection( wx.BOTH )
		fgSizer17.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.save_button = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.save_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.printview_button = wx.Button( self, wx.ID_ANY, u"Print View", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.printview_button, 0, wx.ALL, 5 )
		
		self.cancel_button = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.cancel_button, 0, wx.ALL, 5 )
		
		self.bSizer.Add( fgSizer17, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( self.bSizer )
		self.Layout()
		self.bSizer.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self._evtClose )
		self.Bind( wx.EVT_INIT_DIALOG, self._evtInit )
		self.round_choice.Bind( wx.EVT_CHOICE, self._evtRoundChange )
		self.totalGrams_textCtrl.Bind( wx.EVT_KEY_UP, self._evtGramsChange )
		self.totalGrams_textCtrl.Bind( wx.EVT_KILL_FOCUS, self._evtSetGrams )
		self.totalOz_textCtrl.Bind( wx.EVT_KEY_UP, self._evtTozChange )
		self.totalOz_textCtrl.Bind( wx.EVT_KILL_FOCUS, self._evtSetTroyOz )
		self.percentLoss_textCtrl.Bind( wx.EVT_TEXT, self._evtPctLossChange )
		self.londonSpot_textCtrl.Bind( wx.EVT_TEXT, self._evtLondonSpotChange )
		self.save_button.Bind( wx.EVT_BUTTON, self._evtSave )
		self.printview_button.Bind( wx.EVT_BUTTON, self._evtPrintView )
		self.cancel_button.Bind( wx.EVT_BUTTON, self._evtClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtClose( self, event ):
		event.Skip()
	
	def _evtInit( self, event ):
		event.Skip()
	
	def _evtRoundChange( self, event ):
		event.Skip()
	
	def _evtGramsChange( self, event ):
		event.Skip()
	
	def _evtSetGrams( self, event ):
		event.Skip()
	
	def _evtTozChange( self, event ):
		event.Skip()
	
	def _evtSetTroyOz( self, event ):
		event.Skip()
	
	def _evtPctLossChange( self, event ):
		event.Skip()
	
	def _evtLondonSpotChange( self, event ):
		event.Skip()
	
	def _evtSave( self, event ):
		event.Skip()
	
	def _evtPrintView( self, event ):
		event.Skip()
	
	

###########################################################################
## Class SeasonReport
###########################################################################

class SeasonReport ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Season Report", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, u"Season Report", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText44.Wrap( -1 )
		self.m_staticText44.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		
		self.bSizer.Add( self.m_staticText44, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline14 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizer.Add( self.m_staticline14, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.scrollwindow = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.scrollwindow.SetScrollRate( 5, 5 )
		self.bSizerX = wx.BoxSizer( wx.VERTICAL )
		
		self.dateRange_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Jan, 00 to Jan, 00 2000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dateRange_staticText.Wrap( -1 )
		self.bSizerX.Add( self.dateRange_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline13 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizerX.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer14 = wx.FlexGridSizer( 4, 2, 0, 0 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText42 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Total Dive Hours", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		fgSizer14.Add( self.m_staticText42, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.totalHours_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_READONLY )
		self.totalHours_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer14.Add( self.totalHours_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText43 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Total Grams", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )
		fgSizer14.Add( self.m_staticText43, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.totalGrams_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_READONLY )
		self.totalGrams_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer14.Add( self.totalGrams_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText71 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Total Troy Ounces", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		fgSizer14.Add( self.m_staticText71, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.totalOz_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_READONLY )
		self.totalOz_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer14.Add( self.totalOz_textCtrl, 0, wx.ALL, 5 )
		
		self.m_staticText86 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Avg. Ounces / Hr", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText86.Wrap( -1 )
		fgSizer14.Add( self.m_staticText86, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.ozPerHr_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_READONLY )
		self.ozPerHr_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer14.Add( self.ozPerHr_textCtrl, 0, wx.ALL, 5 )
		
		bSizer13.Add( fgSizer14, 0, 0, 5 )
		
		self.m_staticline17 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer13.Add( self.m_staticline17, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer171 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer171.SetFlexibleDirection( wx.BOTH )
		fgSizer171.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText51 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Estimated Refinement Recovery", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		fgSizer171.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.percentLoss_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, u"80", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		fgSizer171.Add( self.percentLoss_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText50 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"London Spot Price", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		fgSizer171.Add( self.m_staticText50, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.londonSpot_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		fgSizer171.Add( self.londonSpot_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText78 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Estimated Refinement Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText78.Wrap( -1 )
		fgSizer171.Add( self.m_staticText78, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.estTotal_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY )
		self.estTotal_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer171.Add( self.estTotal_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer13.Add( fgSizer171, 0, 0, 5 )
		
		self.bSizerX.Add( bSizer13, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline12 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizerX.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText64 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Dredge Owner", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText64.Wrap( -1 )
		self.m_staticText64.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		self.bSizerX.Add( self.m_staticText64, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer18 = wx.FlexGridSizer( 1, 8, 0, 0 )
		fgSizer18.SetFlexibleDirection( wx.BOTH )
		fgSizer18.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.remainder_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Gross Grams", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.remainder_staticText.Wrap( -1 )
		fgSizer18.Add( self.remainder_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.ownerGrams_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_READONLY )
		self.ownerGrams_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer18.Add( self.ownerGrams_textCtrl, 0, wx.ALL, 5 )
		
		self.m_staticline19 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		fgSizer18.Add( self.m_staticline19, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText612 = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Estimated Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText612.Wrap( -1 )
		fgSizer18.Add( self.m_staticText612, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.ownerEstimate_textCtrl = wx.TextCtrl( self.scrollwindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY )
		self.ownerEstimate_textCtrl.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
		
		fgSizer18.Add( self.ownerEstimate_textCtrl, 0, wx.ALL, 5 )
		
		self.bSizerX.Add( fgSizer18, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline15 = wx.StaticLine( self.scrollwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizerX.Add( self.m_staticline15, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.extraDiver_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Diver Distribution", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.extraDiver_staticText.Wrap( -1 )
		self.extraDiver_staticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		self.bSizerX.Add( self.extraDiver_staticText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.extraDiving_fgSizer = wx.FlexGridSizer( 99, 5, 0, 0 )
		self.extraDiving_fgSizer.SetFlexibleDirection( wx.BOTH )
		self.extraDiving_fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.exName_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exName_staticText.Wrap( -1 )
		self.extraDiving_fgSizer.Add( self.exName_staticText, 0, wx.ALL, 5 )
		
		self.exHours_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Hours", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exHours_staticText.Wrap( -1 )
		self.extraDiving_fgSizer.Add( self.exHours_staticText, 0, wx.ALL, 5 )
		
		self.exGrams_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Grams", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exGrams_staticText.Wrap( -1 )
		self.extraDiving_fgSizer.Add( self.exGrams_staticText, 0, wx.ALL, 5 )
		
		self.exOz_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Troy Oz.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exOz_staticText.Wrap( -1 )
		self.extraDiving_fgSizer.Add( self.exOz_staticText, 0, wx.ALL, 5 )
		
		self.exValue_staticText = wx.StaticText( self.scrollwindow, wx.ID_ANY, u"Estimated Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exValue_staticText.Wrap( -1 )
		self.extraDiving_fgSizer.Add( self.exValue_staticText, 0, wx.ALL, 5 )
		
		self.bSizerX.Add( self.extraDiving_fgSizer, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.scrollwindow.SetSizer( self.bSizerX )
		self.scrollwindow.Layout()
		self.bSizerX.Fit( self.scrollwindow )
		self.bSizer.Add( self.scrollwindow, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline26 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.bSizer.Add( self.m_staticline26, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer17 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer17.SetFlexibleDirection( wx.BOTH )
		fgSizer17.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.printview_button = wx.Button( self, wx.ID_ANY, u"Print View", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.printview_button, 0, wx.ALL, 5 )
		
		self.cancel_button = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.cancel_button, 0, wx.ALL, 5 )
		
		self.bSizer.Add( fgSizer17, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( self.bSizer )
		self.Layout()
		self.bSizer.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self._evtClose )
		self.Bind( wx.EVT_INIT_DIALOG, self._evtInit )
		self.totalGrams_textCtrl.Bind( wx.EVT_KILL_FOCUS, self._evtSetGrams )
		self.totalOz_textCtrl.Bind( wx.EVT_KILL_FOCUS, self._evtSetTroyOz )
		self.percentLoss_textCtrl.Bind( wx.EVT_TEXT, self._evtLondonSpotChange )
		self.londonSpot_textCtrl.Bind( wx.EVT_TEXT, self._evtLondonSpotChange )
		self.printview_button.Bind( wx.EVT_BUTTON, self._evtPrintView )
		self.cancel_button.Bind( wx.EVT_BUTTON, self._evtClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtClose( self, event ):
		event.Skip()
	
	def _evtInit( self, event ):
		event.Skip()
	
	def _evtSetGrams( self, event ):
		event.Skip()
	
	def _evtSetTroyOz( self, event ):
		event.Skip()
	
	def _evtLondonSpotChange( self, event ):
		event.Skip()
	
	
	def _evtPrintView( self, event ):
		event.Skip()
	
	

###########################################################################
## Class VesselSelect
###########################################################################

class VesselSelect ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Vessel", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText135 = wx.StaticText( self, wx.ID_ANY, u"Select Vessel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText135.Wrap( -1 )
		bSizer24.Add( self.m_staticText135, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		vessel_choiceChoices = [ u"Norpac", u"Tahta", u"Julianna" ]
		self.vessel_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, vessel_choiceChoices, 0 )
		self.vessel_choice.SetSelection( 2 )
		bSizer24.Add( self.vessel_choice, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline49 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer24.Add( self.m_staticline49, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.ok_button = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.ok_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( bSizer24 )
		self.Layout()
		bSizer24.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self._evtOK )
		self.Bind( wx.EVT_INIT_DIALOG, self._evtInit )
		self.ok_button.Bind( wx.EVT_BUTTON, self._evtOK )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtOK( self, event ):
		event.Skip()
	
	def _evtInit( self, event ):
		event.Skip()
	
	

