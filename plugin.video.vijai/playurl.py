import urllib2, urllib, xbmcgui, xbmcplugin,xbmcaddon, xbmc, re, sys, os, requests, resolveurl
from vijaicontent import addDir
from getImgPath import getImgPath
def playurl():
    args = sys.argv[2]
    xbmc.log("-------------------------------tesing vijai---------------------------------------------------------------")
    xbmc.log(args)
    mode = args.split('url=')
    mode = mode[1]
    mode = mode.split('&')
    url = mode[0]
    url = urllib.unquote_plus(url)
    try:
        xbmc.log(url)
        movieurl = resolveurl.HostedMediaFile(url)
        movieurl = movieurl.resolve()
        addDir('','',movieurl,"Click to play the link",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    except:
        xbmcgui.Dialog().ok('XBMC', 'Unable to locate video')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
