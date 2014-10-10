#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,urllib
import xbmcaddon,xbmcplugin,xbmcgui

Config = xbmcaddon.Addon()
dialog = xbmcgui.Dialog()



kb = xbmc.Keyboard('','Ingrese su Magnet Link',False)
kb.doModal()

if (kb.isConfirmed()):
    url = kb.getText()
else:
    sys.exit()
    
if str(url).startswith("magnet"):
    pass
elif url == "":
    dialog.ok('ERROR', 'Debe ingresar un Magnet Link.')
else:
    dialog.ok('ERROR', 'No es un Magnet Link válido.')

    
if str(url).startswith("magnet:"):
    url = urllib.quote_plus(url.encode("utf-8"))
else:
    pass


if Config.getSetting("engine") == '0':
    magnet = "plugin://plugin.video.xbmctorrent/play/" + str(url)
else:
    magnet = "plugin://plugin.video.pulsar/play?uri=" + str(url)


addondir = os.path.join(xbmcaddon.Addon().getAddonInfo('path'))
addonsdir = str(addondir).replace("plugin.video.magnetplayer","")

if os.path.isdir(addonsdir + "plugin.video.xbmctorrent") == True and os.path.isdir(addonsdir + "plugin.video.pulsar") == True:
    pass
elif os.path.isdir(addonsdir + "plugin.video.xbmctorrent") == False and os.path.isdir(addonsdir + "plugin.video.pulsar") == False:
    dialog.ok('ERROR', 'Para utilizar este add-on,', 'debes tener instalado XBMCtorrent o Pulsar.', 'TIP: Los puedes descargar desde mi repositorio. :)')
    sys.exit()
elif os.path.isdir(addonsdir + "plugin.video.xbmctorrent") == True and os.path.isdir(addonsdir + "plugin.video.pulsar") == False:
    Config.setSetting("engine", "0")
    magnet = "plugin://plugin.video.xbmctorrent/play/" + str(url)
elif os.path.isdir(addonsdir + "plugin.video.xbmctorrent") == False and os.path.isdir(addonsdir + "plugin.video.pulsar") == True:
    Config.setSetting("engine", "1")
    magnet = "plugin://plugin.video.pulsar/play?uri=" + str(url)



xbmc.Player().play(magnet)

sys.exit()

