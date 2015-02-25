#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,urllib
import xbmcaddon,xbmcplugin,xbmcgui
import repoCheck

Config = xbmcaddon.Addon()
dialog = xbmcgui.Dialog()

Progress = xbmcgui.DialogProgress()

Config.openSettings()


dialog.ok('BEST REPOS INSTALLER', 'Por favor, espera a que el proceso de instalación acabe.')

repoCheck.DocRepo()

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

if Config.getSetting("kinkin") == 'true':
    repoCheck.Kinkin()
    Progress.update(18)
else: pass

if Config.getSetting("lambda") == 'true':
    repoCheck.Lambda()
    Progress.update(24)
else: pass

if Config.getSetting("metal") == 'true':
    repoCheck.Metal()
    Progress.update(30)
else: pass

if Config.getSetting("pulsar") == 'true':
    repoCheck.Pulsar()
    Progress.update(36)
else: pass

if Config.getSetting("enen") == 'true':
    repoCheck.Enen()
    Progress.update(42)
else: pass

if Config.getSetting("shani") == 'true':
    repoCheck.Shani()
    Progress.update(48)
else: pass

if Config.getSetting("highway") == 'true':
    repoCheck.Highway()
    Progress.update(54)
else: pass

if Config.getSetting("theyid") == 'true':
    repoCheck.Theyid()
    Progress.update(60)
else: pass

if Config.getSetting("tknorris") == 'true':
    repoCheck.Tknorris()
    Progress.update(66)
else: pass

if Config.getSetting("tknorrisb") == 'true':
    repoCheck.Tknorrisb()
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



sys.exit()

