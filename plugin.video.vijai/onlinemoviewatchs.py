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
def getonlinemoviewatchcontent(url,regex):
    headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr;q=0.6',
            'Connection': 'keep-alive',
            'DNT': '1',

            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
           }
    r = requests.get(url, headers=headers,verify=False)
    html = r.content
    data = re.compile(regex).findall(html)
    return data
def getstreamurl(url,serverurl,title):
    title = urllib2.quote(title)
    serverurl= serverurl+title
    headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr;q=0.6',
                'Connection': 'keep-alive',
                'DNT': '1',

                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
               }
    try:
        r = requests.get(serverurl, headers=headers)
        return r.text
    except:
        xbmc.log("fetch error")

def onlinemoviewatchsmenu(url):
    args = sys.argv[2]
    if str(sys.argv[2]).find('url=') > 1:
        args = sys.argv[2]
        mode = args.split('url=')
        #xbmc.log(str(mode))
        mode = mode[1]
        mode = mode.split('&')
        url = mode[0]
        url = urllib.unquote_plus(url)
    global referer_temp
    referer_temp = url+"/sw.js"
    headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Sec-Fetch-Mode': 'same-origin',
    'Sec-Fetch-User': '?1',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr;q=0.6',
    'Referer': referer_temp,
    'Origin': url,
    'Cache-Control': 'max-age=0',
    'Service-Worker': 'script',
    }
    response = requests.get(url, headers=headers)
    page = response.content
    soup = BeautifulSoup(page, 'html.parser')
    list = soup.find("ul", id ="menu-menu")
    for link in list.find_all('li'):
        name = link.find('a')
        reg = 'href=\"(.*?)\">(.*?)<'
        data = re.compile(reg).findall(str(name))
        for item in data:
            addDir('folder','onlinemoviewatchscontent',item[0],item[1],"","")
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def onlinemoviewatchscontent():
    #xbmc.log('-----------------------------------------------------program entered onlinemoviewatchscontent------------------------------------------------------------------')
    #xbmc.log(url)
    args = sys.argv[2]
    mode = args.split('url=')
    mode = mode[1]
    mode = mode.split('&')
    url = mode[0]
    url = urllib.unquote_plus(url) 
    xbmc.log('-----------------------------------------------------program entered onlinemoviewatchscontent------------------------------------------------------------------')
    xbmc.log(url)
    # args = sys.argv[2]
    # if str(sys.argv[2]).find('url=') > 1:
    #     args = sys.argv[2]
    #     mode = args.split('url=')
    #     #xbmc.log(str(mode))
    #     mode = mode[1]
    #     mode = mode.split('&')
    #     url = mode[0]
    #     url = urllib.unquote_plus(url)
    # proxy_handler = urllib2.ProxyHandler({})
    # opener = urllib2.build_opener(proxy_handler)
    # req = urllib2.Request(url)
    # opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    # r = opener.open(req)
    # html = r.read()
    # r = requests.get(url)
    # url=r.url    
    # headers = {
    #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr;q=0.6',
    #         'Connection': 'keep-alive',
    #         'DNT': '1',
    #         'Upgrade-Insecure-Requests': '1',
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    #        }
    # r = requests.get(url, headers=headers,verify=False)
    #res = gethtmlcontent(url)
    headers = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Sec-Fetch-Site': 'same-origin',
    'Referer': url,
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr;q=0.6',
    }
    response = requests.get(url, headers=headers)
    res = response.content
    #res= r.content
    #reg = "<div class=\"boxtitle\">\s*<h2><a href=\"(.*?)\" rel=\"bookmark\" title=\"(.*?)\">(.*?)<\/a><\/h2>\s*<\/div>\s*<div class=\"boxentry\">\s*<a href=\"(.*?)\" title=\"(.*?)\">\s*<div class=\"harvendra\">\s*<img width=\"\d+\" height=\"\d+\" src=\"(.*?)\""
    #reg = "<a href=\"(.*?)\" class=\"ml-mask\" title=\"(.*?)\">(?:(\s*)|(\s*<span class=\"mli-quality\">\w+<\/span>\s*))<img class=\"thumb mli-thumb lazy\" title=\"(.*?)\" alt=\"\" data-original=\"(.*?)\" src=\"(.*?)\" style=\"display: block;\">\s*<span class=\"mli-info\">"
    #data = re.compile(reg).findall(res)
    #navRegex = '<a class="nextpostslink" rel="next" href=\"(.*?)\">&raquo;<\/a>'
    #nav = re.compile(navRegex).findall(html)
    #reg = "<div class=\"boxentry\"> <a href=\"(.*?)\" title=\"(.*?)\"><div class=\"harvendra\"> <img width=\"165\" height=\"220\" src=\"(.*?)\""
    #reg = "<a href=\"(.*?)\" title=\"(.*?)\">\s*<img width=\"\d*\" height=\"\d*\" src=\"(.*?)\""
    #reg = '<div class="boxentry">\s+<a href="(.*?)" title="(.*?)">\s+<div class="harvendra">\s+<noscript>(.*?)<\/noscript><img width="\d+"\sheight="\d+"\s+src=\'(.*?)\'\sdata-src="(.*?)"'
    #reg = '<div class="boxentry">\s+<a href="(.*?)" title="(.*?)"><div class="harvendra">\s<noscript>(.*?)<\/noscript><img width="\d+"\sheight="\d+"\s+src="(.*?)"\s+data-lazy-type=\"image\"\s+data-src=\"(.*?)\"'
    reg ='<div class="boxentry">\s+<a href="(.*?)" title="(.*?)">\s+<div class="harvendra">\s+<img width="\d+"\sheight="\d+"\s+src=\"(.*?)\"'
    nav = '<a class="nextpostslink" rel="next" href="(.*?)"'
    data = re.compile(reg).findall(res)
    nav = re.compile(nav).findall(res)
    for item in data:
        thumbnail = item[2]
        thumbnail = thumbnail.replace("https","http")
        addDir('folder','loadonlinemoviewatchs',item[0],item[1],thumbnail,thumbnail)
    if nav:
        nav = nav[0]
        # nav = nav[-52:]
        xbmc.log("-----------------------------------------------vijai test------------------------------------------------------------------")
        xbmc.log(nav)
        addDir( 'folder','onlinemoviewatchscontent',nav,'[B]Next Page...[/B]',"https://lh3.googleusercontent.com/-NsVeHCUW0lo/V4b8r67FVSI/AAAAAAAAD7U/G1ifDqs0nFENPck0-oKCQgc3-Gdm_JM7QCCo/s574/next_574x358.png","https://lh3.googleusercontent.com/-NsVeHCUW0lo/V4b8r67FVSI/AAAAAAAAD7U/G1ifDqs0nFENPck0-oKCQgc3-Gdm_JM7QCCo/s574/next_574x358.png")
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def loadonlinemoviewatchs():
    args = sys.argv[2]
    mode = args.split('url=')
    mode = mode[1]
    mode = mode.split('&')
    url = mode[0]
    url = urllib.unquote_plus(url) 
    #xbmc.log(url)
    #xbmc.log("------------------------------------Entering  load online movie watchs-----------------------------------------------------")
    #xbmc.log("------------------------------------scratching data for default player-----------------------------------------------------")
    # regex ='<iframe class=\"lazy lazy-hidden\"  data-lazy-type=\"iframe\" data-src=\"(.*?)\"'
    # headers = {
    # 'Connection': 'keep-alive',
    # 'Upgrade-Insecure-Requests': '1',
    # 'DNT': '1',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    # 'Sec-Fetch-Mode': 'navigate',
    # 'Sec-Fetch-User': '?1',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'Host': 'www11.onlinemoviewatch.org',
    # 'Referer': 'https://www11.onlinemoviewatch.org/movies/tamil-movies-2019',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr;q=0.6',
    # }
    # response = requests.get(url, headers=headers)
    # res = response.content
    # data = re.compile(regex).findall(res)
    # for urltemp in data:
    #     if 'onlinemoviewatch.in.net' in urltemp:
    #         headers = {
    #             'Connection': 'keep-alive',
    #             'Cache-Control': 'max-age=0',
    #             'Upgrade-Insecure-Requests': '1',
    #             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    #             'DNT': '1',
    #             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #             'Accept-Encoding': 'gzip, deflate, br',
    #             'Accept-Language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr;q=0.6',
    #         }
    #         response = requests.get(urltemp, headers=headers, verify=False)
    #         html = response.content
    #         regex = '<script type=\'text\/javascript\'>eval(.*)'
    #         data = re.compile(regex).findall(html)
    #         if data:
    #             out = unpack(data[0])
    #             regex = 'sources:\[(.*?)\]'
    #             data = re.compile(regex).findall(out)
    #             data = data[0]
    #             data = data.split('"')
    #             for link in data:
    #                 if 'm3u8'  in link:
    #                     addDir('','',link,"Default-player-Link",getImgPath("speedplay_icon"),getImgPath("speedplay_fanart"))
    #         #source code modified on 29042019 ---------------------------------------------------------------------
    #         regex = 'sources:\s\[{src:\s\"(.*?)\"'
    #         data = re.compile(regex).findall(html)
    #         if data:
    #             for link in data:
    #                 if 'm3u8'  in link:
    #                     addDir('','',link,"Default-player-Link",getImgPath("speedplay_icon"),getImgPath("speedplay_fanart"))
    #     if 'verystream' in urltemp:
    #         xbmc.log("-------------------------------------------very stream----------------------------------------------------------")
    #         xbmc.log(urltemp)
    #         response = requests.get(urltemp, verify=False)
    #         html = response.content
    #         regex = 'videolink\">(.*?)<'
    #         data = re.compile(regex).findall(html)
    #         xbmc.log(data[0])
    #         if data:
    #             templink= 'https://verystream.com/gettoken/'+data[0]+'?mime=true'
    #             xbmc.log(templink)
    #             headers = {
    #             'Connection': 'keep-alive',
    #             'Cache-Control': 'max-age=0',
    #             'Upgrade-Insecure-Requests': '1',
    #             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    #             'DNT': '1',
    #             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #             'Accept-Encoding': 'gzip, deflate, br',
    #             'Accept-Language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr;q=0.6',
    #             }   
    #             response = requests.get(templink, headers=headers, verify=False, allow_redirects=False)
    #             link = response.headers['Location']
    #             xbmc.log(link)
    #             if link:
    #                 addDir('','',link,"verystream",getImgPath("speedplay_icon"),getImgPath("speedplay_fanart"))
            


    xbmc.log("------------------------------------scratching data for very stream -----------------------------------------------------")
    regex = '<iframe src="(.*?)"'
    headers = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Sec-Fetch-Site': 'same-origin',
    'Host': 'www11.onlinemoviewatch.org',
    'Referer': 'https://www11.onlinemoviewatch.org/movies/tamil-movies-2019',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr;q=0.6',
    }
    response = requests.get(url, headers=headers)
    res = response.content
    data = re.compile(regex).findall(res)
    xbmc.log(str(data))
    for urltemp in data:
        if 'verystream' in urltemp:
            xbmc.log("-------------------------------------------very stream----------------------------------------------------------")
            xbmc.log(urltemp)
            response = requests.get(urltemp, verify=False)
            html = response.content
            regex = 'videolink\">(.*?)<'
            data = re.compile(regex).findall(html)
            #xbmc.log(data[0])
            if data:
                templink= 'https://verystream.com/gettoken/'+data[0]+'?mime=true'
                xbmc.log(templink)
                headers = {
                'Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
                'DNT': '1',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr;q=0.6',
                }   
                response = requests.get(templink, headers=headers, verify=False, allow_redirects=False)
                link = response.headers['Location']
                xbmc.log(link)
                if link:
                    addDir('','',link,"verystream",getImgPath("speedplay_icon"),getImgPath("speedplay_fanart"))
        if "oload" in urltemp:
            addDir('folder','playurl',urltemp,"oload",getImgPath("openload_icon"),getImgPath("openload_fanart"))
        if "1megavideo" in urltemp:
            reg = "<script type='text\/javascript'>eval\((.*=?)"
            headers = {
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr;q=0.6',
                        'Connection': 'keep-alive',
                        'DNT': '1',
                        'Host': '1megavideo.live',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
            }
            r = requests.get(urltemp, headers=headers,verify=False)
            html = r.content
            data = re.compile(reg).findall(html)
            res = data[0]
            out= unpack(res)
            #xbmc.log(out)
            reg = 'file:"(.*?)"'
            movieurl = re.compile(reg).findall(out)
            movieurl = movieurl[1]
            if movieurl:
                addDir('','',movieurl,"1megavideo-link",getImgPath("speedplay_icon"),getImgPath("speedplay_fanart"))
            #addDir('folder','playurl',url,"megavideo",getImgPath("openload_icon"),getImgPath("openload_fanart"))
            # regex = "sources: \[{file:\"(.*?)\"},{file:\"(.*?)\"}]"
            # movieurl = getdatacontent(url,regex)
            # #xbmc.log("--------------------------------------------------------online movie watch---------------------------------------------------------------")
            # #xbmc.log(str(movieurl))
            # movieurl = movieurl[0]
            # if movieurl[0]:
            #     print (movieurl[0])
            #     addDir('','',movieurl[0],"megavideo-link 1",getImgPath("openload_icon"),getImgPath("openload_fanart"))
            # if movieurl[1]:
            #     print (movieurl[1])
            #     movieurl = movieurl[1]
            #     print (movieurl)
            #     movieurl = movieurl.split(',')
            #     movieurl = movieurl[0]
            #     addDir('','',movieurl,"megavideo-link 2",getImgPath("openload_icon"),getImgPath("openload_fanart"))
        if "streamango" in urltemp:
            addDir('folder','playurl',urltemp,"streamango",getImgPath("openload_icon"),getImgPath("openload_fanart"))
        if "verystream" in urltemp:
            addDir('folder','playurl',urltemp,"verystream",getImgPath("openload_icon"),getImgPath("openload_fanart"))
        # if "verystream" in urltemp:
        #     addDir('folder','playurl',urltemp,"verystream",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    # #xbmc.log("------------------------------------scratching - Ends for 1megavideo-link -----------------------------------------------------")
    # #xbmc.log("------------------------------------scratching - for openload, streamango and other links -----------------------------------------------------")
    # reg = '<p><a href="(.*?)" target="_blank" rel="noopener">'
    # data = getonlinemoviewatchcontent(url,reg)
    # #xbmc.log("----------------------Printed Data -----------------------------------------------------")
    # #xbmc.log(str(data))
    # for url in data:
    #     if "openload" in url:
    #         regex = '(?:iframe src|IFRAME SRC|iframe SRC)="(.+?)"'
    #         data = getonlinemoviewatchcontent(url,regex)
    #         #xbmc.log(str(data))
    #         for urltemp in data:
    #             if "oload" in urltemp:
    #                 addDir('folder','playurl',urltemp,"oload",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    #     if "vidwatch" in url:
    #         regex = '(?:iframe src|IFRAME SRC|iframe SRC)="(.+?)"'
    #         data = getonlinemoviewatchcontent(url,regex)
    #         #xbmc.log(str(data))
    #         for urltemp in data:
    #             if "vidwatch" in urltemp:
    #                 urltemp = urltemp.replace('vidwatch4','vidwatch')
    #                 addDir('folder','playurl',urltemp,"vidwatch",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    #     if "openload" in url:
    #         regex = '(?:iframe src|IFRAME SRC|iframe SRC)="(.+?)"'
    #         data = getonlinemoviewatchcontent(url,regex)
    #         #xbmc.log(str(data))
    #         for urltemp in data:
    #             if "oload" in urltemp:
    #                 addDir('folder','playurl',urltemp,"openload",getImgPath("openload_icon"),getImgPath("openload_fanart"))

    #     if "streamango" in url:
    #         regex = '(?:iframe src|IFRAME SRC|iframe SRC)="(.+?)"'
    #         data = getonlinemoviewatchcontent(url,regex)
    #         #xbmc.log(str(data))
    #         for urltemp in data:
    #             if "streamango" in urltemp:
    #                 addDir('folder','playurl',urltemp,"streamango",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    #     if "stremango" in url:
    #         regex = '(?:iframe src|IFRAME SRC|iframe SRC)="(.+?)"'
    #         data = getonlinemoviewatchcontent(url,regex)
    #         #xbmc.log(str(data))
    #         for urltemp in data:
    #             if "streamango" in urltemp:
    #                 addDir('folder','playurl',urltemp,"streamango",getImgPath("openload_icon"),getImgPath("openload_fanart"))


    # if (getdatacontent(url,"button-openload")):
    #     openload = getstreamurl(url,"https://onlinemoviewatchs.io/servers/openload.php?pname=",data[0])
    #     if openload:
    #         try:
    #             movieurl = resolveurl.HostedMediaFile(openload)
    #             movieurl = movieurl.resolve()
    #             if movieurl:
    #                 addDir('folder','playurl',playurl,"openload",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    #         except:
    #             dialog.ok('openload', 'Unable to locate video')
    # if (getdatacontent(url,"button-streamango")):
    #     streamango = getstreamurl(url,"https://onlinemoviewatchs.io/servers/streamango.php?pname=",data[0])
    #     if streamango:
    #         try:
    #             movieurl = resolveurl.HostedMediaFile(streamango)
    #             movieurl = movieurl.resolve()
    #             if movieurl:
    #                 addDir('folder','playurl',playurl,"streamango",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    #         except:
    #             dialog.ok('streamango', 'Unable to locate video')
    # if (getdatacontent(url,"button-thevideo")):
    #     thevideo = getstreamurl(url,"https://onlinemoviewatchs.io/servers/thevideo.php?pname=",data[0])
    #     if thevideo:
    #         try:
    #             movieurl = resolveurl.HostedMediaFile(thevideo)
    #             movieurl = movieurl.resolve()
    #             if movieurl:
    #                 addDir('folder','playurl',playurl,"thevideo",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    #         except:
    #             dialog.ok('thevideo', 'Unable to locate video')
    xbmc.log(url)
    headers = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Sec-Fetch-Site': 'same-origin',
    'Referer': 'https://www11.onlinemoviewatch.org/movies/telugu-movies-2019',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr;q=0.6',
    }

    response = requests.get(url, headers=headers)
    regex = "webkitAllowFullScreen mozallowfullscreen allowfullscreen src=\"(.*?)\""
    res = str(response.content)
    data = re.compile(regex).findall(res)
    xbmc.log("data-------------------------------------------------------")
    xbmc.log(str(data))
    for url in data:
        if "speedwatch" in url:
            addDir('folder','playurl',url,"speedwatch",getImgPath("openload_icon"),getImgPath("openload_fanart"))

    xbmcplugin.endOfDirectory(int(sys.argv[1])) 
    # proxy_handler = urllib2.ProxyHandler({})
    # opener = urllib2.build_opener(proxy_handler)
    # req = urllib2.Request(url)
    # opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    # r = opener.open(req)
    # html = r.read()
    # #reg = "<a href=\"(.*?)\" target=\"loadmovies\">"
    # reg = "data-lazy-src=\"(.*?)\""
    #iframe_speedplay = re.compile(reg).findall(html)
    # reg = "class=\"tabs-catch-all\"><a target=\"_blank\" href=\"(.*?)\">"
    # iframe_open= re.compile(reg).findall(html)
    # if iframe_open:
    #   iframe_open = iframe_open[0]
    # r = requests.get(url)
    # html = r.content

    # iframeSRC = re.compile("<iframe SRC=\"(.*?)\"").findall(html)
    # iframesrc = re.compile("<iframe src=\"(.*?)\"").findall(html)
    # iframe_speedplay1 = re.compile("<iframe SRC=\"(.*?)\"").findall(html)
    # if iframe_speedplay1:
    #     for url in iframe_speedplay1:
    #         if "speedplay" in url:
    #             proxy_handler = urllib2.ProxyHandler({})
    #             opener = urllib2.build_opener(proxy_handler)
    #             req = urllib2.Request(url)
    #             opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    #             r = opener.open(req)
    #             html = r.read()
    #             reg = "<script type='text\/javascript'>eval\((.*=?)"
    #             data = re.compile(reg).findall(html)
    #             res = data[0]
    #             res = res[:-1]
    #             out= unpack(res)
    #             reg = "var player=new Clappr\.Player\({sources:\[\"(.*?)\",\"(.*?)\"\]"
    #             movieurl = re.compile(reg).findall(out)
    #             movieurl = movieurl[0]
    #             if movieurl:
    #                 addDir('','',movieurl[1],"speedplaylink",getImgPath("speedplay_icon"),getImgPath("speedplay_fanart"))
    # if iframeSRC:
    #     for url in iframeSRC:            
    #         if "speedplay" in url:
    #             proxy_handler = urllib2.ProxyHandler({})
    #             opener = urllib2.build_opener(proxy_handler)
    #             req = urllib2.Request(url)
    #             opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    #             r = opener.open(req)
    #             html = r.read()
    #             reg = "<script type='text\/javascript'>eval\((.*=?)"
    #             data = re.compile(reg).findall(html)
    #             res = data[0]
    #             res = res[:-1]
    #             out= unpack(res)
    #             reg = "var player=new Clappr\.Player\({sources:\[\"(.*?)\",\"(.*?)\"\]"
    #             movieurl = re.compile(reg).findall(out)
    #             movieurl = movieurl[0]
    #             if movieurl:
    #                 addDir('','',movieurl[1],"speedplaylink",getImgPath("speedplay_icon"),getImgPath("speedplay_fanart"))
    #         # if "thevideo" in url:
       #         #  url = url.split("=")
       #         #  proxy_handler = urllib2.ProxyHandler({})
       #         #  opener = urllib2.build_opener(proxy_handler)
       #         #  req = urllib2.Request(url[1])
       #         #  opener.addheaders = [('User-agent', 'Mozilla/5.0'),()]
       #         #  r = opener.open(req)
       #         #  html = r.read()
       #         #  movieurl = re.compile("sources: \[{\"file\":\"(.*?)\"").findall(html)
       #         #  if movieurl:
    #         #             ##xbmc.log(str(item))
    #         #             addDir('','',movieurl[0],"thevideo.io",getImgPath("openload_icon"),getImgPath("openload_fanart"))       
    #         if "openload" in url:
    #             try:
    #                 movieurl = resolveurl.HostedMediaFile(url)
    #                 movieurl = movieurl.resolve()
    #                 ##xbmc.log("movie url ---------------------------------------------------------------------------------------------------------------------------------------------")
    #                 ##xbmc.log(str(item))
    #                 if movieurl:
    #                     ##xbmc.log(str(item))
    #                     addDir('','',movieurl,"openloadlink",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    #             except:
    #                 #xbmc.log("Fetch error") 
    #         if "streamango" in url:
    #             try:
    #                 movieurl = resolveurl.HostedMediaFile(url)
    #                 movieurl = movieurl.resolve()
    #                 ##xbmc.log("movie url ---------------------------------------------------------------------------------------------------------------------------------------------")
    #                 ##xbmc.log(str(item))
    #                 if movieurl:
    #                     ##xbmc.log(str(item))
    #                     addDir('','',movieurl,"streamango",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    #             except:
    #                 #xbmc.log("Fetch error") 
    #         if "thevideo" in url:
    #             try:
    #                 url = url.split("=")
    #                 url = url[1]
    #                 movieurl = resolveurl.HostedMediaFile(url)
    #                 movieurl = movieurl.resolve()
    #                 ##xbmc.log("movie url ---------------------------------------------------------------------------------------------------------------------------------------------")
    #                 ##xbmc.log(str(item))
    #                 if movieurl:
    #                     ##xbmc.log(str(item))
    #                     addDir('','',movieurl,"thevideo",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    #             except:
    #                 #xbmc.log("Fetch error") 
    # if iframesrc:
    #         for url in iframesrc:            
    #             if "speedplay" in url:
    #                 proxy_handler = urllib2.ProxyHandler({})
    #                 opener = urllib2.build_opener(proxy_handler)
    #                 req = urllib2.Request(url)
    #                 opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    #                 r = opener.open(req)
    #                 html = r.read()
    #                 reg = "<script type='text\/javascript'>eval\((.*=?)"
    #                 data = re.compile(reg).findall(html)
    #                 res = data[0]
    #                 res = res[:-1]
    #                 out= unpack(res)
    #                 reg = "var player=new Clappr\.Player\({sources:\[\"(.*?)\",\"(.*?)\"\]"
    #                 movieurl = re.compile(reg).findall(out)
    #                 movieurl = movieurl[0]
    #                 if movieurl:
    #                     addDir('','',movieurl[1],"speedplaylink",getImgPath("speedplay_icon"),getImgPath("speedplay_fanart"))
    #             # if "thevideo" in url:
    #                #  url = url.split("=")
    #                #  proxy_handler = urllib2.ProxyHandler({})
    #                #  opener = urllib2.build_opener(proxy_handler)
    #                #  req = urllib2.Request(url[1])
    #                #  opener.addheaders = [('User-agent', 'Mozilla/5.0'),()]
    #                #  r = opener.open(req)
    #                #  html = r.read()
    #                #  movieurl = re.compile("sources: \[{\"file\":\"(.*?)\"").findall(html)
    #                #  if movieurl:
    #             #             ##xbmc.log(str(item))
    #             #             addDir('','',movieurl[0],"thevideo.io",getImgPath("openload_icon"),getImgPath("openload_fanart"))       
    #             if "openload" in url:
    #                 try:
    #                     movieurl = resolveurl.HostedMediaFile(url)
    #                     movieurl = movieurl.resolve()
    #                     ##xbmc.log("movie url ---------------------------------------------------------------------------------------------------------------------------------------------")
    #                     ##xbmc.log(str(item))
    #                     if movieurl:
    #                         ##xbmc.log(str(item))
    #                         addDir('','',movieurl,"openloadlink",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    #                 except:
    #                     #xbmc.log("Fetch error") 
    #             if "streamango" in url:
    #                 try:
    #                     movieurl = resolveurl.HostedMediaFile(url)
    #                     movieurl = movieurl.resolve()
    #                     ##xbmc.log("movie url ---------------------------------------------------------------------------------------------------------------------------------------------")
    #                     ##xbmc.log(str(item))
    #                     if movieurl:
    #                         ##xbmc.log(str(item))
    #                         addDir('','',movieurl,"streamango",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    #                 except:
    #                     #xbmc.log("Fetch error") 
    #             if "thevideo" in url:
    #                 try:
    #                     url = url.split("=")
    #                     url = url[1]
    #                     movieurl = resolveurl.HostedMediaFile(url)
    #                     movieurl = movieurl.resolve()
    #                     ##xbmc.log("movie url ---------------------------------------------------------------------------------------------------------------------------------------------")
    #                     ##xbmc.log(str(item))
    #                     if movieurl:
    #                         ##xbmc.log(str(item))
    #                         addDir('','',movieurl,"thevideo",getImgPath("openload_icon"),getImgPath("openload_fanart"))
    #                 except:
    #                     #xbmc.log("Fetch error")               
    
