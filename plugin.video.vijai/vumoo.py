import urllib2, urllib, xbmcgui, xbmcplugin,xbmcaddon, xbmc, re, sys, os, requests
from t0mm0.common.net import Net
from t0mm0.common.addon import Addon
from unpack import unpack
from vijaicontent import getdatacontent
from vijaidirectory import addDir
import resolveurl
from getImgPath import getImgPath
def vumoo(url):
    args = sys.argv[2]
    if str(sys.argv[2]).find('url=') > 1:
        args = sys.argv[2]
        mode = args.split('url=')

        mode = mode[1]
        mode = mode.split('&')
        url = mode[0]
        url = urllib.unquote_plus(url)
    proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy_handler)
    req = urllib2.Request(url)
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    r = opener.open(req)
    html = r.read()
    reg ="(?:<div class=\"slick-slide category-slide video_item movie_item_container\" id=\"\w+_\d+\">|<div class=\"slick-slide category-slide video_item movie_item_container\" id=\"\w+_\d+\"> <div class=\"cam-badge\">\s\w+\s<\/div>) <a href=\"(.*?)\"\sdata-remote=\"(.*?)\" alt=\"(.*?)\" class=\"zoom\" data-title=\"(.*?)\" data-type=\"page\" > <div class=\"artwork\" style=\"background-image: url(.*?);"
    data = re.compile(reg).findall(html)
    for item in data:
        img = str(item[4]).replace("(","")
        img = img.replace(")","")
        addDir('folder','loadvumoomovie',"http://vumoo.li"+item[0] ,item[2],img,img)
    index = int(url[-1:])
    index = index + 1
    addDir( 'folder','vumoo',"http://vumoo.li/videos/category/New%20releases/?page="+str(index),'[B]Next Page...[/B]',"https://lh3.googleusercontent.com/-NsVeHCUW0lo/V4b8r67FVSI/AAAAAAAAD7U/G1ifDqs0nFENPck0-oKCQgc3-Gdm_JM7QCCo/s574/next_574x358.png","https://lh3.googleusercontent.com/-NsVeHCUW0lo/V4b8r67FVSI/AAAAAAAAD7U/G1ifDqs0nFENPck0-oKCQgc3-Gdm_JM7QCCo/s574/next_574x358.png" )
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def loadvumoomovie():
    args = sys.argv[2]
    mode = args.split('url=')
    mode = mode[1]
    mode = mode.split('&')
    url = mode[0]
    url = urllib.unquote_plus(url) 

    proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy_handler)
    req = urllib2.Request(url)
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')]
    r = opener.open(req)
    html = r.read()
    reg = "var googleLink = \"(.*?)\""
    data = re.compile(reg).findall(html)
    if data:
        if data[0] != "null":
            data = re.compile(reg).findall(html)
            xbmc.log("vumoo google---------------------------------------------------------------------------------------------------------------------------------------------")
            xbmc.log(str(data))
            st = data[0]
            st = st[-5:]
            url = "http://vumoo.li/api/plink?id="
            url = url+st+"&res=720"
            headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Encoding': 'gzip, deflate, sdch','Accept-Language': 'en-US,en;q=0.8,fr;q=0.6,ta;q=0.4,fr-FR;q=0.2,zh-CN;q=0.2,zh;q=0.2', 'Connection': 'keep-alive', 'Cookie': '__cfduid=d851158c20c1b099dbf03851cea1c6dbb1496161096; ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22e6558729140a03503c22bee37bf3ea0e%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A15%3A%22108.162.229.103%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A115%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F58.0.3029.110+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1496258372%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D3612882b165565b2fcbd22b1707ea281','DNT':'1', 'Host': 'vumoo.li','Upgrade-Insecure-Requests':'1', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' }
            try:
                r = requests.get(url,headers=headers, allow_redirects=False)
                movieurl=  r.headers.get('location')
                headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Encoding': 'gzip, deflate, sdch','Accept-Language': 'en-US,en;q=0.8,fr;q=0.6,ta;q=0.4,fr-FR;q=0.2,zh-CN;q=0.2,zh;q=0.2', 'Connection': 'keep-alive', 'Cookie': 'NID=104=bn3vrgPkdaObtpTcvpUVPzYXFxJ3MWwOckpA7G520PYiANHyzUsofTpJOgbxsPt0MXJQx9S89wlX1pIqGnAYnC06ZnMgOHERw7zN4HKhTAcpkrXQpNxG3-XwPw_0AZbW','DNT':'1', 'Host': 'lh3.googleusercontent.com','Upgrade-Insecure-Requests':'1', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' }
                try:
                    r = requests.get(movieurl,headers=headers, allow_redirects=False)
                    movieurl=  r.headers.get('location')
                    if movieurl:
                        #print movieurl
                        addDir('','',movieurl,"vumoolink-720p",getImgPath("vumoo_icon"),getImgPath("vumoo_fanart"))
                except:
                    xbmc.log("request failed")
            except:
                xbmc.log("request failed") 
            try:
                url = url+st+"&res=360"
                headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Encoding': 'gzip, deflate, sdch','Accept-Language': 'en-US,en;q=0.8,fr;q=0.6,ta;q=0.4,fr-FR;q=0.2,zh-CN;q=0.2,zh;q=0.2', 'Connection': 'keep-alive', 'Cookie': '__cfduid=d851158c20c1b099dbf03851cea1c6dbb1496161096; ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22e6558729140a03503c22bee37bf3ea0e%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A15%3A%22108.162.229.103%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A115%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F58.0.3029.110+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1496258372%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D3612882b165565b2fcbd22b1707ea281','DNT':'1', 'Host': 'vumoo.li','Upgrade-Insecure-Requests':'1', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' }
                r = requests.get(url,headers=headers, allow_redirects=False)
                movieurl=  r.headers.get('location')
                headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Encoding': 'gzip, deflate, sdch','Accept-Language': 'en-US,en;q=0.8,fr;q=0.6,ta;q=0.4,fr-FR;q=0.2,zh-CN;q=0.2,zh;q=0.2', 'Connection': 'keep-alive', 'Cookie': 'NID=104=bn3vrgPkdaObtpTcvpUVPzYXFxJ3MWwOckpA7G520PYiANHyzUsofTpJOgbxsPt0MXJQx9S89wlX1pIqGnAYnC06ZnMgOHERw7zN4HKhTAcpkrXQpNxG3-XwPw_0AZbW','DNT':'1', 'Host': 'lh3.googleusercontent.com','Upgrade-Insecure-Requests':'1', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' }
                r = requests.get(movieurl,headers=headers, allow_redirects=False)
                movieurl=  r.headers.get('location')
                if movieurl:
                    #print movieurl
                    addDir('','',movieurl,"vumoolink-360p",getImgPath("vumoo_icon"),getImgPath("vumoo_fanart"))
            except:
                xbmc.log("request failed") 
    
    reg = "var openloadLink = \"(.*?)\""
    data = re.compile(reg).findall(html)
    if data:
        url = data[0]
        movieurl = url.replace("\\","")
        xbmc.log("openload proper url ---------------------------------------------------------------------------------------------------------------------------------------------")
        xbmc.log(movieurl)
    try:
        movieurl = resolveurl.HostedMediaFile(movieurl)
        movieurl = movieurl.resolve()
        xbmc.log("movie url ---------------------------------------------------------------------------------------------------------------------------------------------")
        if movieurl:
            addDir('','',movieurl,"openloadlink",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    except:
        xbmc.log("unable to fetch openload URL")           
    

    xbmcplugin.endOfDirectory(int(sys.argv[1]))