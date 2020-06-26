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

def loadvoirfilms(url):
    args = sys.argv[2]
    if str(sys.argv[2]).find('url=') > 1:
        args = sys.argv[2]
        mode = args.split('url=')
        #xbmc.log(str(mode))
        mode = mode[1]
        mode = mode.split('&')
        url = mode[0]
        url = urllib.unquote_plus(url)
    #data = getdatacontent(url,"<a href=\"(?P<link>.*?)\" title=\"(?P<title>.*?)\">\s+<span class=\"affiche\">\s+<span class=\"(.*?)\"><\/span>\s*<img src=\"(?P<icon>.*?)\"")
    try:
        data = getdatacontent(url,"<a href=\"(?P<link>.*?)\" title=\"(?P<title>.*?)\">\s+<span class=\"affiche\">\s+<span class=\"(.*?)\"><\/span>\s*<img src=\"(?P<icon>.*?)\" alt=\"(.*?)\" style=\"(.*?)\">\s+<\/span>\s+<\/a>\s+<(.*?)>\s+<(.*?)>\s+<(.*?)>\s+<(.*?)>\s+<span class=\"(.*?)\"")
        xbmc.log("-----------------------------------------------loadvoirfilms -------------------------------------------------------------")
        xbmc.log(str(data))
        #data = getdatacontent(url,"<a href=\"(.*?)\" title=\"(.*?)\">\s+<span class=\"affiche\">\s+<span class=\"(.*?)\"><\/span>\s*<img src=\"(>.*?)\" alt=\"(.*?)\" style=\"(.*?)\">\s+<\/span>\s+<\/a>\s+<(.*?)>\s+<(.*?)>\s+<(.*?)>\s+<(.*?)>\s+<span class=\"(.*?)\"")
        nav = getdatacontent(url,"<a href=\W+\/lesfilms\d+\W+ rel=\W+nofollow\W+>suiv")
        xbmc.log("-----------------------------------------------loadvoirfilms -------------------------------------------------------------")
        xbmc.log(str(nav))
        nav = nav[0]
        reg = "href=\"(.*?)\""
        nav = re.compile(reg).findall(nav)
        url = url.split("/")
        url = "http://"+url[2]
        #xbmc.log("-----------------------------------------------loadvoirfilms -------------------------------------------------------------")
        for item in data:
            link = url+item[0].decode('utf-8',errors='ignore')
            #xbmc.log(link)
            title = item[4].decode('utf-8',errors='ignore')
            title = title + '-'+item[2]+'-'+item[10].replace('qualite', '')
            ##xbmc.log(title)
            icon = item[3].decode('utf-8',errors='ignore')
            #xbmc.log(icon)
            #icon = icon.replace("https","http")
            addDir('folder','playvoirfilms',link,title,icon,icon)
        if nav:
            #xbmc.log("-----------------------------------------------load voirfims navlink-------------------------------------------------------------")
            navlink = url+nav[0]
            #xbmc.log(navlink)
            addDir( 'folder','voirfilms',navlink,'[B]Next Page...[/B]',"https://lh3.googleusercontent.com/-NsVeHCUW0lo/V4b8r67FVSI/AAAAAAAAD7U/G1ifDqs0nFENPck0-oKCQgc3-Gdm_JM7QCCo/s574/next_574x358.png","https://lh3.googleusercontent.com/-NsVeHCUW0lo/V4b8r67FVSI/AAAAAAAAD7U/G1ifDqs0nFENPck0-oKCQgc3-Gdm_JM7QCCo/s574/next_574x358.png" )
    except Exception as e:
        xbmcgui.Dialog().ok('XBMC', str(e))        
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def playvoirfilms():
    args = sys.argv[2]
    mode = args.split('url=')
    mode = mode[1]
    mode = mode.split('&')
    url = mode[0]
    url = urllib.unquote_plus(url)
    xbmc.log("-----------------------------------------------playvoirfilms - url-------------------------------------------------------------")
    xbmc.log(url)
    headers = {
            'Host': url,
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'DNT': '1',
            'Referer': url,
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8,ta;q=0.7,fr-FR;q=0.6,zh-CN;q=0.5,zh;q=0.4',
            
    }
    data= getdatacontent(url,"data-src=\"(.*?)\" target=\"(.*?)\" class=\"(.*?)\" rel=\"(.*?)\"><div class=\"(.*?)\" style=\"(.*?)\"><div class=\"(.*?)\">Lien \d+:<\/div><div class=\"(.*?)\" style=\"(.*?)\">\s+<span class=\"(.*?)\"><\/span>")
    #xbmc.log(str(data))
    #xbmc.log("-----------------------------------------------playvoirfilms - DATA-------------------------------------------------------------")

    for item in data:
        #xbmc.log("-----------------------------------------------playvoirfilms - item-------------------------------------------------------------")
        #xbmc.log(str(item))
        url_temp = "http://www.voirfims.ws"+item[0]
        r = requests.get(url_temp,headers=headers)
        link =  r.text
        #xbmc.log("-----------------------------------------------playvoirfilms - link-------------------------------------------------------------")
        #xbmc.log(str(link))
        reg = 'url=(.*?)\"'
        link = re.compile(reg).findall(link)
        if link:
            if resolveurl.HostedMediaFile(link[0]):
                addDir('folder','playurl',link[0],getstreamlinkname(link[0]),getImgPath("openload_icon"),getImgPath("openload_fanart"))
            ##xbmc.log("HostedMediaFile:"+str(resolveurl.HostedMediaFile(link))


    # for item in data:
    #     if ("Openload" in item[0]):
    #         try:
    #             url = getdatacontent(item[1],"(?:iframe src|IFRAME SRC)=\"(.+?)\"")
    #             movieurl = url[0]
    #             if movieurl:
    #                 addDir('folder','playurl',movieurl,"openload",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    #         except:
    #             #xbmc.log("unable to fetch openload URL")      
    #     if ("Streamango" in item[0]):
    #         movieurl = item[1]
    #         if movieurl:
    #             addDir('folder','playurl',movieurl,"streamango",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    #     if ("Netutv" in item[0]):
    #         #xbmc.log("work in progress")
    #     if ("Oneload" in item[0]):
    #         try:
    #             movieurl = item[1]
    #             if movieurl:
    #                 addDir('folder','playurl',movieurl,"Oneload",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    #         except:
    #             #xbmc.log("unable to fetch Oneload URL") 
    #     if ("estream" in item[1]):
    #         try:
    #             movieurl = item[1]
    #             if movieurl:
    #                 addDir('folder','playurl',movieurl,"estream",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    #         except:
    #             #xbmc.log("unable to fetch Oneload URL") 
    #     if ("Prostream" in item[0]):
    #         #xbmc.log("work in progress")
    #     if ("Oload" in item[0]):
    #         #xbmc.log("work in progress")
    #     if ("Vidzi" in item[0]):
    #         try:
    #             movieurl = item[1]
    #             if movieurl:
    #                 addDir('folder','playurl',movieurl,"Vidzi",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    #         except:
    #             #xbmc.log("unable to fetch Oneload URL") 
    # # for item in data:
    # #     if ("Openload" in item[0]):
    # #         try:
    # #             url = getdatacontent(item[1],"(?:iframe src|IFRAME SRC)=\"(.+?)\"")
    # #             movieurl = resolveurl.HostedMediaFile(url[0])
    # #             movieurl = movieurl.resolve()
    # #             if movieurl:
    # #                 addDir('','',movieurl,"openload",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    # #         except:
    # #             #xbmc.log("unable to fetch openload URL")      
    # #     if ("Streamango" in item[0]):
    # #         movieurl = resolveurl.HostedMediaFile(item[1])
    # #         movieurl = movieurl.resolve()
    # #         if movieurl:
    # #             addDir('','',movieurl,"streamango",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    # #     if ("Netutv" in item[0]):
    # #         #xbmc.log("work in progress")
    # #     if ("Oneload" in item[0]):
    # #         try:
    # #             movieurl = resolveurl.HostedMediaFile(item[1])
    # #             movieurl = movieurl.resolve()
    # #             if movieurl:
    # #                 addDir('','',movieurl,"Oneload",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    # #         except:
    # #             #xbmc.log("unable to fetch Oneload URL") 
    # #     if ("Prostream" in item[0]):
    # #         #xbmc.log("work in progress")
    # #     if ("Oload" in item[0]):
    # #         #xbmc.log("work in progress")
    # #     if ("Vidzi" in item[0]):
    # #         try:
    # #             movieurl = resolveurl.HostedMediaFile(item[1])
    # #             movieurl = movieurl.resolve()
    # #             if movieurl:
    # #                 addDir('','',movieurl,"Vidzi",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    # #         except:
    # #             #xbmc.log("unable to fetch Oneload URL") 
    xbmcplugin.endOfDirectory(int(sys.argv[1]))