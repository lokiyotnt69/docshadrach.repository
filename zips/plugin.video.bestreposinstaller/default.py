#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,urllib
import xbmcaddon,xbmcplugin,xbmcgui
import repoCheck

Config = xbmcaddon.Addon()
dialog = xbmcgui.Dialog()

Config.openSettings()


dialog.ok('BEST REPO INSTALLER', 'Por favor, espera a que el proceso de instalación acabe.')

repoCheck.DocRepo()



if Config.getSetting("bromix") == 'true':
    repoCheck.Bromix()
else: pass

if Config.getSetting("kinkin") == 'true':
    repoCheck.Kinkin()
else: pass

if Config.getSetting("lambda") == 'true':
    repoCheck.Lambda()
else: pass

if Config.getSetting("metal") == 'true':
    repoCheck.Metal()
else: pass

if Config.getSetting("pulsar") == 'true':
    repoCheck.Pulsar()
else: pass

if Config.getSetting("enen") == 'true':
    repoCheck.Enen()
else: pass

if Config.getSetting("shani") == 'true':
    repoCheck.Shani()
else: pass

if Config.getSetting("highway") == 'true':
    repoCheck.Highway()
else: pass

if Config.getSetting("theyid") == 'true':
    repoCheck.Theyid()
else: pass

if Config.getSetting("tknorris") == 'true':
    repoCheck.Tknorris()
else: pass

if Config.getSetting("total") == 'true':
    repoCheck.Total()
else: pass

if Config.getSetting("tvaddons") == 'true':
    repoCheck.Tvaddons()
else: pass

if Config.getSetting("israeli") == 'true':
    repoCheck.Israeli()
else: pass

if Config.getSetting("xunity") == 'true':
    repoCheck.Xunity()
else: pass
    


dialog.ok('HECHO!', 'Repositorios instalados.')



sys.exit()

