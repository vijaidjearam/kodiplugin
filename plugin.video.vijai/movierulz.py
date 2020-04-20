import urllib2, urllib, xbmcgui, xbmcplugin,xbmcaddon, xbmc, re, sys, os, requests
from t0mm0.common.net import Net
from t0mm0.common.addon import Addon
from unpack import unpack
from vijaicontent import getdatacontent,addDir,getImgPath
import resolveurl
def loadmovierulz(url):
    args = sys.argv[2]
    if str(sys.argv[2]).find('url=') > 1:
        args = sys.argv[2]
        mode = args.split('url=')
        xbmc.log(str(mode))
        mode = mode[1]
        mode = mode.split('&')
        url = mode[0]
        url = urllib.unquote_plus(url)
    data = getdatacontent(url,"<a href=\"(.*?)\"\stitle=\"(.*?)\">\s*<img width=\"\d+\" height=\"\d+\" src=\"(.*?)\"")
    nav = getdatacontent(url,"<a href=\"(.*?)\">&larr;(\s|)Older Entries")
    nav =  nav[0]
    for item in data:
        addDir('folder','playMovierulz',item[0],item[1],item[2],item[2])
    if nav:
        addDir( 'folder','movierulz-telugu',nav[0],'[B]Next Page...[/B]',"https://lh3.googleusercontent.com/-NsVeHCUW0lo/V4b8r67FVSI/AAAAAAAAD7U/G1ifDqs0nFENPck0-oKCQgc3-Gdm_JM7QCCo/s574/next_574x358.png","https://lh3.googleusercontent.com/-NsVeHCUW0lo/V4b8r67FVSI/AAAAAAAAD7U/G1ifDqs0nFENPck0-oKCQgc3-Gdm_JM7QCCo/s574/next_574x358.png" )
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def playMovierulz():
    args = sys.argv[2]
    mode = args.split('url=')
    mode = mode[1]
    mode = mode.split('&')
    url = mode[0]
    url = urllib.unquote_plus(url)
    data= getdatacontent(url,"<p><strong>(.*?)<\/strong><br \/>\s+<a href=\"(.*?)\"")
    for item in data:
        if ("Openload" in item[0]):
            try:
                url = getdatacontent(item[1],"(?:iframe src|IFRAME SRC)=\"(.+?)\"")
                movieurl = url[0]
                if movieurl:
                    addDir('folder','playurl',movieurl,"openload",getImgPath("openload_icon"),getImgPath("openload_fanart"))
            except:
                xbmc.log("unable to fetch openload URL")      
        if ("Streamango" in item[0]):
            movieurl = item[1]
            if movieurl:
                addDir('folder','playurl',movieurl,"streamango",getImgPath("openload_icon"),getImgPath("openload_fanart"))
        if ("Netutv" in item[0]):
            xbmc.log("work in progress")
        if ("Oneload" in item[0]):
            try:
                movieurl = item[1]
                if movieurl:
                    addDir('folder','playurl',movieurl,"Oneload",getImgPath("openload_icon"),getImgPath("openload_fanart"))
            except:
                xbmc.log("unable to fetch Oneload URL") 
        if ("estream" in item[1]):
            try:
                movieurl = item[1]
                if movieurl:
                    addDir('folder','playurl',movieurl,"estream",getImgPath("openload_icon"),getImgPath("openload_fanart"))
            except:
                xbmc.log("unable to fetch Oneload URL") 
        if ("Prostream" in item[0]):
            xbmc.log("work in progress")
        if ("Oload" in item[0]):
            xbmc.log("work in progress")
        if ("Vidzi" in item[0]):
            try:
                movieurl = item[1]
                if movieurl:
                    addDir('folder','playurl',movieurl,"Vidzi",getImgPath("openload_icon"),getImgPath("openload_fanart"))
            except:
                xbmc.log("unable to fetch Oneload URL")
        if ("vidoza" in item[0]):
            try:
                movieurl = item[1]
                if movieurl:
                    tempurl = getdatacontent(movieurl, 'sourcesCode: \[{ src: \"(.*?)\", type: "video\/mp4", label:\"(.*?)\", res:\"(.*?)\"}\]')
                    tempurl = tempurl[0]
                    xbmc.log("fetching vidoza URL") 
                    xbmc.log(tempurl[0])
                    tempurl = tempurl[0].replace('https','http')
                    xbmc.log(tempurl)
                    addDir('','',tempurl,"vidoza",getImgPath("openload_icon"),getImgPath("openload_fanart")) 
                    #addDir('folder','playurl',tempurl[0],"vidoza",getImgPath("openload_icon"),getImgPath("openload_fanart"))
            except:
                xbmc.log("unable to fetch Oneload URL") 
        if ("vup" in item[0]):
            try:
                movieurl = item[1]
                if movieurl:
                    addDir('folder','playurl',movieurl,"vup",getImgPath("openload_icon"),getImgPath("openload_fanart"))
            except:
                xbmc.log("unable to fetch Oneload URL")
        if ("netutv" in item[0]):
            try:
                movieurl = item[1]
                if movieurl:
                    addDir('folder','playurl',movieurl,"netutv",getImgPath("openload_icon"),getImgPath("openload_fanart"))
            except:
                xbmc.log("unable to fetch Oneload URL")
        if ("videobin" in item[0]):
            try:
                movieurl = item[1]
                if movieurl:
                    addDir('folder','playurl',movieurl,"videobin",getImgPath("openload_icon"),getImgPath("openload_fanart"))
            except:
                xbmc.log("unable to fetch Oneload URL")

    # for item in data:
    #     if ("Openload" in item[0]):
    #         try:
    #             url = getdatacontent(item[1],"(?:iframe src|IFRAME SRC)=\"(.+?)\"")
    #             movieurl = resolveurl.HostedMediaFile(url[0])
    #             movieurl = movieurl.resolve()
    #             if movieurl:
    #                 addDir('','',movieurl,"openload",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    #         except:
    #             xbmc.log("unable to fetch openload URL")      
    #     if ("Streamango" in item[0]):
    #         movieurl = resolveurl.HostedMediaFile(item[1])
    #         movieurl = movieurl.resolve()
    #         if movieurl:
    #             addDir('','',movieurl,"streamango",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    #     if ("Netutv" in item[0]):
    #         xbmc.log("work in progress")
    #     if ("Oneload" in item[0]):
    #         try:
    #             movieurl = resolveurl.HostedMediaFile(item[1])
    #             movieurl = movieurl.resolve()
    #             if movieurl:
    #                 addDir('','',movieurl,"Oneload",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    #         except:
    #             xbmc.log("unable to fetch Oneload URL") 
    #     if ("Prostream" in item[0]):
    #         xbmc.log("work in progress")
    #     if ("Oload" in item[0]):
    #         xbmc.log("work in progress")
    #     if ("Vidzi" in item[0]):
    #         try:
    #             movieurl = resolveurl.HostedMediaFile(item[1])
    #             movieurl = movieurl.resolve()
    #             if movieurl:
    #                 addDir('','',movieurl,"Vidzi",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    #         except:
    #             xbmc.log("unable to fetch Oneload URL") 
    xbmcplugin.endOfDirectory(int(sys.argv[1]))