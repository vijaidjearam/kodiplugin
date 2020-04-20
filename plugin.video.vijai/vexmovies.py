import urllib2, urllib, xbmcgui, xbmcplugin,xbmcaddon, xbmc, re, sys, os, requests
from t0mm0.common.net import Net
from t0mm0.common.addon import Addon
from unpack import unpack
from vijaicontent import getdatacontent,addDir,getImgPath
import resolveurl

def getstreamlinkname(url):
    temp = url.split(".")
    if 'www' in temp[0]: 
        link = temp[1]
        return link
    if 'www' not in temp[0]:
        link = temp[0]
        link = link.split("/")
        return link[-1]


def loadvexmovies(url):
    args = sys.argv[2]
    if str(sys.argv[2]).find('url=') > 1:
        args = sys.argv[2]
        mode = args.split('url=')
        xbmc.log(str(mode))
        mode = mode[1]
        mode = mode.split('&')
        url = mode[0]
        url = urllib.unquote_plus(url)
    #data = getdatacontent(url,"<a href=\"(?P<link>.*?)\" title=\"(?P<title>.*?)\">\s+<span class=\"affiche\">\s+<span class=\"(.*?)\"><\/span>\s*<img src=\"(?P<icon>.*?)\"")
    data = getdatacontent(url,"<a href=\"(.*?)\">\s+<div class=\"image\">\s+<img src=\"(.*?)\" alt=\"(.*?)\"")
    nav = getdatacontent(url,"<li class=\'dd\'><a class=\'current\'>\d+<\/a><\/li><li><a rel=\'nofollow\' class=\'page larger\' href=\'(.*?)\'>")
    for item in data:
        addDir('folder','playvexmovies',item[0],item[2],item[1],item[1])
    if nav:
        navlink = nav[0]
        addDir( 'folder','vexmovies',navlink,'[B]Next Page...[/B]',"https://lh3.googleusercontent.com/-NsVeHCUW0lo/V4b8r67FVSI/AAAAAAAAD7U/G1ifDqs0nFENPck0-oKCQgc3-Gdm_JM7QCCo/s574/next_574x358.png","https://lh3.googleusercontent.com/-NsVeHCUW0lo/V4b8r67FVSI/AAAAAAAAD7U/G1ifDqs0nFENPck0-oKCQgc3-Gdm_JM7QCCo/s574/next_574x358.png" )
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def playvexmovies():
    args = sys.argv[2]
    mode = args.split('url=')
    mode = mode[1]
    mode = mode.split('&')
    url = mode[0]
    url = urllib.unquote_plus(url)
    regex = "<(iframe|IFRAME) (src|SRC)=\"(.*?)\""
    iframe = getdatacontent(url,regex)
    iframe = iframe[0]
    for link in iframe:
        if "consistent" in link:
            url = link
            regex = "<player :title=\"{(.*W?)\"></player>"
            data= getdatacontent(url,regex)
            data = data[0]
            data = data.replace('&quot;','\"')
            data = data.replace('/','')
            regex = "\"src\":\"(.*?)\""
            data = re.compile(regex).findall(data)
            if data:
                for url in data:
                    if "dfcdn.net" in url:
                        xbmc.log("-----------------------------------------------playable url--------------------------------------------------------------------")
                        xbmc.log(url)
                        addDir('','',url.replace('&amp;','&'),"vexmovielink1",'','')
                    if "streamango" in url:
                        xbmc.log("-----------------------------------------------playable url--------------------------------------------------------------------")
                        xbmc.log(url)
                        url = url.split('\\')
                        xbmc.log("-----------------------------------------------playable url--------------------------------------------------------------------")
                        xbmc.log(str(url))
                        url = "https://streamango.com/embed/"+url[4]
                        addDir('folder','playurl',url,getstreamlinkname(url),getImgPath("openload_icon"),getImgPath("openload_fanart"))
                    if "openload" in url:
                        xbmc.log(url)
                        addDir('folder','playurl',url,getstreamlinkname(url),getImgPath("openload_icon"),getImgPath("openload_fanart"))
    xbmcplugin.endOfDirectory(int(sys.argv[1]))