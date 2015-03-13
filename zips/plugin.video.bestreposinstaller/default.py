#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,urllib
import xbmcaddon,xbmcplugin,xbmcgui
import orphAddon
import repoCheck

Config = xbmcaddon.Addon()
dialog = xbmcgui.Dialog()

Progress = xbmcgui.DialogProgress()

Config.openSettings()


repoCheck.DocRepo()


if Config.getSetting("anon") == 'true' or Config.getSetting("bromix") == 'true' or Config.getSetting("iwf") == 'true' or Config.getSetting("kinkin") == 'true' or Config.getSetting("lambda") == 'true' or Config.getSetting("metal") == 'true' or Config.getSetting("pulsar") == 'true' or Config.getSetting("enen") == 'true' or Config.getSetting("shani") == 'true' or Config.getSetting("highway") == 'true' or Config.getSetting("theyid") == 'true' or Config.getSetting("tknorris") == 'true' or Config.getSetting("total") == 'true' or Config.getSetting("tvaddons") == 'true' or Config.getSetting("israeli") == 'true' or Config.getSetting("xunity") == 'true':
    
    dialog.ok('BEST REPOS INSTALLER', 'Se instalarán los repositorios que has seleccionado.', '', 'Por favor, espera a que el proceso de instalación acabe.')
    Progress.create("Instalando..", "Descargando repositorios...")
    Progress.update(0)
    if Progress.iscanceled() == True:
        sys.exit()
    
    if Config.getSetting("anon") == 'true':
        repoCheck.Anon()
        Progress.update(6)
    else: pass
    
    if Config.getSetting("bromix") == 'true':
        repoCheck.Bromix()
        Progress.update(12)
    else: pass
    
    if Config.getSetting("iwf") == 'true':
        repoCheck.Iwf()
        print "yes yes tes"
        Progress.update(18)
    else: pass
    
    if Config.getSetting("kinkin") == 'true':
        repoCheck.Kinkin()
        Progress.update(24)
    else: pass
    
    if Config.getSetting("lambda") == 'true':
        repoCheck.Lambda()
        Progress.update(30)
    else: pass
    
    if Config.getSetting("metal") == 'true':
        repoCheck.Metal()
        Progress.update(36)
    else: pass
    
    if Config.getSetting("pulsar") == 'true':
        repoCheck.Pulsar()
        Progress.update(42)
    else: pass
    
    if Config.getSetting("enen") == 'true':
        repoCheck.Enen()
        Progress.update(48)
    else: pass
    
    if Config.getSetting("shani") == 'true':
        repoCheck.Shani()
        Progress.update(54)
    else: pass
    
    if Config.getSetting("highway") == 'true':
        repoCheck.Highway()
        Progress.update(60)
    else: pass
    
    if Config.getSetting("theyid") == 'true':
        repoCheck.Theyid()
        Progress.update(66)
    else: pass
    
    if Config.getSetting("tknorris") == 'true':
        repoCheck.Tknorris()
        Progress.update(72)
    else: pass
    
    if Config.getSetting("total") == 'true':
        repoCheck.Total()
        Progress.update(78)
    else: pass
    
    if Config.getSetting("tvaddons") == 'true':
        repoCheck.Tvaddons()
        Progress.update(84)
    else: pass
    
    if Config.getSetting("israeli") == 'true':
        repoCheck.Israeli()
        Progress.update(90)
    else: pass
    
    if Config.getSetting("xunity") == 'true':
        repoCheck.Xunity()
        Progress.update(96)
    else: pass
        
    Progress.update(100)
    dialog.ok('HECHO!', 'Repositorios instalados.')
    
else: pass


if Config.getSetting("latino") == 'true' or Config.getSetting("pelisalacarta") == 'true' or Config.getSetting("tvalacarta") == 'true' or Config.getSetting("kmedia") == 'true' or Config.getSetting("mashup") == 'true' or Config.getSetting("bbc") == 'true':

    dialog.ok('BEST REPOS INSTALLER', 'Se instalarán los add-ons que has seleccionado.', '', 'Por favor, espera a que el proceso de instalación acabe.')
    Progress.create("Instalando..", "Descargando add-ons...")
    Progress.update(0)

    if Config.getSetting("latino") == 'true':
        orphAddon.Latino()
        Progress.update(12)
    else: pass
    if Config.getSetting("pelisalacarta") == 'true':
        orphAddon.Pelisalacarta()
        Progress.update(25)
    else: pass
    if Config.getSetting("tvalacarta") == 'true':
        orphAddon.TValacarta()
        Progress.update(38)
    else: pass
    if Config.getSetting("kmedia") == 'true':
        Progress.update(38, 'KMediaTorrent puede tardar mucho, NO CANCELES!')
        orphAddon.Kmedia()
        Progress.update(55, 'Descargando add-ons...')
    else: pass
    if Config.getSetting("mashup") == 'true':
        orphAddon.Mashup()
        Progress.update(70)
    else: pass
    if Config.getSetting("bbc") == 'true':
        orphAddon.BBC()
        Progress.update(85)
    else: pass
    
    Progress.update(100)
    dialog.ok('HECHO!', 'Add-ons instalados.')

else: pass



sys.exit()

