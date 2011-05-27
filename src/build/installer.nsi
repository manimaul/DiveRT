!include "MUI2.nsh"
!include "WinMessages.nsh"

Name "Dive Recover Tracker"
OutFile "DiveRT_1.02_Setup.exe"
InstallDir $PROGRAMFILES32\DiveRT

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "exe.win32-2.7\license.txt"
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH

!insertmacro MUI_LANGUAGE "English"

Section "Dive Recover Tracker"

SetOutPath "$INSTDIR\DiveRT"
File /r "exe.win32-2.7\*"

SetShellVarcontext all
CreateDirectory "$APPDATA\DiveRT"
CopyFiles "$INSTDIR\DiveRT\icons\DiveRT.ico" "$APPDATA\DiveRT"
CreateShortCut "$INSTDIR\DiveRT\DiveRT.lnk" "$INSTDIR\DiveRT\DiveRT.exe" "" \
"$APPDATA\DiveRT\DiveRT.ico" "" SW_SHOWNORMAL "" "Dive Recover Tracker"

CreateDirectory "$SMPROGRAMS\DiveRT"
CopyFiles "$INSTDIR\DiveRT\DiveRT.lnk" "$SMPROGRAMS\DiveRT"

WriteUninstaller "$INSTDIR\Uninstall.exe"
CreateShortCut "$INSTDIR\DiveRT\Uninstall.lnk" "$INSTDIR\Uninstall.exe" "" \
"$INSTDIR\Uninstall.exe" "" SW_SHOWNORMAL "" "Uninstall Dive Recover Tracker"
CopyFiles "$INSTDIR\DiveRT\Uninstall.lnk" "$SMPROGRAMS\DiveRT"

SetShellVarContext current
CopyFiles "$INSTDIR\DiveRT\DiveRT.lnk" "$DESKTOP"

SectionEnd

Section "Uninstall"

RMDir /r "$INSTDIR"
SetShellVarContext all
RMDir /r "$SMPROGRAMS\DiveRT"
RMDir /r "$APPDATA\DiveRT"
SetShellVarContext current
Delete "$DESKTOP\DiveRT.lnk"

SectionEnd
