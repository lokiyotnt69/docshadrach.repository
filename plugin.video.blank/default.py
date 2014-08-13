
import os
import xbmcaddon, xbmcgui


file = os.path.join(xbmcaddon.Addon().getAddonInfo('path'),'LEER.txt')

dialog = xbmcgui.Dialog()

texto = str(file)

tupla = texto.partition("XBMC")


dialog.ok('Encuentra las instrucciones en:', str(tupla[0]), str(tupla[1]), str(tupla[2]))

sys.exit()

