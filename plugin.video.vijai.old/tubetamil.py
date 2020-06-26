import urllib2, urllib, xbmcgui, xbmcplugin,xbmcaddon, xbmc, re, sys, os, requests
from bs4 import BeautifulSoup
from t0mm0.common.net import Net
from t0mm0.common.addon import Addon
from unpack import unpack
from vijaicontent import getdatacontent,gethtmlcontent
from vijaidirectory import addDir
import resolveurl
from getImgPath import getImgPath
from playurl import playurl
dialog = xbmcgui.Dialog()

def tubetamil(url):
    xbmc.log(sys.argv[2])
    args = sys.argv[2]
    if str(sys.argv[2]).find('url=') > 1:
        args = sys.argv[2]
        mode = args.split('url=')
        #xbmc.log(str(mode))
        mode = mode[1]
        mode = mode.split('&')
        url = mode[0]
        url = urllib.unquote_plus(url)
    headers = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'DNT': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr;q=0.6',
    }
    # try:
    #page = requests.get(url, headers=headers, verify=False)
    page = gethtmlcontent(url)
    soup = BeautifulSoup(page, 'html.parser')
    for div in soup.findAll("div", {"class": "thumb"}):
        for each in div.findAll('a'):
            link = each.get('href')
            title = each.get('title')
            title = title.encode('UTF-8')
            thumbnail = each.img['src']
            thumbnail = thumbnail.replace(" ", "")
            addDir('folder','tubetamilloadcontent',link,title,thumbnail,thumbnail)
    for li in soup.findAll("li",{"class":"next"}):
        if li:
            for each in li.findAll('a'):
                nextbutton = each.get('href')
                #print'Nextbutton : '+nextbutton
                addDir( 'folder','tubetamil',nextbutton,'[B]Next Page...[/B]',"https://lh3.googleusercontent.com/-NsVeHCUW0lo/V4b8r67FVSI/AAAAAAAAD7U/G1ifDqs0nFENPck0-oKCQgc3-Gdm_JM7QCCo/s574/next_574x358.png","https://lh3.googleusercontent.com/-NsVeHCUW0lo/V4b8r67FVSI/AAAAAAAAD7U/G1ifDqs0nFENPck0-oKCQgc3-Gdm_JM7QCCo/s574/next_574x358.png")
    # except Exception as e:
    #     xbmcgui.Dialog().ok('XBMC', str(e))
     
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def tubetamilloadcontent():
    args = sys.argv[2]
    mode = args.split('url=')
    mode = mode[1]
    mode = mode.split('&')
    url = mode[0]
    url = urllib.unquote_plus(url) 
    headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr;q=0.6',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
           }
    #page = requests.get(url, headers=headers, verify=False)
    page = gethtmlcontent(url)
    soup = BeautifulSoup(page, 'html.parser')
    try:
        iframe = soup.find_all('iframe')[0]['src']
        if "youtube" in iframe:
            addDir('folder','playurl',iframe,"youtube - link",getImgPath("openload_icon"),getImgPath("openload_fanart"))
        if "dailymotion" in iframe:
            addDir('folder','playurl',iframe,"Dailymotion - link",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    except:
        xbmcgui.Dialog().ok('XBMC', 'Cannot Proccess This Link at the Moment - Work In Progress')  
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
