;-------------------------------------------------------------------------
; Installer script for DiveRT
;-------------------------------------------------------------------------

;--------------------------------------------
; General definitions: just some constants that are referred later.
!define PRODUCT_NAME "Dive RT"
!define PRODUCT_VERSION_MAJOR 2
!define PRODUCT_VERSION_MINOR 0
!define PRODUCT_DISPLAY_VERSION "2.0"
!define PRODUCT_PUBLISHER "Will Kamp"
!define PRODUCT_WEB_SITE "http://blog.matrixmariner.com"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}" ; 
!define PRODUCT_UNINST_ROOT_KEY "HKLM"
!define PRODUCT_INSTALL_DIR "$PROGRAMFILES\DiveRT"

;--------------------------------------------
; Maximum compression
SetCompressor /SOLID lzma

;--------------------------------------------
; Modern UI definitions
!include "MUI2.nsh"

;--------------------------------
;Interface Settings
!define MUI_ABORTWARNING
!define MUI_ICON "exe.win32-2.7\icons\DiveRT.ico"
!define MUI_UNICON "exe.win32-2.7\icons\DiveRT.ico"
!define MUI_HEADERIMAGE
!define MUI_HEADERIMAGE_BITMAP "exe.win32-2.7\icons\MUI_HEADERIMAGE_BITMAP.bmp"
;MUI_HEADERIMAGE_BITMAP recommended size is 150x57
!define MUI_HEADERIMAGE_RIGHT
!define MUI_HEADER_TRANSPARENT_TEXT
!define MUI_WELCOMEFINISHPAGE_BITMAP "exe.win32-2.7\icons\MUI_WELCOMEFINISHPAGE_BITMAP.bmp"
;MUI_WELCOMEFINISHPAGE_BITMAP recommended size is 164x314 
!define MUI_WELCOMEFINISHPAGE_BITMAP_NOSTRETCH 

;--------------------------------
;Pages

; Welcome page
!insertmacro MUI_PAGE_WELCOME

; License page
!define MUI_LICENSEPAGE_CHECKBOX
!insertmacro MUI_PAGE_LICENSE "exe.win32-2.7\license.txt"

; Instfiles page
!insertmacro MUI_PAGE_INSTFILES

; Finish page
!define MUI_FINISHPAGE_SHOWREADME "$INSTDIR\license.txt"
!define MUI_FINISHPAGE_NOREBOOTSUPPORT
!insertmacro MUI_PAGE_FINISH

; Uninstaller pages
!insertmacro MUI_UNPAGE_INSTFILES

; Language files
!insertmacro MUI_LANGUAGE "English"

;--------------------------------------------
; Installer Settings
Name "${PRODUCT_NAME}"
OutFile "${PRODUCT_NAME} Setup.exe"
InstallDir "${PRODUCT_INSTALL_DIR}"
ShowInstDetails show
ShowUnInstDetails show
BrandingText "${PRODUCT_PUBLISHER}"
RequestExecutionLevel admin ;Request application privileges for Windows Vista/7

;--------------------------------
;Installer Sections

Section "MainSection" MainSection

  SetOutPath "$INSTDIR"
  SetOverwrite ifnewer
  
  ;Copy files
  File /r "exe.win32-2.7\*"

  SetShellVarcontext all
  CreateDirectory "$APPDATA\DiveRT"
  CopyFiles "$INSTDIR\icons\DiveRT.ico" "$APPDATA\DiveRT"
  CreateShortCut "$INSTDIR\DiveRT.lnk" "$INSTDIR\DiveRT.exe" "" \
  "$APPDATA\DiveRT\DiveRT.ico" "" SW_SHOWNORMAL "" "Dive Recover Tracker"

  CreateDirectory "$SMPROGRAMS\DiveRT"
  CopyFiles "$INSTDIR\DiveRT.lnk" "$SMPROGRAMS\DiveRT"

  WriteUninstaller "$INSTDIR\Uninstall.exe"
  CreateShortCut "$INSTDIR\Uninstall.lnk" "$INSTDIR\Uninstall.exe" "" \
  "$INSTDIR\Uninstall.exe" "" SW_SHOWNORMAL "" "Uninstall Dive Recover Tracker"
  CopyFiles "$INSTDIR\Uninstall.lnk" "$SMPROGRAMS\DiveRT"

  SetShellVarContext current
  CopyFiles "$INSTDIR\DiveRT.lnk" "$DESKTOP"
  
  ;Create Start Menu folders and shortcuts.
  ;CreateDirectory "$STARTMENU\Programs\${PRODUCT_NAME}"
  ;CreateShortCut "$STARTMENU\Programs\${PRODUCT_NAME}\${PRODUCT_NAME}.lnk" "$INSTDIR\SQLAnalyzer.exe"
  ;CreateShortCut "$STARTMENU\Programs\${PRODUCT_NAME}\README.lnk" "$INSTDIR\README.txt"
  ;CreateShortCut "$STARTMENU\Programs\${PRODUCT_NAME}\Sample.lnk" "$INSTDIR\sqlanalyzer.gif"
  ;CreateShortCut "$STARTMENU\Programs\${PRODUCT_NAME}\Uninstall.lnk" "$INSTDIR\Uninstall.exe"
  
  ;Create uninstaller
  ;WriteUninstaller "$INSTDIR\Uninstall.exe"

  ;Add/Remove registry settings: This registry entry will list the product in 'installed programs list'
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "${PRODUCT_NAME}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\Uninstall.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\\icons\DiveRT.ico"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_DISPLAY_VERSION}"
  WriteRegDWORD ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "VersionMajor" "${PRODUCT_VERSION_MAJOR}"
  WriteRegDWORD ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "VersionMinor" "${PRODUCT_VERSION_MINOR}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd

;--------------------------------
;Uninstaller Section

;When the uninstaller is launched, this function provides a confirmation message box.
Function un.onInit
	MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "Are you sure you want to completely remove ${PRODUCT_NAME} and all of its components?" IDYES +2
	Abort
FunctionEnd

;When the uninstallation is complete, this function displays a success message box.
Function un.onUninstSuccess
	HideWindow
	MessageBox MB_ICONINFORMATION|MB_OK "${PRODUCT_NAME} was successfully removed from your computer."
FunctionEnd

;This function gets executed when uninstaller is launched. It basically removes all installed files.
Section "Uninstall"

RMDir /r "$INSTDIR"
SetShellVarContext all
RMDir /r "$SMPROGRAMS\DiveRT"
RMDir /r "$APPDATA\DiveRT"
SetShellVarContext current
Delete "$DESKTOP\DiveRT.lnk"

  ;Unregister the OCX controls.
  ;Exec 'regsvr32 -u "$INSTDIR\RICHTX32.OCX" /S'
  ;Exec 'regsvr32 -u "$INSTDIR\COMDLG32.OCX" /S'
  ;Exec 'regsvr32 -u "$INSTDIR\MSFLXGRD.OCX" /S'

  ;Delete all the files
  ;Delete "$INSTDIR\sqlanalyzer.ico"
  ;Delete "$INSTDIR\SQLAnalyzer.exe"
  ;Delete "$INSTDIR\sqlanalyzer.gif"
  ;Delete "$INSTDIR\README.txt"
  ;Delete "$INSTDIR\RICHTX32.OCX"
  ;Delete "$INSTDIR\COMDLG32.OCX"
  ;Delete "$INSTDIR\MSFLXGRD.OCX"
  ;Delete "$INSTDIR\Uninstall.exe"

  ;Remove the installation folder.
  ;RMDir "$INSTDIR"
  
  ;Remove the Shortcuts
  ;Delete "$STARTMENU\Programs\${PRODUCT_NAME}\${PRODUCT_NAME}.lnk"
  ;Delete "$STARTMENU\Programs\${PRODUCT_NAME}\README.lnk"
  ;Delete "$STARTMENU\Programs\${PRODUCT_NAME}\Sample.lnk"
  ;Delete "$STARTMENU\Programs\${PRODUCT_NAME}\Uninstall.lnk"
  ;RMDir /r "$STARTMENU\Programs\${PRODUCT_NAME}"
  
  ;Remove the entry from 'installed programs list'
  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"

  ;SetAutoClose True ;This will close the uinstall window that shows the details of files deleted.
SectionEnd