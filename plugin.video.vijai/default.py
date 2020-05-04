import urllib2, urllib, xbmcgui, xbmcplugin,xbmcaddon, xbmc, re, sys, os, requests
from t0mm0.common.net import Net
from t0mm0.common.addon import Addon
from unpack import unpack
import resolveurl
from vijaicontent import getdatacontent,gethtmlcontent,addDir,getImgPath
# from getImgPath import getImgPath
# from vijaidirectory import addDir
from tamilgun import tamilgun,loadgunmovie
from tubetamil import tubetamil,tubetamilloadcontent
from vumoo import vumoo,loadvumoomovie
from voirfilms import loadvoirfilms,playvoirfilms
from onlinemoviewatchs import onlinemoviewatchscontent,loadonlinemoviewatchs,onlinemoviewatchsmenu
from movierulz import loadmovierulz,playMovierulz
from vexmovies import loadvexmovies,playvexmovies
from playurl import playurl
from movie import site
addon_handle= int(sys.argv[1])
get_site_content_regex = '<a href=\"(?P<pageurl>.*?)\"\stitle=\"(?P<title>.*?)\">\s*<img width=\"\d+\" height=\"\d+\" src=\"(?P<poster>.*?)\"'
get_nav_data_regex = '<a href=\"(.*?)\">&larr;(\s|)Older Entries'
get_stream_url_regex = '<p><strong>(?P<streamtitle>.*?)<\/strong><br \/>\s+<a href=\"(?P<streamurl>.*?)\"'
movierulz_tamil = site(url="",redirection_name="movierulz_tamil",get_site_content_regex=get_site_content_regex,get_nav_data_regex=get_nav_data_regex,get_stream_url_regex=get_stream_url_regex)
xbmc.log('Checking if movierulz_tamil is a an object------------------------------------')
xbmc.log(str(isinstance(movierulz_tamil,site)))
# def playurl()
#     args = sys.argv[2]
#     mode = args.split('url=')
#     mode = mode[1]
#     mode = mode.split('&')
#     url = mode[0]
#     url = urllib.unquote_plus(url)
#     movieurl = resolveurl.HostedMediaFile(url)
#     movieurl = movieurl.resolve()
#     xbmc.Player().play(url)

# def main_menu():
#     addDir('folder','tamilgun_HD_movie','','tamilgun_HD_movie',getImgPath("tamilgun_HD_movie_icon"),getImgPath("tamilgun_fanart"))
#     addDir('folder','tamilgun_Newmovie','','tamilgun_Newmovie',getImgPath("tamilgun_Newmovie_icon"),getImgPath("tamilgun_fanart"))
#     addDir('folder','vumoo','','vumoo',getImgPath("vumoo_icon"),getImgPath("vumoo_fanart"))
#     addDir('folder','onlinemoviewatchstelugu','','onlinemoviewatchstelugu',getImgPath("onlinemoviewatch_icon"),getImgPath("onlinemoviewatch_fanart"))
#     addDir('folder','onlinemoviewatchstamil','','onlinemoviewatchstamil',getImgPath("onlinemoviewatch_icon"),getImgPath("onlinemoviewatch_fanart"))
#     addDir('folder','onlinemoviewatchshindi','','onlinemoviewatchshindi',getImgPath("onlinemoviewatch_icon"),getImgPath("onlinemoviewatch_fanart"))
#     addDir('folder','movierulz-telugu','','movierulz-telugu',getImgPath("movierulz_icon"),getImgPath("movierulz_icon"))
#     addDir('folder','movierulz-tamil','','movierulz-tamil',getImgPath("movierulz_icon"),getImgPath("movierulz_icon"))
#     addDir('folder','movierulz-hindi','','movierulz-hindi',getImgPath("movierulz_icon"),getImgPath("movierulz_icon"))
#     xbmcplugin.endOfDirectory(int(sys.argv[1]))
def main_menu():
    addDir('folder','tamil','','tamil',getImgPath("tamil"),getImgPath("tamil"))
    addDir('folder','telugu','','telugu',getImgPath("telugu"),getImgPath("telugu"))
    addDir('folder','hindi','','hindi',getImgPath("hindi"),getImgPath("hindi"))
    addDir('folder','hollywood','','hollywood',getImgPath("hollywood"),getImgPath("hollywood"))
    addDir('folder','French','','French',getImgPath("french"),getImgPath("french"))
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def tamil():
    addDir('folder','tamilgun_HD_movie','','tamilgun_HD_movie',getImgPath("tamilgun_HD_movie_icon"),getImgPath("tamilgun_fanart"))
    addDir('folder','tamilgun_Newmovie','','tamilgun_Newmovie',getImgPath("tamilgun_Newmovie_icon"),getImgPath("tamilgun_fanart"))
    addDir('folder','tamilgun_Dubbedmovie','','tamilgun_Dubbedmovie',getImgPath("tamilgun_Newmovie_icon"),getImgPath("tamilgun_fanart"))
    addDir('folder','tubetamil','','tubetamil',getImgPath("tubetamil_icon"),getImgPath("tubetamil_icon"))
    addDir('folder','onlinemoviewatchs','','onlinemoviewatchs',getImgPath("onlinemoviewatch_icon"),getImgPath("onlinemoviewatch_fanart"))
    addDir('folder','movierulz_tamil','','movierulz_tamil',getImgPath("movierulz_icon"),getImgPath("movierulz_icon"))
    addDir('folder','movierulz-all-tamil-movies','','movierulz-all-tamil-movies',getImgPath("movierulz_icon"),getImgPath("movierulz_icon"))
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
def telugu():
	addDir('folder','onlinemoviewatchs','','onlinemoviewatchs',getImgPath("onlinemoviewatch_icon"),getImgPath("onlinemoviewatch_fanart"))
	addDir('folder','movierulz-telugu','','movierulz-telugu',getImgPath("movierulz_icon"),getImgPath("movierulz_icon"))
	addDir('folder','movierulz-all-telugu-movies','','movierulz-all-telugu-movies',getImgPath("movierulz_icon"),getImgPath("movierulz_icon"))
	xbmcplugin.endOfDirectory(int(sys.argv[1]))
def hindi():
    addDir('folder','onlinemoviewatchs','','onlinemoviewatchs',getImgPath("onlinemoviewatch_icon"),getImgPath("onlinemoviewatch_fanart"))    
    addDir('folder','movierulz-hindi-2019','','movierulz-hindi-2019',getImgPath("movierulz_icon"),getImgPath("movierulz_icon"))
    addDir('folder','movierulz-hindi-2018','','movierulz-hindi-2018',getImgPath("movierulz_icon"),getImgPath("movierulz_icon"))    
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
def hollywood():
	addDir('folder','onlinemoviewatchs','','onlinemoviewatchs',getImgPath("onlinemoviewatch_icon"),getImgPath("onlinemoviewatch_fanart"))
	xbmcplugin.endOfDirectory(int(sys.argv[1]))
def French():
    addDir('folder','voirfilms','','voirfilms',getImgPath("voirfilms_icon"),getImgPath("voirfilms_fanart"))
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

mode = None
args = sys.argv[2]
if len(args) > 0:
    mode = args.split('mode=')
    mode=mode[1].split('&')
    mode = mode[0]

if mode == None: 
    main_menu()
elif mode == 'tamil':
    tamil()
elif mode == 'telugu':
    telugu()
elif mode == 'hindi':
    hindi()
elif mode == 'hollywood':
    hollywood()
elif mode == 'French':
    French()
elif mode == 'tamilgun_HD_movie': 
    url = "http://tamilgun.com"
    r = requests.get(url) 
    url = r.url
    url = url.split('/')
    url = url[0]+'//'+url[2]+'/'
    xbmc.log("tamilgun url--------------------------------------------------------------------------------")
    xbmc.log(url)
    tamilgun_HD_movie = url+"categories/hd-movies/"
    xbmc.log(tamilgun_HD_movie)
    tamilgun(tamilgun_HD_movie)
elif mode == 'tamilgun_Newmovie':
    url = "http://tamilgun.com"
    r = requests.get(url) 
    url = r.url
    url = url.split('/')
    url = url[0]+'//'+url[2]+'/'
    xbmc.log("tamilgun url--------------------------------------------------------------------------------")
    xbmc.log(url)
    tamilgun_Newmovie = url+"categories/new-movies-a/" 
    tamilgun(tamilgun_Newmovie)
elif mode == 'tamilgun_Dubbedmovie':
    url = "http://tamilgun.com"
    r = requests.get(url) 
    url = r.url
    url = r.url
    url = url.split('/')
    url = url[0]+'//'+url[2]+'/'
    tamilgun_Dubbedmovie = url+"categories/dubbed-movies/" 
    tamilgun(tamilgun_Dubbedmovie)
elif mode == 'tubetamil':
    url = "https://www.tubetamil.com"
    tubetamil(url)
elif mode == 'onlinemoviewatchs':
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'DNT': '1',
    }

    response = requests.get('https://onlinemoviewatch.org/', headers=headers)
    url = response.headers
    url = url['Link']
    url = url.split('/')
    url = "https://"+url[2]
    xbmc.log("url--------------------------------------")
    xbmc.log(url)
    onlinemoviewatchsmenu(url)
elif mode == 'onlinemoviewatchsmenu':
    url = "http://www.onlinemoviewatch.org"
    r = requests.get(url,verify=False) 
    url = r.url
    onlinemoviewatchscontent(url)
elif mode == 'onlinemoviewatchscontent':
    # args = sys.argv[2]
    # mode = args.split('url=')
    # mode = mode[1]
    # mode = mode.split('&')
    # url = mode[0]
    # url = urllib.unquote_plus(url)
    onlinemoviewatchscontent()
elif mode == 'loadvumoomovie':
    loadvumoomovie()
elif mode == 'loadgunmovie':
    loadgunmovie()
elif mode == 'tubetamilloadcontent':
    tubetamilloadcontent()
elif mode == 'loadonlinemoviewatchs':
    loadonlinemoviewatchs()
elif mode == 'movierulz-telugu':
    url = "http://www.movierulz.com"
    r = requests.get(url) 
    url = r.url
    url = url+"/telugu-movie/"
    loadmovierulz(url)
elif mode == 'movierulz-all-telugu-movies':
    url = "http://www.movierulz.com"
    r = requests.get(url) 
    url = r.url
    url = url+"/category/telugu-movie/"
    loadmovierulz(url)
elif mode == 'movierulz_tamil':
    url = "http://www.movierulz.com"
    r = requests.get(url) 
    url = r.url
    url = url+"/tamil-movie-free/"
    movierulz_tamil.loadsitecontent(url)
# elif mode == 'movierulz-tamil':
#     url = "http://www.movierulz.com"
#     r = requests.get(url) 
#     url = r.url
#     url = url+"/category/tamil-movie/"

#     loadmovierulz(url)
# elif mode == 'movierulz-hindi-2018':
#     url = "http://www.movierulz.com"
#     r = requests.get(url) 
#     url = r.url
#     url = url+"/category/bollywood-movie-2018/"
#     loadmovierulz(url)
# elif mode == 'movierulz-hindi-2019':
#     url = "http://www.movierulz.com"
#     r = requests.get(url) 
#     url = r.url
#     url = url+"/category/bollywood-movie-2019/"
#     loadmovierulz(url)
elif mode == 'liststreamurl':
    #playMovierulz()
    movierulz_tamil.liststreamurl()
elif mode == 'playurl':
    playurl()
elif mode == 'voirfilms':
    url = "https://www.voirfilms.com"
    try:
        r = requests.get(url) 
        url = r.url
        voirfilms_url = url+"/film-en-streaming" 
        loadvoirfilms(voirfilms_url)
    except Exception as e:
        xbmcgui.Dialog().ok('XBMC', str(e))
elif mode == 'playvoirfilms':
    playvoirfilms()
xbmcplugin.endOfDirectory(addon_handle)





