#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib,urllib2,re,sys
import xbmcaddon,xbmcplugin,xbmcgui
import resolvers
from random import shuffle


Config = xbmcaddon.Addon()


def filestube(api, search, host, sort, days, page_n):
    page = 1
    base_url = 'http://api.filestube.com/?key=' + str(api) + '&phrase=' + str(search) + '&hosting=' + str(host) + str(days) + str(sort) + '&page='
    try:
        while page <= int(page_n):        
            url = base_url + str(page)
            req = urllib2.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
            response = urllib2.urlopen(req)
            link = response.read()
            response.close()
            match = re.compile('<name>.+?</name><extension>.+?</extension><size>.+?</size><description>.+?</description><link>(.+?)</link>').findall(link)
            for url in match:
                resp = urllib2.urlopen(url)
                titleandlink = resp.read()
                resp.close()
                rematch = re.compile('<a class="file-link-main" title="(.+?)" href="(.+?)"').findall(titleandlink)
                for title, direc_link in rematch:
                    if direc_link.startswith("http://allmyvideos.net/"):
                        url_direc = resolvers.allmyvideos(direc_link)
                        for reallink in url_direc:
                            addLink(title, reallink, 1, '')
                    elif direc_link.startswith("http://played.to/"):
                        url_direc = resolvers.played(direc_link)
                        for reallink in url_direc:
                            addLink(title, reallink, 1, '')
                    elif direc_link.startswith("http://www.vidspot.net/"):
                        url_direc = resolvers.vidspot(direc_link)
                        for reallink in url_direc:
                            addLink(title, reallink, 1, '')
                    elif direc_link.startswith("http://vodlocker.com/"):
                        url_direc = resolvers.vodlocker(direc_link)
                        for reallink in url_direc:
                            addLink(title, reallink, 1, '')                  
            page += 1
    except:
        pass


def addLink(name,url,mode,iconimage):
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)



def find_api():

    dialog = xbmcgui.Dialog()
    
    if Config.getSetting("pregunta_API") == 'true' and len(Config.getSetting("api_number")) == 32:
    	api = Config.getSetting("api_number")
    	return api
    elif Config.getSetting("pregunta_API") == 'true' and len(Config.getSetting("api_number")) != 32:  
        errorapi = dialog.ok('ERROR', 'La clave API que ha introducido no es correcta.')
    	if errorapi == True:
            Config.openSettings()
        else:
            sys.exit()
    else:
    	APIS = ["d8b8dce7af5b206d1381e146c7f4ed1a","56042019a766667ca5a49f4133cf3528","655282f0e3b71f6937bbfcd76eefab98","29ad4adea2119081ec51907e1cb6dfe8","7bd74e31d87641c402b7622de1a79e8a"]
    	shuffle(APIS)
    	api = APIS[0]
    	return api

api = find_api()


search_raw = Config.getSetting("search_query")
search = search_raw.replace(' ', '+')


def find_host():
    
	dialog = xbmcgui.Dialog()
        
	if Config.getSetting("played") == 'true':
		played = " 110"
	else:
		played = ""
		
	if Config.getSetting("allmyvideos") == 'true':
		allmyvideos = " 111"
	else:
		allmyvideos = ""
	
	if Config.getSetting("vidspot") == 'true':
		vidspot = " 112"
	else:
		vidspot = ""

	if Config.getSetting("vodlocker") == 'true':
		vodlocker = " 122"
	else:
		vodlocker = ""

	hosts = played + allmyvideos + vidspot + vodlocker
	whitespace = hosts.strip()
	host = whitespace.replace(' ', '%2C')
	
	if host == "":
		errorhost = dialog.ok('ERROR', 'Debe seleccionar al menos un Servidor de la lista.')
		if errorhost == True:
			Config.openSettings()
		else:
			sys.exit()
	else:
		return host

host = find_host()


if Config.getSetting("sort") == 'true':
	sort = "&sort=dd"
else:
	sort = ""


if Config.getSetting("anyday") == '0':
	days = ""
else:
	days = "&date=" + str(Config.getSetting("anyday"))
	

page_n = int(Config.getSetting("pages")) / 10


	
def run_addon(api, search, host, sort, days, page_n): 
    if search == "" or Config.getSetting("pregunta_search") == 'false':
        filestube(api, "hdrip", host, "", days, page_n)
    else:
        filestube(api, search, host, sort, days, page_n)


run_addon(api, search, host, sort, days, page_n)



xbmcplugin.endOfDirectory(int(sys.argv[1]))
