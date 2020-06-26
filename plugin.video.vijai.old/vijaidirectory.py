import urllib2, urllib, xbmcgui, xbmcplugin,xbmcaddon, xbmc, re, sys, os, requests
from t0mm0.common.net import Net
from t0mm0.common.addon import Addon
from unpack import unpack
import resolveurl
addon_handle= int(sys.argv[1])
tamilgun_icon = "http://cdn.appstorm.net/mac.appstorm.net/files/2012/07/icon4.png"
net = Net()
addonId        = 'plugin.video.vijai'
addon_settings = xbmcaddon.Addon(id = addonId);
addon          = Addon( addonId, sys.argv )
addonPath      = xbmc.translatePath( addon.get_path() )
resPath        = os.path.join( addonPath, 'resources' )
iconPath       = os.path.join( resPath, 'images' )
def addDir (dir_type,mode,url,name,iconimage,fanart):
    base_url = sys.argv[0]
    base_url +="?url=" +urllib.quote_plus(url)
    base_url += "&mode=" +str(mode)
    base_url +="&name=" +urllib.quote_plus(name)
    base_url +="&icoimage=" +urllib.quote_plus(iconimage)
    base_url +="&fanart=" +urllib.quote_plus(fanart)
    li = xbmcgui.ListItem(name,iconImage=iconimage)
    li.setInfo(type="Video",infoLabels={"Title": name})
    li.setProperty("Fanart_Image", fanart)
    if dir_type != '':
        link = xbmcplugin.addDirectoryItem(handle=addon_handle,url=base_url,listitem=li,isFolder=True)
    else:
        link = xbmcplugin.addDirectoryItem(handle=addon_handle,url=url,listitem=li,isFolder=False)
    return link