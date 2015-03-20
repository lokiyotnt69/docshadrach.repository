# -*- coding: utf-8 -*-
import os, urllib, xbmc, zipfile

def ExtractAll(_in, _out):
	try:
		zin = zipfile.ZipFile(_in, 'r')
		zin.extractall(_out)
	except Exception, e:
		print str(e)
		return False

	return True
	
	
def Latino():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'plugin.video.latinototal')):
		return
		
	url = "https://www.dropbox.com/s/j7u4m8k0o56g309/plugin.video.latinototal-0.2.0.zip?dl=1"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")
	
	
def Pelisalacarta():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'plugin.video.pelisalacarta')):
		return
		
	url = "http://blog.tvalacarta.info/descargas/pelisalacarta-xbmc-addon-gotham-3.9.99.zip"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")
	
	
def TValacarta():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'plugin.video.tvalacarta')):
		return
		
	url = "http://blog.tvalacarta.info/descargas/tvalacarta-xbmc-addon-gotham-3.3.21.zip"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")
	
	
def Kmedia():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'plugin.video.kmediatorrent-2.3.3')):
		return
		
	url = "https://github.com/jmarth/plugin.video.kmediatorrent/archive/v2.3.3.zip"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")
	
	
def Mashup():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'plugin.video.movie25')):
		return
		
	url = "https://github.com/Mafarricos/Mafarricos-modded-xbmc-addons/blob/master/repo/plugin.video.movie25/plugin.video.movie25-1.4.2.zip?raw=true"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")
	
	
def Streamnation():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'plugin.video.streamnation')):
		return
		
	url = "https://www.dropbox.com/s/xxvn5md2yczsb3e/plugin.video.streamnation-0.7.2.zip?dl=1"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")
	
	
def BBC():
	if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'service.bbclivefootballscores')):
		return
		
	url = "https://github.com/elParaguayo/service.bbclivefootballscores/releases/download/v0.3.0RC/service.bbclivefootballscores.v0.3.0rc.zip"
	addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
	packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
	
	urllib.urlretrieve(url, packageFile)
	ExtractAll(packageFile, addonsDir)
		
	try:
		os.remove(packageFile)
	except:
		pass
			
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")
	

	




