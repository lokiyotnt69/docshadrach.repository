#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import xbmcaddon,xbmcplugin,xbmcgui
import shutil


Config = xbmcaddon.Addon()

dialog = xbmcgui.Dialog()

addondir = os.path.join(xbmcaddon.Addon().getAddonInfo('path'))
addonsdir = str(addondir).replace("mod","")



if os.path.isdir(addonsdir) == True and Config.getSetting("state") != "done":
    try:
        shutil.copytree(addondir + "\\mods\\", addonsdir + "\\resources\\site-packages\\xbmctorrent\\scrapers\\mods\\")
    except:
        pass
    shutil.copy(addonsdir + "\\resources\\site-packages\\xbmctorrent\\scrapers\\mods\\index_mod.py", addonsdir + "\\resources\\site-packages\\xbmctorrent\\index.py")
    Config.setSetting("state","done")
    dialog.ok("DONE", "Now you have modified scrapers!")
elif os.path.isdir(addonsdir) == True and Config.getSetting("state") == "done":
    shutil.copy(addonsdir + "\\resources\\site-packages\\xbmctorrent\\scrapers\\mods\\index.py", addonsdir + "\\resources\\site-packages\\xbmctorrent\\index.py")
    Config.setSetting("state","")
    dialog.ok("DONE", "REVERTED.")
else:
    dialog.ok("ERROR", "Looks like you have not XBMCtorrent.")
    sys.exit()