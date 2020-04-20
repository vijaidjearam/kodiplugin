import urllib2, urllib, xbmcgui, xbmcplugin,xbmcaddon, xbmc, re, sys, os, requests
from t0mm0.common.addon import Addon
addonId        = 'plugin.video.vijai'
addon_settings = xbmcaddon.Addon(id = addonId);
addon          = Addon( addonId, sys.argv )
addonPath      = xbmc.translatePath( addon.get_path() )
resPath        = os.path.join( addonPath, 'resources' )
iconPath       = os.path.join( resPath, 'images' )
def getImgPath( icon ):
    icon = icon + '.png'
    imgPath = os.path.join( iconPath, icon )
   # print imgPath
    if os.path.exists( imgPath ):
        return imgPath
    else:
        return ''