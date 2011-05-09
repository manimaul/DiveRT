#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Copyright (C) 2010 by Will Kamp <manimaul!gmail.com>

#C:\path\to\src>python buildWin.py build

from cx_Freeze import setup, Executable
import sys, os, shutil

#python setup.py build
debug = "Console"
release = "Win32GUI"

if sys.platform == 'win32':
    exe = Executable('DiveRT.py', base=release, icon='icons/DiveRT.ico')
 
#buildOptions = dict(compressed = True, path = sys.path + ["rc", "icon"])
buildOptions = dict(compressed = True)

 
setup(name='DiveRT', 
        version  = '1.0', 
        author = 'Will Kamp', 
        author_email = 'manimaul@gmail.com', 
        url = 'http://matrixmariner.com',
        description = 'Dive Recover Tracker',
        zip_safe = True,
        options = dict(build_exe = buildOptions),
        executables = [exe]
      )

from distutils.dir_util import copy_tree
copy_tree('.//icons', './/build//exe.win32-2.7//icons')
shutil.copy2('DiveRT_Template.sql', 'build//exe.win32-2.7')
shutil.copy2('license.txt', 'build//exe.win32-2.7')
shutil.copy2('installer.nsi', 'build')